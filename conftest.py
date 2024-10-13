import pytest

def pytest_addoption(parser):
    parser.addoption("--stopat", action="store", default="", help="Specify the test function to stop at")

@pytest.fixture
def stop_at(request):
    return request.config.getoption("--stopat")