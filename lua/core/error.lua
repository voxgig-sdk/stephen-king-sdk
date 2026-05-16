-- StephenKing SDK error

local StephenKingError = {}
StephenKingError.__index = StephenKingError


function StephenKingError.new(code, msg, ctx)
  local self = setmetatable({}, StephenKingError)
  self.is_sdk_error = true
  self.sdk = "StephenKing"
  self.code = code or ""
  self.msg = msg or ""
  self.ctx = ctx
  self.result = nil
  self.spec = nil
  return self
end


function StephenKingError:error()
  return self.msg
end


function StephenKingError:__tostring()
  return self.msg
end


return StephenKingError
