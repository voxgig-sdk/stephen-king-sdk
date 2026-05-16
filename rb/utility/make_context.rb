# StephenKing SDK utility: make_context
require_relative '../core/context'
module StephenKingUtilities
  MakeContext = ->(ctxmap, basectx) {
    StephenKingContext.new(ctxmap, basectx)
  }
end
