# StephenKing SDK utility: feature_add
module StephenKingUtilities
  FeatureAdd = ->(ctx, f) {
    ctx.client.features << f
  }
end
