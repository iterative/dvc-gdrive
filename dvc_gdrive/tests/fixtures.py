import pytest

from .cloud import GDrive


@pytest.fixture
def make_gdrive():
    def _make_gdrive():
        return GDrive(GDrive.get_url())

    return _make_gdrive


@pytest.fixture
def gdrive(make_gdrive):
    return make_gdrive()
