import pytest
from dvc.testing.api_tests import (  # noqa, pylint: disable=unused-import
    TestAPI,
)
from dvc.testing.remote_tests import (  # noqa, pylint: disable=unused-import
    TestRemote,
)
from dvc.testing.workspace_tests import TestAdd as _TestAdd
from dvc.testing.workspace_tests import (  # noqa, pylint: disable=unused-import
    TestGetUrl,
)
from dvc.testing.workspace_tests import TestImport as _TestImport
from dvc.testing.workspace_tests import (  # noqa, pylint: disable=unused-import
    TestLsUrl,
)


@pytest.fixture
def cloud(make_cloud):
    yield make_cloud(typ="gdrive")


@pytest.fixture
def remote(make_remote):
    yield make_remote(name="upstream", typ="gdrive")


@pytest.fixture
def workspace(make_workspace):
    yield make_workspace(name="workspace", typ="gdrive")


class TestImport(_TestImport):
    pass


class TestAdd(_TestAdd):
    pass
