from zero_to_one_hundred.factories.sb_factory import SBFactory
<<<<<<< HEAD
=======
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e


# pylint: disable=W0621


<<<<<<< HEAD
def test_get_processor(get_config_map, persist_fs, process_fs):
=======
def test_get_processor(get_config_map):
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
    SBFactory(get_config_map, persist_fs, process_fs)


def test_N_processor():
    assert len(SBFactory.SUPPORTED_PROCESSOR) == 4
