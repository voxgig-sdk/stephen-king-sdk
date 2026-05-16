# StephenKing SDK feature factory

from feature.base_feature import StephenKingBaseFeature
from feature.test_feature import StephenKingTestFeature


def _make_feature(name):
    features = {
        "base": lambda: StephenKingBaseFeature(),
        "test": lambda: StephenKingTestFeature(),
    }
    factory = features.get(name)
    if factory is not None:
        return factory()
    return features["base"]()
