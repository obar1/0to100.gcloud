from zero_to_one_hundred.models.section import Section
<<<<<<< HEAD


def test_init(get_config_map, persist_fs, process_fs, http_url):
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
=======
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs


def test_init(get_config_map, http_url):
    actual = Section(get_config_map, process_fs, process_fs, http_url)
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
    assert actual.http_url == "https://cloud.google.com/abc"
    assert actual.dir_name == "https§§§cloud.google.com§abc"
    assert (
        actual.dir_readme_md
        == get_config_map.get_repo_path + "/" + "https§§§cloud.google.com§abc/readme.md"
    )


<<<<<<< HEAD
def test_write(get_config_map, persist_fs, process_fs, http_url):
=======
def test_write(get_config_map, http_url):
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
    actual = Section(get_config_map, persist_fs, process_fs, http_url)


def test_build_from_dir(
    get_config_map, persist_fs, process_fs, simple_http, simple_dir
):
    assert (
        Section.build_from_dir(
            persist_fs, process_fs, get_config_map, simple_http
        ).dir_name
        == simple_dir
    )


def test_section_is_quest(get_gcp_config_map, persist_fs, process_fs):
    http_url = "https://www.cloudskillsboost.google/quests/257"
<<<<<<< HEAD
    actual = Section(get_gcp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_gcp_quest
=======
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    assert actual.is_quest
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e


def test_section_is_lab(get_gcp_config_map, persist_fs, process_fs):
    http_url = "https://www.cloudskillsboost.google/course_sessions/3062553/labs"
<<<<<<< HEAD
    actual = Section(get_gcp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_gcp_lab
=======
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    assert actual.is_lab
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e


def test_section_is_template(get_gcp_config_map, persist_fs, process_fs):
    http_url = "https://www.cloudskillsboost.google/course_templates/536"
<<<<<<< HEAD
    actual = Section(get_gcp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_gcp_template
=======
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    assert actual.is_template
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e


def test_section_is_gamee(get_gcp_config_map, persist_fs, process_fs):
    http_url = "https://www.cloudskillsboost.google/games/4423"
<<<<<<< HEAD
    actual = Section(get_gcp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_gcp_game


def test_is_datacamp_project(get_datacamp_config_map, persist_fs, process_fs):
    http_url = "https://app.datacamp.com/learn/projects/1833"
    actual = Section(get_datacamp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_datacamp_project


def test_is_datacamp_tutorial(get_datacamp_config_map, persist_fs, process_fs):
    http_url = "https://app.datacamp.com/learn/tutorials/git-push-pull"
    actual = Section(get_datacamp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_datacamp_tutorial


def test_is_datacamp_course(get_datacamp_config_map, persist_fs, process_fs):
    http_url = "https://app.datacamp.com/learn/courses/writing-efficient-python-code"
    actual = Section(get_datacamp_config_map, persist_fs, process_fs, http_url)
    assert actual.is_datacamp_course


def test_gcp_get_format_as_md(get_gcp_config_map, persist_fs, process_fs):
    http_url = "https://www.cloudskillsboost.google/games/4423"
    actual = Section.build_from_dir(
        persist_fs, process_fs, get_gcp_config_map, http_url
    )
    assert actual.get_format_as_md == """:snake:"""
=======
    actual = Section(get_config_map, persist_fs, process_fs, http_url)
    assert actual.is_game
>>>>>>> a04ee23055442648c912c5aaef19708538794f5e
