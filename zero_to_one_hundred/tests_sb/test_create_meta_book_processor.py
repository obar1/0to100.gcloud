from subprocess import CalledProcessError
from unittest.mock import patch

from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.processors.snatch_book_processor import (
    SnatchBookProcessor,
)
<<<<<<< HEAD


@patch("zero_to_one_hundred.factories.sb_factory.SBFactory.get_processor")
def test_process(get_config_map, persist_fs, process_fs, http_url):
    actual: SnatchBookProcessor = SBFactory(
        get_config_map,
        persist_fs,
        process_fs,
=======
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as sb_persist_fs
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as sb_process_fs


@patch("zero_to_one_hundred.factories.sb_factory.SBFactory.get_processor")
def test_process(get_config_map, http_url):
    actual: SnatchBookProcessor = SBFactory(
        get_config_map,
        sb_persist_fs,
        sb_process_fs,
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
    ).get_processor([None, "snatch_book", http_url])
    for p in actual:
        try:
            p.process()
        except CalledProcessError:
            pass
