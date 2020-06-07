import pickle
import os
from pytest import fixture


def pytest_configure(config):
    """Optional markers"""
    config.addinivalue_line(
        "markers", "create_file(file_name): name of file that will be created in resources folder"
    )


@fixture(scope="session")
def test_resource_dir():
    """Location of Test Resource files"""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'tests',
        'resources',
    )


@fixture(scope="module")
def mocked_session(test_resource_dir):
    file_location = os.path.join(test_resource_dir, "session.txt")
    with open(file_location, "rb") as f:
        return pickle.load(f)


@fixture(scope="module")
def mocked_history(test_resource_dir):
    file_location = os.path.join(test_resource_dir, "history.txt")
    with open(file_location, "rb") as f:
        return pickle.load(f)


@fixture(scope="module")
def mocked_missions(test_resource_dir):
    file_location = os.path.join(test_resource_dir, "missions.txt")
    with open(file_location, "rb") as f:
        return pickle.load(f)


@fixture
def create_file(request, test_resource_dir):
    """
    To use, annotate the target function with @pytest.mark.create_file("name_of_file.txt")
    Pass `create_file` as a parameter to the test function, and use create_file.append(myobj)
    to write myobj to `tests/resources/name_of_file.txt`

    See tests/resources/resource_maker.py for example
    """
    content_list = []
    yield content_list
    for mark in request.node.iter_markers("create_file"):
        for file, content in zip(mark.args, content_list):
            file_location = os.path.join(test_resource_dir, file)
            with open(file_location, "wb") as f:
                pickle.dump(content, f)
