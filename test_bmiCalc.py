import bmiCalc as BMI

def test_Normal_bmiCalc_function ():
    expected = 0
    result = BMI.bmiCalc(height=1.85, weight=65)
    assert (result == expected)


def test_Over_bmiCalc_function ():
    expected = 1
    result = BMI.bmiCalc(height=1.85, weight=150)
    assert (result == expected)


def test_under_bmiCalc_function ():
    expected = -1
    result = BMI.bmiCalc(height=1.85, weight=30)
    assert (result == expected)

