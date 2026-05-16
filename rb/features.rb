# StephenKing SDK feature factory

require_relative 'feature/base_feature'
require_relative 'feature/test_feature'


module StephenKingFeatures
  def self.make_feature(name)
    case name
    when "base"
      StephenKingBaseFeature.new
    when "test"
      StephenKingTestFeature.new
    else
      StephenKingBaseFeature.new
    end
  end
end
