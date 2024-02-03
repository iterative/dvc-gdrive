import pytest

from dvc.testing.api_tests import (  # noqa: F401
    TestAPI,
)
from dvc.testing.remote_tests import (  # noqa: F401
    TestRemote,
)
from dvc.testing.workspace_tests import TestGetUrl as _TestGetUrl
from dvc.testing.workspace_tests import TestImport as _TestImport
from dvc.testing.workspace_tests import TestLsUrl as _TestLsUrl


@pytest.fixture
def cloud(make_cloud):
    return make_cloud(typ="gdrive")


@pytest.fixture
def remote(make_remote):
    return make_remote(name="upstream", typ="gdrive")


@pytest.fixture
def workspace(make_workspace):
    return make_workspace(name="workspace", typ="gdrive")


@pytest.mark.xfail
class TestImport(_TestImport):
    pass


@pytest.mark.xfail
class TestLsUrl(_TestLsUrl):
    pass


@pytest.mark.xfail
class TestGetUrl(_TestGetUrl):
    pass
