from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.models.metadata import Metadata
<<<<<<< HEAD


def test_init(get_config_map, persist_fs, process_fs, http_url, isbn):
    actual = Metadata(
        SBConfigMap(persist_fs),
        persist_fs,
        process_fs,
=======
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as sb_persist_fs
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as sb_process_fs


def test_init(get_config_map, http_url, isbn):
    actual = Metadata(
        SBConfigMap(sb_persist_fs),
        sb_persist_fs,
        sb_process_fs,
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
        MetaBook.get_isbn,
        http_url,
    )
    assert str(actual.isbn).endswith(isbn)
    assert str(actual.http_url) == http_url
    assert actual.pages_tot == 0
    assert actual.page_curr == 0


<<<<<<< HEAD
def test_get_page_perc(get_config_map, persist_fs, process_fs, http_url):
    actual = Metadata(
        SBConfigMap(persist_fs),
        persist_fs,
        process_fs,
=======
def test_get_page_perc(get_config_map, http_url):
    actual = Metadata(
        SBConfigMap(sb_persist_fs),
        sb_persist_fs,
        sb_process_fs,
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
        MetaBook.get_isbn,
        http_url,
        99,
        999,
    )
    assert actual.get_page_perc == "9.9%"
