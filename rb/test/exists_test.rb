# StephenKing SDK exists test

require "minitest/autorun"
require_relative "../StephenKing_sdk"

class ExistsTest < Minitest::Test
  def test_create_test_sdk
    testsdk = StephenKingSDK.test(nil, nil)
    assert !testsdk.nil?
  end
end
