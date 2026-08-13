# StephenKing SDK utility registration
require_relative '../core/utility_type'
require_relative 'clean'
require_relative 'done'
require_relative 'make_error'
require_relative 'feature_add'
require_relative 'feature_hook'
require_relative 'feature_init'
require_relative 'fetcher'
require_relative 'make_fetch_def'
require_relative 'make_context'
require_relative 'make_options'
require_relative 'make_request'
require_relative 'make_response'
require_relative 'make_result'
require_relative 'make_point'
require_relative 'make_spec'
require_relative 'make_url'
require_relative 'param'
require_relative 'prepare_auth'
require_relative 'prepare_body'
require_relative 'prepare_headers'
require_relative 'prepare_method'
require_relative 'prepare_params'
require_relative 'prepare_path'
require_relative 'prepare_query'
require_relative 'graphql'
require_relative 'result_basic'
require_relative 'result_body'
require_relative 'result_headers'
require_relative 'transform_request'
require_relative 'transform_response'

StephenKingUtility.registrar = ->(u) {
  u.clean = StephenKingUtilities::Clean
  u.done = StephenKingUtilities::Done
  u.make_error = StephenKingUtilities::MakeError
  u.feature_add = StephenKingUtilities::FeatureAdd
  u.feature_hook = StephenKingUtilities::FeatureHook
  u.feature_init = StephenKingUtilities::FeatureInit
  u.fetcher = StephenKingUtilities::Fetcher
  u.make_fetch_def = StephenKingUtilities::MakeFetchDef
  u.make_context = StephenKingUtilities::MakeContext
  u.make_options = StephenKingUtilities::MakeOptions
  u.make_request = StephenKingUtilities::MakeRequest
  u.make_response = StephenKingUtilities::MakeResponse
  u.make_result = StephenKingUtilities::MakeResult
  u.make_point = StephenKingUtilities::MakePoint
  u.make_spec = StephenKingUtilities::MakeSpec
  u.make_url = StephenKingUtilities::MakeUrl
  u.param = StephenKingUtilities::Param
  u.prepare_auth = StephenKingUtilities::PrepareAuth
  u.prepare_body = StephenKingUtilities::PrepareBody
  u.prepare_headers = StephenKingUtilities::PrepareHeaders
  u.prepare_method = StephenKingUtilities::PrepareMethod
  u.prepare_params = StephenKingUtilities::PrepareParams
  u.prepare_path = StephenKingUtilities::PreparePath
  u.prepare_query = StephenKingUtilities::PrepareQuery
  u.graphql_body = StephenKingUtilities::GraphqlBody
  u.graphql_errors = StephenKingUtilities::GraphqlErrors
  u.result_basic = StephenKingUtilities::ResultBasic
  u.result_body = StephenKingUtilities::ResultBody
  u.result_headers = StephenKingUtilities::ResultHeaders
  u.transform_request = StephenKingUtilities::TransformRequest
  u.transform_response = StephenKingUtilities::TransformResponse
}
