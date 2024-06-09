import pytest
from string_utils import StringUtils


@pytest.mark.parametrize('num1, result', [("привет", "Привет"),
                                          ('123', "123"),
                                          ("Добрый день", "Добрый день")])
def test_positive_capitilize(num1, result):#
    stringutils = StringUtils()
    res = stringutils.capitilize(num1)
    assert res == result
    print (res)


@pytest.mark.xfail
@pytest.mark.negative_test_capitilize
@pytest.mark.parametrize('line, result', [("", ""),  # должен падать но проходит тест
                                          # также должен падать но проходит
                                          (" ", " "),
                                          (None, None)
                                          ])
def test_negative_capitilize(line, result):
    stringutils = StringUtils()
    res = stringutils.capitilize(line)
    assert res == result
    print (res)

@pytest.mark.parametrize('num1, result', [(" hello", "hello"),("H ello", "H ello "),("H ello", "H ello")])
def test_Spaces_first(num1, result):#
    test = StringUtils()
    res = test.trim(num1)
    assert res == result

@pytest.mark.parametrize('val, delim, result', [("1,2,3", ",", ['1','2','3']),(" , , ", ",",[' ',' ',' '])])
def test_to_list(val, delim, result):
    test = StringUtils()
    res = test.to_list(val, delim)
    assert res == result


@pytest.mark.parametrize('val, sumbol, result', [("1,2,3", "1", True),(" , , ", " ",True),('ab cdef','g',False)])
def test_contains(val, simbol, result):#ll
    test = StringUtils()
    res = test.containst(val, delim)
    assert res == result

@pytest.mark.parametrize('val, sumbol, result', [("SkyPro", "k", "SyPro"),("SkyPro", "Pro " , "Sky"),(" "," "," ")])
def test_delete_symbol(val, simbol, result):#
    test = StringUtils()
    res = test.delete_symbol(val, simbol)
    assert res == result
   
@pytest.mark.parametrize('val, sumbol, result', [("SkyPro", "S", True),("SkyPro", "Pro",False),("",'',True)])
def test_starts_with(val, simbol, result):#
    test = StringUtils()
    res = test.starts_with(val, sumbol)
    assert res == result
    

@pytest.mark.parametrize('val, sumbol, result', [("SkyPro", "o", True),("23456", "5 ",False),("","",True)])
def test_end_with(val, simbol, result):#
    test = StringUtils()
    res = test.end_with(val, sumbol)
    assert res == result

@pytest.mark.parametrize('val , result', [("1,2,3,1,2,3",  False),("      ",False ),("", True)])
def test_is_empty(val,  result): #  
    test = StringUtils()
    res = test.is_empty(val)
    assert res == result
 

@pytest.mark.parametrize('val, delim, result', [([1,2,3,1,2,3], "*",'1*2*3*1*2*3'),([1,2,3] , " ","123"),([], '*', "")])
def list_to_string(val, delim, result):#
    test = StringUtils() 
    res = list_to_string(val, delim)
    assert res == result