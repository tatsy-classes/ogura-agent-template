def pytest_addoption(parser):
    parser.addoption("--path", action="store", default="data/level1/sample.jpg")
