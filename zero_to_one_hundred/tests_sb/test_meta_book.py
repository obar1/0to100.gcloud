from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
<<<<<<< HEAD


# pylint: disable=W0613
def test_init(get_config_map, persist_fs, process_fs, http_url):
    actual = MetaBook(
        SBConfigMap(persist_fs),
        persist_fs,
        process_fs,
=======
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as sb_persist_fs
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as sb_process_fs


# pylint: disable=W0613
def test_init(get_config_map, http_url):
    actual = MetaBook(
        SBConfigMap(sb_persist_fs),
        sb_persist_fs,
        sb_process_fs,
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
        http_url,
    )
    assert str(actual.isbn).endswith("9780135956977")
    assert str(actual.contents_path).endswith("9780135956977")
    assert str(actual.path_pdf).endswith("9780135956977/9780135956977.pdf")
    assert str(actual.path_epub).endswith("9780135956977/9780135956977.epub")
    assert str(actual.path_img).endswith("9780135956977/9780135956977.png")


<<<<<<< HEAD
def test_build_from_dir(get_config_map, persist_fs, process_fs):
    assert (
        MetaBook.build_from_dir(
            SBConfigMap(persist_fs),
            persist_fs,
            process_fs,
=======
def test_build_from_dir(get_config_map):
    assert (
        MetaBook.build_from_dir(
            SBConfigMap(sb_persist_fs),
            sb_persist_fs,
            sb_process_fs,
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
            "./books/9780135956977",
        ).isbn
        == "9780135956977"
    )


def test_is_valid_ebook_path():
    dirs = ["0123456789", "1234567890123", "books", "ABC"]
    actual = [d for d in dirs if MetaBook.is_valid_ebook_path(d)]
    assert actual == ["1234567890123"]
