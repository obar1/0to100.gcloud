<<<<<<< HEAD
from zero_to_one_hundred.configs.sb_config_map import SAFARI_BOOKS_MAP, SBConfigMap
=======
from zero_to_one_hundred.configs.sb_config_map import SAFARI_BOOKS_MAP
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e

# pylint: disable=W0621,W0613


<<<<<<< HEAD
def test_provide__pass(get_config_map: SBConfigMap):
=======
def test_provide__pass(get_config_map):
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
    actual = get_config_map
    assert actual.get_type == SAFARI_BOOKS_MAP
    assert actual.get_books_path is not None
    assert actual.get_download_engine_books_path is not None
    assert actual.get_oreilly_username is not None
    assert actual.get_oreilly_userpassword is not None
    assert actual.get_oreilly_userpassword is not None
    assert actual.get_split_pdf_pages == 100
<<<<<<< HEAD
    assert actual.get_download_books is True


def test__repr__(get_config_map: SBConfigMap, get_map_yaml_path: str):
=======


def test__repr__(get_config_map, get_map_yaml_path):
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
    actual = get_config_map
    assert (
        repr(actual)
        == f"MAP_YAML_PATH from {get_map_yaml_path} type {get_config_map.get_type}"
    )
