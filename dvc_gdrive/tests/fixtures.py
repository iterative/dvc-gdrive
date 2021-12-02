import os

import pytest


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(
        str(pytestconfig.rootdir), "dvc_gdrive", "tests", "docker-compose.yml"
    )


@pytest.fixture
def make_gdrive():
    def _make_gdrive():
        raise NotImplementedError

    return _make_gdrive


@pytest.fixture
def gdrive(make_gdrive):
    return make_gdrive()

