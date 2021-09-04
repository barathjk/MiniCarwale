"""
Test Cases for MiniCarWale
"""
from emicalc import emi_calculator

def test_altroz():
    """
    test case
    """
    principal = 650000
    rate = 8.5
    time = 5
    assert emi_calculator(principal, rate, time) == 13335.75
    assert emi_calculator(100000, 0, 4) is None
    assert emi_calculator(-0.45, -9, -7.5) is None

def test_harrier():
    """
    test case
    """
    assert emi_calculator(100000, 0, 4) is None
    assert emi_calculator(800000, 9.25, 5) == 16703.92
    assert emi_calculator(0.000000, 9.0000, -7895632) is None

def test_nexon():
    """
    test case
    """
    assert emi_calculator(0, 0, 0) is None
    assert emi_calculator(-0.23568945, "unknown", -7.5) is None #passing string as a parameter
    assert emi_calculator(800000, 9.25, 5) == 16703.92

def test_swift():
    """
    test case
    """
    assert emi_calculator(500000, 12.5, 3) == 16726.81
    assert emi_calculator(225356, -2, 4) is None
    assert emi_calculator(-0.8956, -9, -7.5) is None

def test_vitara():
    """
    test case
    """
    assert emi_calculator(100000, 0, 4) is None
    assert emi_calculator(750000, 10.25, 5) == 16027.7
    assert emi_calculator(-0.2365, -9, -7.5) is None

def test_ciaz():
    """
    test case
    """
    assert emi_calculator(600000, 6.5, 2) == 26727.75
    assert emi_calculator(100000, 0, 4) is None
    assert emi_calculator(-0.1245, -9, -7.5) is None

def test_jazz():
    """
    test case
    """
    assert emi_calculator(425000, 8.5, 5) == 8719.53
    assert emi_calculator(-5623, 0, 4) is None
    assert emi_calculator(-0.0235689, -9, -7.5) is None

def test_city():
    """
    test case
    """
    assert emi_calculator(800000, 9.25, 5) == 16703.92
    assert emi_calculator(1, 0, 4) is None
    assert emi_calculator(-0.45, -9, -7.5) is None

def test_wrv():
    """
    test case
    """
    assert emi_calculator(200000, 6.75, 4) == 4766.09
    assert emi_calculator(23, 0, 4) is None
    assert emi_calculator(-0.45, -9, -7.5) is None

def test_skoda():
    """
    test case
    """
    assert emi_calculator(550000, 11.01, 5) == 11961.08
    assert emi_calculator(0.23564, 0, -4) is None
    assert emi_calculator(-0.45, -9, -7.5) is None

def test_superb():
    """
    test case
    """
    assert emi_calculator(800000, 9.25, 5) == 16703.92
    assert emi_calculator(-0.9568, 0, 9) is None
    assert emi_calculator(-0.45, -9, -7.5) is None

def test_octavia():
    """
    test case
    """
    assert emi_calculator(3000000, 9.25, 5) == 62639.69
    assert emi_calculator(-0.2565, 0, 2) is None
    assert emi_calculator(-0.45, -9, -7.5) is None
