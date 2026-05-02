from lib.control_flow import admin_login, hows_the_weather, fizzbuzz, calculator


def test_admin_login_grants_access_for_admin_credentials():
    assert admin_login("admin", "12345") == "Access granted"
    assert admin_login("ADMIN", "12345") == "Access granted"


def test_admin_login_denies_access_for_invalid_credentials():
    assert admin_login("admin", "wrong") == "Access denied"
    assert admin_login("user", "12345") == "Access denied"


def test_hows_the_weather():
    assert hows_the_weather(30) == "It's brisk out there!"
    assert hows_the_weather(50) == "It's a little chilly out there!"
    assert hows_the_weather(80) == "It's perfect out there!"
    assert hows_the_weather(90) == "It's too dang hot out there!"


def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(8) == 8


def test_calculator():
    assert calculator("+", 3, 5) == 8
    assert calculator("-", 10, 4) == 6
    assert calculator("*", 6, 7) == 42
    assert calculator("/", 10, 2) == 5
    assert calculator("^", 2, 2) is None



