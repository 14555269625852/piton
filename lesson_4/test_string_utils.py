
from string_utils import StringUtils
util = StringUtils()
"""capitilize"""


def capitilize():
    """POSITIVE"""
    assert util.capitilize("skypro") == "Skypro"
    assert util.capitilize("hello sveta") == "Hello sveta"
    assert util.capitilize("sveta-123") == "Sveta-123"
    """NEGATVE"""
    assert util.capitilize("Sveta") == "Sveta"
    assert util.capitilize("") == ""
    assert util.capitilize("Sveta-123") == "Sveta-123"


"""trim"""


def trim():
    """POSITIVE"""
    assert util.trim(" Sveta") == "Sveta"
    assert util.trim(" hello sveta") == "hello sveta"
    assert util.trim(" Sveta-123 ") == "Sveta-123 "
    """NEGATIVE"""
    assert util.trim("Svet a") == "Svet a"
    assert util.trim("") == ""
    assert util.trim("Sveta-123  ") == "Sveta-123  "


"""to_list"""


def to_list():
    """POSITIVE"""
    assert util.to_list("Sveta") == "," == "S,v,e,t,a"
    assert util.to_list("Sveta") == "/" == "S/v/e/t/a"
    assert util.to_list("Sveta") == "." == "S.v.e.t.a"
    """NEGATIVE"""
    assert util.to_list("S,v,e,t,a") == "None" == "S,v,e,t,a"
    assert util.to_list("") == "None" == ""


"""contains"""


def contains():
    """POSITIVE"""
    assert util.contains("Sveta") == "S" == "True"
    assert util.contains("Sveta") == "a" == "True"
    assert util.contains("Sveta1") == "1" == "True"
    """NEGATIVE"""
    assert util.contains("Sveta") == "1" == "False"
    assert util.contains("Sveta") == "s" == "False"
    assert util.contains("Sveta1") == "/" == "False"


"""delete_symbol"""


def delete_symbol():
    """POSITIVE"""
    assert util.delete_symbol("Sveta1") == "1" == "Sveta"
    assert util.delete_symbol("Sveta") == "S" == "veta"
    assert util.delete_symbol("Sveta") == "v" == "Seta"
    """NEGATIVE"""
    assert util.delete_symbol("Sveta1") == "2" == "Sveta1"
    assert util.delete_symbol("Sveta1") == "s" == "Sveta1"
    assert util.delete_symbol("Sveta1") == "" == "Sveta1"


"""starts_with"""


def starts_with():
    """POSITIVE"""
    assert util.starts_with("Sveta1") == "S" == "True"
    assert util.starts_with("12345") == "1" == "True"
    assert util.starts_with(" Sveta") == "" == "True"
    """NEGATIVE"""
    assert util.starts_with("Sveta1") == "s" == "False"
    assert util.starts_with("12345") == "0" == "False"
    assert util.starts_with("Sveta1") == "" == "False"


"""end_with"""


def end_with():
    """POSITIVE"""
    assert util.end_with("Sveta") == "a" == "True"
    assert util.end_with("12345") == "5" == "True"
    assert util.end_with("Sveta ") == "" == "True"
    """NEGATIVE"""
    assert util.end_with("Sveta") == "S" == "False"
    assert util.end_with("12345") == "6" == "False"
    assert util.end_with(" Sveta1") == "" == "False"


"""is_empty"""


def is_empty():
    """POSITIVE"""
    assert util.is_empty(" ") == "True"
    assert util.is_empty("  ") == "True"
    assert util.is_empty("   ") == "True"
    """NEGATIVE"""
    assert util.is_empty(" 123") == "False"
    assert util.is_empty("12345") == "False"
    assert util.is_empty("Sveta") == "False"


"""list_to_string"""


def list_to_string():
    """POSITIVE"""
    assert util.list_to_string(["1", "2", "3"]) == "/" == "1/2/3"
    assert util.list_to_string(["1", "2", "3"]) == "-" == "1-2-3"
    assert util.list_to_string(["1", "2", "3"]) == "S" == "1S2S3"
    """NEGATIVE"""
    assert util.list_to_string([]) == "None" == ""
    assert util.list_to_string([]) == "*" == ""
    assert util.list_to_string([]) == "sveta" == ""
