package = "voxgig-sdk-stephen-king"
version = "0.0.1-1"
source = {
  -- git+https (GitHub dropped git:// in 2022); pin the install to the release
  -- tag pushed by `make publish`, and point at the lua/ subdir of the monorepo.
  url = "git+https://github.com/voxgig-sdk/stephen-king-sdk.git",
  tag = "lua/v0.0.1",
  dir = "stephen-king-sdk/lua"
}
description = {
  summary = "Unofficial generated Lua SDK for the Stephen King public API. Not affiliated with or endorsed by the upstream API provider.",
  homepage = "https://github.com/voxgig-sdk/stephen-king-sdk",
  issues_url = "https://github.com/voxgig-sdk/stephen-king-sdk/issues",
  license = "MIT",
  labels = { "voxgig", "sdk", "generated-sdk", "openapi", "api-client", "stephen-king" }
}
dependencies = {
  "lua >= 5.3",
  "dkjson >= 2.5",
}
build = {
  type = "builtin",
  modules = {
    ["stephen-king_sdk"] = "stephen-king_sdk.lua",
    ["config"] = "config.lua",
    ["config_shared"] = "config_shared.lua",
    ["features"] = "features.lua",
  }
}
