from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS

ZTOH_MAP = "ztoh-map"


class ZTOHConfigMap(AConfigMap):
    def __init__(self, persist_fs: ZTOHPersistFS):
        super().__init__(persist_fs)

    @property
    def get_repo_path(self):
<<<<<<< HEAD
        return self.load["repo"]["path"]
=======
        return self.persist_fs.abs_path(self.load["repo"]["path"])
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e

    @property
    def get_repo_map_md(self):
        return self.load["repo"]["map_md"]

    @property
    def get_repo_sorted(self) -> bool:
        return bool(self.load["repo"]["sorted"])
<<<<<<< HEAD

    @property
    def get_repo_legend_type(self) -> str | None:
        return self.load["repo"].get("legend_type")
=======
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
