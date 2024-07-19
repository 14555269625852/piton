import pytest
from string_utils import StringUtils
utils = StringUtils()


@pytest.mark.parametrize('string, result', [
    # POSITIVE
    ("skypro", "Skypro"),
    ("hello sveta", "Hello sveta"),
    ("sveta-123", "Sveta-123"),
    # NEGATIVE
    ("", ""),
    ("Sveta", "Sveta"),
    ("Sveta-123", "Sveta-123"),
])
def test_capitalize(string, result):
    assert utils.capitilize(string) == result


@pytest.mark.parametrize('string, result', [
    # POSITIVE
    (" Sveta", "Sveta"),
    (" hello sveta", "hello sveta"),
    ("  Sveta-123 ", "Sveta-123 "),
    # NEGATIVE
    ("Svet a", "Svet a"),
    ("", ""),
    ("Sveta-123  ",  "Sveta-123  "),
])
def test_trim(string, result):
    assert utils.trim(string) == result


@pytest.mark.parametrize('string, share, result', [
    # POSITIVE
    ("Sveta*1997*year", "*", ["Sveta", "1997", "year"]),
    ("S/v/e/t/a", "/", ["S", "v", "e", "t", "a"]),
    ("111,222,333", ",", ["111", "222", "333"]),
    # NEGATIVE
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
    ])
def test_to_list(string, share, result):
    if share is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, share)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    # POSITIVE
    ("Sveta", "S", True),
    ("Sveta", "a", True),
    ("Sveta1", "1", True),
    # NEGATIVE
    ("Sveta", "1", False),
    ("Sveta", "s", False),
    ("Sveta1", "/", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    # POSITIVE
    ("Sveta1", "1", "Sveta"),
    ("Sveta", "S", "veta"),
    ("Sveta", "v", "Seta"),
    # NEGATIVE
    ("Sveta1", "2", "Sveta1"),
    ("Sveta1", "s", "Sveta1"),
    ("Sveta1", "", "Sveta1"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    # POSITIVE
    ("Sveta1", "S", True),
    ("12345", "1", True),
    (" sveta", "", True),
    # NEGATIVE
    ("Sveta1", "s", False),
    ("12345", "0", False),
    ("Sveta1", "/", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    # POSITIVE
    ("Sveta", "a", True),
    ("12345", "5", True),
    ("Sveta ", "", True),
    # NEGATIVE
    ("Sveta", "S", False),
    ("12345", "6", False),
    ("Sveta1", "/", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result', [
    # POSITIVE
    (" ", True),
    ("  ", True),
    ("   ", True),
    # NEGATIVE
    (" 123", False),
    ("12345", False),
    ("Sveta", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


@pytest.mark.parametrize('lst, connect, result', [
    # POSITIVE
    (["1", "2", "3"], "/", "1/2/3"),
    (["Sveta", "1997", "year"], "-", "Sveta-1997-year"),
    (["Sveta", "1", "2"], "", "Sveta12"),
    # NEGATIVE
    ([], None, ""),
    ([], "*", ""),
    ([], "sveta", ""),
])
def test_list_to_string(lst, connect, result):
    if connect is None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, connect)
    assert res == result
