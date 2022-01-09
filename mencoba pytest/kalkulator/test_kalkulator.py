# coding with pytest
import pytest
from kalkulator import Kalkulator, str2num


def test_str2num():
    assert True
    assert str2num('123') == int(123)
    assert str2num('1e3E6') == int(1000)
    assert str2num('0.1e1') == float(1)
    assert str2num('seratus 5') is None


def test_instance():
    calc = Kalkulator()
    assert str(calc) == '0'
    calc.calculate('+', 1, 9)
    assert str(calc) == '10'

    calc.calculate('*', '_', '7')
    assert str(calc) == '70'

    with pytest.raises(ZeroDivisionError):
        calc.calculate('/', 1, 0)
