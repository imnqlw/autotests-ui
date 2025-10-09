import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0



@pytest.fixture(params=["chromium", "webkit", "firefox"])
# Фикстура будет возвращать три разных браузера
# Соотвественно все автотесты использующие данную фикстуру будут запускаться три раза
def browser(request: SubRequest) -> str:
    return request.param  # Внутри атрибута param находится одно из значений "chromium", "webkit", "firefox"


# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_open_browser(browser: str):
    # Используем фикстуру в автотесте, она вернет нам браузер в виде строки
    print(f"Running test on browser: {browser}")


# Для тестовых классов параметризация указывается для самого класса
@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    # Параметр "user" передается в качестве аргумента в каждый тестовый метод класса
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    # Аналогично тут передается "user"
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

# Словарь пользователей: номер телефона — ключ, описание — значение
users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),  # Передаем список номеров телефонов
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"  # Генерируем идентификаторы динамически
)
def test_identifiers(phone_number: str):
    pass

@pytest.mark.parametrize(
    "value",
    [1, pytest.param(2, marks=pytest.mark.skip(reason="Not supported")), 3]
)
def test_example(value):
    pass

@pytest.mark.parametrize(
    "input_value",
    [
        pytest.param(1, marks=pytest.mark.xfail(reason="Known issue with 1")),
        2,
        pytest.param(3, marks=pytest.mark.skip(reason="Feature not implemented for 3")),
    ]
)
def test_function(input_value):
    assert input_value != 1