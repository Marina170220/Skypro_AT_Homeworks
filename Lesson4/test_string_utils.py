from string_utils import StringUtils
import pytest

utils = StringUtils()


# test capitalize

@pytest.mark.parametrize("input_data, result", [
    ("тест", "Тест"),
    ("Тест", "Тест"),
    ("ТЕСТ", "Тест"),
    ("текст с пробелами", "Текст с пробелами"),
    ("test", "Test"),
    ("Test", "Test"),
    ("TEST", "Test"),
    ("text with spaces", "Text with spaces"),
    ("56780", "56780"),

    (" ", " "),
    ("", ""),
    ("123тест", "123тест"),
])
def test_capitalize(input_data, result):
    assert utils.capitilize(input_data) == result


@pytest.mark.xfail()
def test_capitalize_int():
    assert utils.capitilize(123) == 123


@pytest.mark.xfail()
def test_capitalize_none():
    assert utils.capitilize(None) == None


# test trim

@pytest.mark.parametrize("input_data, result", [
    (" тест", "тест"),
    ("  Тест", "Тест"),
    ("  ТЕСТ  ", "ТЕСТ  "),
    (" текст с пробелами", "текст с пробелами"),
    (" test ", "test "),
    ("  Test    ", "Test    "),
    (" T-EST", "T-EST"),
    ("text with spaces ", "text with spaces "),
    (" 56780", "56780"),

    (" ", ""),
    ("", ""),
])
def test_trim(input_data, result):
    assert utils.trim(input_data) == result


@pytest.mark.xfail()
def test_trim_int():
    assert utils.trim(12345) == "12345"


@pytest.mark.xfail()
def test_trim_none():
    assert utils.trim(None) == None


# test to_list

@pytest.mark.parametrize("input_data, delimeter, result", [
    ("One,Two,Three", ",", ["One", "Two", "Three"]),
    ("1/2/3", "/", ["1", "2", "3"]),
    ("One Two Three", " ", ["One", "Two", "Three"]),

    (" ", " ", []),
    ("1,2,3", None, ["1,2,3"]),
    ("", None, []),
])
def test_to_list(input_data, delimeter, result):
    if delimeter is None:
        res = utils.to_list(input_data)
    res = utils.to_list(input_data, delimeter)

    assert res == result


@pytest.mark.xfail()
def test_to_list_int():
    assert utils.to_list(123) == [123]


@pytest.mark.xfail()
def test_to_list_none():
    assert utils.to_list(None) == []


# test contains

@pytest.mark.parametrize("input_string, symbol, result", [
    ("Test string", "T", True),
    ("тест", "е", True),
    ("12345", "5", True),
    ("M&m's", "&", True),
    ("хорошая погода", " ", True),
    ("Кое-что интересное", "-", True),
    ("", "", True),
    (" ", " ", True),

    ("something", "S", False),
    ("1257", "a", False),
    ("что-то на русском", "На", False),
    ("", " ", False),
])
def test_contains(input_string, symbol, result):
    assert utils.contains(input_string, symbol) == result


@pytest.mark.xfail()
def test_contains_int():
    assert utils.contains(123, 1) == True


@pytest.mark.xfail()
def test_contains_none_symbol():
    assert utils.contains("some text", None) == False


# test delete_symbol

@pytest.mark.parametrize("input_string, symbol, result", [
    ("Test string", "T", "est string"),
    ("тест", "е", "тст"),
    ("1231451", "1", "2345"),
    ("M&m&s", "&", "Mms"),
    ("хо ро шая Пог ода", " ", "хорошаяПогода"),
    ("", "", ""),
    (" ", " ", ""),

    ("something", "S", "something"),
    ("1257", "a", "1257"),
    ("оценка 5", "55", "оценка 5"),
    (" ", " ", ""),
    ("", "f", ""),
])
def test_delete_symbol(input_string, symbol, result):
    assert utils.delete_symbol(input_string, symbol) == result


@pytest.mark.xfail()
def test_delete_symbol_int():
    assert utils.delete_symbol(123, 1) == 123


@pytest.mark.xfail()
def test_delete_symbol_none_symbol():
    assert utils.delete_symbol("some text", None) == "some text"


@pytest.mark.xfail()
def test_delete_symbol_none_string():
    assert utils.delete_symbol(None, "s") == None


# test starts_with

@pytest.mark.parametrize("input_string, symbol, result", [
    ("Test string", "T", True),
    ("тест", "т", True),
    ("12345", "1", True),
    (" Кое-что интересное", " ", True),
    ("", "", True),
    (" ", " ", True),

    ("m&m's", "&", False),
    ("хорошая погода", " ", False),
    ("something", "S", False),
    ("1257", "a", False),
    ("", " ", False),
])
def test_starts_with(input_string, symbol, result):
    assert utils.starts_with(input_string, symbol) == result


@pytest.mark.xfail()
def test_starts_with_int():
    assert utils.starts_with(123, 1) == True


@pytest.mark.xfail()
def test_starts_with_none_symbol():
    assert utils.starts_with("", None) == True


# test ends_with

@pytest.mark.parametrize("input_string, symbol, result", [
    ("Test string", "g", True),
    ("тест", "т", True),
    ("12345", "5", True),
    ("Кое-что интересное ", " ", True),
    ("", "", True),
    (" ", " ", True),

    ("m&m's", "&", False),
    ("хорошая погода", " ", False),
    ("something", "G", False),
    ("1257", "a", False),
    ("", " ", False),
])
def test_end_with(input_string, symbol, result):
    assert utils.end_with(input_string, symbol) == result


@pytest.mark.xfail()
def test_end_with_int():
    assert utils.end_with(123, 3) == True


@pytest.mark.xfail()
def test_end_with_none_symbol():
    assert utils.end_with("", None) == True


# test is_empty

@pytest.mark.parametrize("input_string, result", [
    ("", True),
    (" ", True),
    ("     ", True),

    ("not empty", False),
    ("false", False),
    (" какой-то текст ", False),
    ("1257", False),
])
def test_is_empty(input_string, result):
    assert utils.is_empty(input_string) == result


@pytest.mark.xfail()
def test_is_empty_int():
    assert utils.is_empty(123) == False


@pytest.mark.xfail()
def test_is_empty_none_string():
    assert utils.is_empty(None) == False


# test list_to_string

@pytest.mark.parametrize("input_list, joiner, result", [
    (["One", "Two", "Three"], ", ", "One, Two, Three"),
    (["1", "2", "3"], "/", "1/2/3"),
    (["One", "Two", "Three"], " ", "One Two Three"),
    (["1,2,3"], None, "1,2,3"),
    ([1, 2, 3], ",", "1,2,3"),

    ([], " ", ""),
    ([], None, ""),
])
def test_list_to_string(input_list, joiner, result):
    if joiner is None:
        res = utils.list_to_string(input_list)
    res = utils.list_to_string(input_list, joiner)

    assert res == result


@pytest.mark.xfail()
def test_list_to_string_none():
    assert utils.list_to_string(None, ",") == None
