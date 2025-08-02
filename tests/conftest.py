import pytest




@pytest.fixture(scope='module')
def set_up():
    print('НАЧАЛО ТЕСТИРОВАНИЯ')
    yield
    print('КОНЕЦ ТЕСТИРОВАНИЯ')