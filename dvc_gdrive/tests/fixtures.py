import pytest
from dvc.fs import GDriveFileSystem

from .cloud import GDrive


@pytest.fixture
def make_gdrive():
    def _make_gdrive():
        from urllib.parse import urlparse

        url = GDrive.get_url()
        ret = GDrive(url)
        fs = GDriveFileSystem(**ret.config)

        parsed = urlparse(url)
        bucket = parsed.hostname
        path = parsed.path.lstrip("/")

        fs.fs._gdrive_create_dir(  # noqa, pylint: disable=protected-access
            bucket, path  # noqa, pylint: disable=protected-access
        )
        return ret

    return _make_gdrive


@pytest.fixture
def gdrive(make_gdrive):
    return make_gdrive()
