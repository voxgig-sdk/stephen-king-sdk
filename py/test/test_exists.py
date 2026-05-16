# ProjectName SDK exists test

import pytest
from stephenking_sdk import StephenKingSDK


class TestExists:

    def test_should_create_test_sdk(self):
        testsdk = StephenKingSDK.test(None, None)
        assert testsdk is not None
