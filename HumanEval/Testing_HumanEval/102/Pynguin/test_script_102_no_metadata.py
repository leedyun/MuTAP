# Automatically generated by Pynguin.

import script_102 as module_0



def test_case_0():
    list_0 = []
    float_0 = 966.3564
    tuple_0 = (list_0, list_0, float_0)
    list_1 = [tuple_0]
    var_0 = module_0.choose_num(list_1, list_0)
    assert var_0 == -1
    




def test_case_2():
    int_0 = 2838
    var_0 = module_0.choose_num(int_0, int_0)
    assert var_0 == 2838
    var_1 = module_0.choose_num(int_0, int_0)
    assert var_1 == 2838
    var_2 = module_0.choose_num(int_0, int_0)
    assert var_2 == 2838
   



def test_case_3():
    int_0 = 63
    none_type_0 = None
    var_0 = module_0.choose_num(int_0, int_0)
    assert var_0 == -1
    



def test_case_4():
    bool_0 = False
    var_0 = module_0.choose_num(bool_0, bool_0)
    assert var_0 is False
    var_1 = module_0.choose_num(var_0, bool_0)
    assert var_1 is False
    bool_1 = True
    var_2 = module_0.choose_num(var_0, bool_1)
    assert var_2 == 0
    var_3 = module_0.choose_num(bool_0, var_2)
    assert var_3 == 0
    var_4 = module_0.choose_num(bool_0, var_0)
    assert var_4 is False
    