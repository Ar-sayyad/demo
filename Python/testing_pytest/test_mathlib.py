import mathlib
import pytest

# import sys
@pytest.mark.parametrize("test_input , expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100)
                         ])
def test_cal_total(test_input, expected_output):
    result = mathlib.cal_square(test_input)
    assert result == expected_output

# @pytest.mark.skipif(sys.version_info < (3,5), reason = "I dont want to run this test Now")
# def test_cal_total():
#     total = mathlib.cal_total(4,5)
#     assert total == 9
#
# def test_calc_multiply():
#     result = mathlib.cal_multiply(10,3)
#     assert result == 30

# @pytest.mark.windows
# def test_window_1():
#     assert True
#
# @pytest.mark.windows
# def test_window_2():
#     assert True
#
# @pytest.mark.mac
# def test_mac_1():
#     assert True
#
# @pytest.mark.mac
# def test_mac_2():
#     assert True