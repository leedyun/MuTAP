# Automatically generated by Pynguin.
import script_85 as module_0


def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    var_0 = module_0.add(set_0)



def test_case_1():
    bytes_0 = b"Pf\x7f\xee\x9d\xef\xfd(O\x08v\x89\xe2d\x92\xb5\xd9\xaf>\xd3"
    var_0 = module_0.add(bytes_0)
    assert var_0 == 488
    