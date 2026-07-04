-- Typed models for the StephenKing SDK (LuaLS annotations).
--
-- GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
-- params (op.<name>.points[].args.params[]). Field/param types come from the
-- canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
-- @voxgig/apidef VALID_CANON). Annotations only — no runtime effect. Do not
-- edit by hand.

---@class Book
---@field id? number
---@field isbn? string
---@field page? number
---@field publisher? string
---@field title? string
---@field year? number

---@class BookLoadMatch
---@field id number

---@class BookListMatch

---@class Short
---@field collection? string
---@field id? number
---@field title? string
---@field type? string
---@field year? number

---@class ShortLoadMatch
---@field id number

---@class ShortListMatch

---@class Villain
---@field gender? string
---@field id? number
---@field name? string
---@field note? string
---@field status? string
---@field work? string

---@class VillainLoadMatch
---@field id number

---@class VillainListMatch

local M = {}

return M
