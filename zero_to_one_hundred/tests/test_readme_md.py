from zero_to_one_hundred.models.readme_md import ReadMeMD
from zero_to_one_hundred.models.section import Section
<<<<<<< HEAD


def test_refresh_links(get_config_map, persist_fs, process_fs, http_url):
    ReadMeMD(
        get_config_map,
        persist_fs,
        process_fs,
        Section.from_http_url_to_dir,
=======
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS


def test_refresh_links(get_config_map, http_url):
    ReadMeMD(
        get_config_map,
        ZTOHPersistFS,
        ZTOHProcessFS,
        Section.from_dir_to_http_url,
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
        http_url,
    )
