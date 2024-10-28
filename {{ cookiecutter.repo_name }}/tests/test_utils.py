import pytest
import yaml
from {{ cookiecutter.package_name }}.utils.util import yaml2dict


@pytest.fixture
def example_yaml():
    return {"a": 1, "b": "2", "c": [3, 4, 5], "d": {6: 7}, "e": True}


def test_yaml2dict(tmp_path, example_yaml):
    fpath = tmp_path / "tmp.yaml"
    yaml.dump(example_yaml, open(fpath, "w"))
    conf = yaml2dict(fpath)
    assert conf == example_yaml

