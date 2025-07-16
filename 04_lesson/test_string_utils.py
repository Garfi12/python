import pytest
from string_utils import StringUtils


@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, res_in', [
        ("hello", "Hello"),
        ("гонка", "Гонка"),
        ("cake1", "Cake1")
        ])
def test_positive_capitilize(string_in, res_in):
    string = StringUtils()
    res = string.capitilize(string_in)
    assert res == res_in
 

@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('string_in, res_in', [
    ("Next", "Next"),
    (" ", " ") 
    ])
def test_negative_capitilize(string_in, res_in):
    string = StringUtils()
    res = string.capitilize(string_in)
    assert res == res_in


@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, res_in', [
       (" sky", "sky"),
       ("  cat", "cat"),
       ("   ocean", "ocean"),
       (" небо", "небо"),
       (" fly1", "fly1")
       ])
def test_positive_trim(string_in, res_in):
    string = StringUtils()
    res = string.trim(string_in)
    assert res == res_in


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('string_in, res_in', [
    ("sky","sky"),
    ("", ""),
    ("blue sky", "bluesky")
    ])
def test_negative_trim(string_in, res_in):
    string = StringUtils()
    res = string.trim(string_in)
    assert res == res_in


@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
      ("Cats", "C", True),
      ("Cats", "Z", False),
      ("Машина", "М", True),
      ("Солнце", "Т", False),
      ("Blue1", "B", True),
      ("Blue2", "Y", False),
      ("Blue1", "1", True),
      ("Blue1", "u", True)
      ])
def test_positive_contains(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.contains(string_in,symbol_in)
    assert res == res_in


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
      (" ", "C", False),
      ("", "Z", False)
       ])
def test_negative_contains(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.contains(string_in, symbol_in)
    assert res == res_in


@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
    ("FullHouse", "Full", "House"),
    ("Bees", "s", "Bee"),
    ("Door1", "1", "Door"),
    ("Peace!", "!", "Peace"),
    ("Снегопад", "опад", "Снег"),
    ("Луч1", "1", "Луч"),
    ("Ура!", "!", "Ура"),
    ("12345", "23", "145")
    ])
def test_positive_delete_symbol(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.delete_symbol(string_in, symbol_in)
    assert res == res_in


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
    ("FullHouse", "", "FullHouse"),
    ("", "s", ""),
    ("Tree", "s", "Tree")
    ])
def test_negative_delete_symbol(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.delete_symbol(string_in, symbol_in)
    assert res == res_in


@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, res_in', [
    ("a,b,c,d",["a","b","c","d"]),
    ("а,б,в,г",["а","б","в","г"]),
    ("1,2,3,4,5",["1","2","3","4","5"])
    ])
def test_positive_to_list(string_in, res_in):
    string = StringUtils()
    res = string.to_list(string_in)
    assert res == res_in


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('string_in, res_in', [
    ("",[""])
    ])
def test_negative_to_list(string_in, res_in):
    string = StringUtils()
    res = string.to_list(string_in)
    assert res == res_in


@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
    ("Sky", "S", True),
    ("Лето", "Л", True),
    ("1234", "1", True)
    ])
def test_positive_starts_with(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.starts_with(string_in, symbol_in)
    assert res == res_in


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
      (" Sky", "S", True),
      ("", "s", False),
      ("Slow", "", False)
      ])
def test_negative_starts_with(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.starts_with(string_in, symbol_in)
    assert res == res_in


@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
    ("Sky", "y", True),
    ("Лето", "о", True),
    ("1234", "4", True)
    ])
def test_positive_end_with(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.end_with(string_in, symbol_in)
    assert res == res_in


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('string_in, symbol_in, res_in', [
      (" Sky", "S", False),
      ("", "s", False),
      ("Slow", "", False)
      ])
def test_negative_end_with(string_in, symbol_in, res_in):
    string = StringUtils()
    res = string.end_with(string_in, symbol_in)
    assert res == res_in


@pytest.mark.positive_test
@pytest.mark.parametrize('string_in, res_in', [
    ("", True),
    (" ", True),
    ("Hello", False)
    ])
def test_positive_is_empty(string_in, res_in):
    string = StringUtils()
    res = string.is_empty(string_in)
    assert res == res_in

 
@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('string_in, res_in', [
    ("", True),
    (" ", True),
    ("Hello", False),
    ("123", False)
    ])
def test_negative_is_empty(string_in, res_in):
    string = StringUtils()
    res = string.is_empty(string_in)
    assert res == res_in


@pytest.mark.positive_test
@pytest.mark.parametrize('lst, res_in', [
    ([1,2,3,4],"1, 2, 3, 4"),
    (["Sky","Pro"],"Sky, Pro"),
    (["Небо","вокруг"],"Небо, вокруг")
    ])
def test_positive_list_to_string(lst, res_in):
    string = StringUtils()
    res = string.list_to_string(lst)
    assert res == res_in


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('lst, res_in', [
    ([ ]," "),
    ([" "," "]," , ")
    ])
def test_negative_list_to_string(lst, res_in):
    string = StringUtils()
    res = string.list_to_string(lst)
    assert res == res_in