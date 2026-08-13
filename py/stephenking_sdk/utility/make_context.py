# StephenKing SDK utility: make_context

from stephenking_sdk.core.context import StephenKingContext


def make_context_util(ctxmap, basectx):
    return StephenKingContext(ctxmap, basectx)
