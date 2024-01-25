from zero_to_one_hundred.factories.sb_factory import SBFactory

from zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
<<<<<<< HEAD
=======
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e


# pylint: disable=W0621


<<<<<<< HEAD
def test_pass(
    get_config_map,
    persist_fs,
    process_fs,
):
    actual = SBFactoryProvider(persist_fs, process_fs)
=======
def test_pass(get_config_map):
    actual = SBFactoryProvider(SBPersistFS, SBProcessFS)
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
    assert isinstance(actual.provide(), SBFactory)
