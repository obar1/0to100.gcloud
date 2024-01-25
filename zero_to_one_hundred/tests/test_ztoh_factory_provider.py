import pytest

from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
<<<<<<< HEAD
=======
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e


# pylint: disable=W0621,W0613


<<<<<<< HEAD
def test_pass(get_config_map, persist_fs, process_fs):
    actual = ZTOHFactoryProvider(persist_fs, process_fs)
    assert isinstance(actual.provide(), ZTOHFactory)


def test_provide__unsupported(env_unsupported_map_yaml, persist_fs, process_fs):
    with pytest.raises(NotImplementedError):
        ZTOHFactoryProvider(persist_fs, process_fs).provide()
=======
def test_pass(get_config_map):
    actual = ZTOHFactoryProvider(ZTOHPersistFS, ZTOHProcessFS)
    assert isinstance(actual.provide(), ZTOHFactory)


def test_provide__unsupported(get_unsupported_factory_provider):
    with pytest.raises(NotImplementedError):
        get_unsupported_factory_provider.provide()
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
