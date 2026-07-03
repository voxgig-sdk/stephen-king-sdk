# Villain entity test

require "minitest/autorun"
require "json"
require_relative "../StephenKing_sdk"
require_relative "runner"

class VillainEntityTest < Minitest::Test
  def test_create_instance
    testsdk = StephenKingSDK.test(nil, nil)
    ent = testsdk.Villain(nil)
    assert !ent.nil?
  end

  def test_basic_flow
    setup = villain_basic_setup(nil)
    # Per-op sdk-test-control.json skip.
    _live = setup[:live] || false
    ["list", "load"].each do |_op|
      _should_skip, _reason = Runner.is_control_skipped("entityOp", "villain." + _op, _live ? "live" : "unit")
      if _should_skip
        skip(_reason || "skipped via sdk-test-control.json")
        return
      end
    end
    # The basic flow consumes synthetic IDs from the fixture. In live mode
    # without an *_ENTID env override, those IDs hit the live API and 4xx.
    if setup[:synthetic_only]
      skip "live entity test uses synthetic IDs from fixture — set STEPHENKING_TEST_VILLAIN_ENTID JSON to run live"
      return
    end
    client = setup[:client]

    # Bootstrap entity data from existing test data.
    villain_ref01_data_raw = Vs.items(Helpers.to_map(
      Vs.getpath(setup[:data], "existing.villain")))
    villain_ref01_data = nil
    if villain_ref01_data_raw.length > 0
      villain_ref01_data = Helpers.to_map(villain_ref01_data_raw[0][1])
    end

    # LIST
    villain_ref01_ent = client.Villain(nil)
    villain_ref01_match = {}

    villain_ref01_list_result, err = villain_ref01_ent.list(villain_ref01_match, nil)
    assert_nil err
    assert villain_ref01_list_result.is_a?(Array)

    # LOAD
    villain_ref01_match_dt0 = {
      "id" => villain_ref01_data["id"],
    }
    villain_ref01_data_dt0_loaded, err = villain_ref01_ent.load(villain_ref01_match_dt0, nil)
    assert_nil err
    villain_ref01_data_dt0_load_result = Helpers.to_map(villain_ref01_data_dt0_loaded)
    assert !villain_ref01_data_dt0_load_result.nil?
    assert_equal villain_ref01_data_dt0_load_result["id"], villain_ref01_data["id"]

  end
end

def villain_basic_setup(extra)
  Runner.load_env_local

  entity_data_file = File.join(__dir__, "..", "..", ".sdk", "test", "entity", "villain", "VillainTestData.json")
  entity_data_source = File.read(entity_data_file)
  entity_data = JSON.parse(entity_data_source)

  options = {}
  options["entity"] = entity_data["existing"]

  client = StephenKingSDK.test(options, extra)

  # Generate idmap via transform.
  idmap = Vs.transform(
    ["villain01", "villain02", "villain03"],
    {
      "`$PACK`" => ["", {
        "`$KEY`" => "`$COPY`",
        "`$VAL`" => ["`$FORMAT`", "upper", "`$COPY`"],
      }],
    }
  )

  # Detect ENTID env override before envOverride consumes it. When live
  # mode is on without a real override, the basic test runs against synthetic
  # IDs from the fixture and 4xx's. Surface this so the test can skip.
  entid_env_raw = ENV["STEPHENKING_TEST_VILLAIN_ENTID"]
  idmap_overridden = !entid_env_raw.nil? && entid_env_raw.strip.start_with?("{")

  env = Runner.env_override({
    "STEPHENKING_TEST_VILLAIN_ENTID" => idmap,
    "STEPHENKING_TEST_LIVE" => "FALSE",
    "STEPHENKING_TEST_EXPLAIN" => "FALSE",
    "STEPHENKING_APIKEY" => "NONE",
  })

  idmap_resolved = Helpers.to_map(
    env["STEPHENKING_TEST_VILLAIN_ENTID"])
  if idmap_resolved.nil?
    idmap_resolved = Helpers.to_map(idmap)
  end

  if env["STEPHENKING_TEST_LIVE"] == "TRUE"
    merged_opts = Vs.merge([
      {
        "apikey" => env["STEPHENKING_APIKEY"],
      },
      extra || {},
    ])
    client = StephenKingSDK.new(Helpers.to_map(merged_opts))
  end

  live = env["STEPHENKING_TEST_LIVE"] == "TRUE"
  {
    client: client,
    data: entity_data,
    idmap: idmap_resolved,
    env: env,
    explain: env["STEPHENKING_TEST_EXPLAIN"] == "TRUE",
    live: live,
    synthetic_only: live && !idmap_overridden,
    now: (Time.now.to_f * 1000).to_i,
  }
end
