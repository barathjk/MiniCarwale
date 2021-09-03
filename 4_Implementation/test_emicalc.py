"""
Test Cases for MiniCarWale
"""
from emicalc import emi_calculator

def test_altroz():
    principal = 650000
    rate = 8.5
    t = 5
    assert 13335.75 == emi_calculator(principal, rate, t)
    assert emi_calculator(100000, 0, 4)
    assert emi_calculator(-0.45, -9, -7.5)

def test_harrier():
    assert emi_calculator(100000, 0, 4) == None
    assert 16703.92 == emi_calculator(800000, 9.25, 5)
    assert emi_calculator(0.000000, 9.0000, -7895632) == None

def test_nexon():
    assert emi_calculator(0, 0, 0) == None
    assert emi_calculator(-0.23568945, "unknown", -7.5) == None #passing string as a parameter
    assert 16703.92 == emi_calculator(800000, 9.25, 5)

def test_swift():
    assert 16726.81 == emi_calculator(500000, 12.5, 3)
    assert emi_calculator(225356, -2, 4) == None
    assert emi_calculator(-0.8956, -9, -7.5) == None

def test_vitara():
    assert emi_calculator(100000, 0, 4) == None
    assert 16027.7 == emi_calculator(750000, 10.25, 5)
    assert emi_calculator(-0.2365, -9, -7.5) == None

def test_ciaz():
    assert 26727.75 == emi_calculator(600000, 6.5, 2)
    assert emi_calculator(100000, 0, 4) == None
    assert emi_calculator(-0.1245, -9, -7.5) == None

def test_jazz():
    assert 8719.53 == emi_calculator(425000, 8.5, 5)
    assert emi_calculator(-5623, 0, 4) == None
    assert emi_calculator(-0.0235689, -9, -7.5) == None

def test_city():
    assert 16703.92 == emi_calculator(800000, 9.25, 5)
    assert emi_calculator(1, 0, 4) == None
    assert emi_calculator(-0.45, -9, -7.5) == None

def test_wrv():
    assert 4766.09 == emi_calculator(200000, 6.75, 4)
    assert emi_calculator(23, 0, 4) == None
    assert emi_calculator(-0.45, -9, -7.5) == None

def test_skoda():
    assert 11961.08 == emi_calculator(550000, 11.01, 5)
    assert emi_calculator(0.23564, 0, -4) == None
    assert emi_calculator(-0.45, -9, -7.5) == None

def test_superb():
    assert 16703.92 == emi_calculator(800000, 9.25, 5)
    assert emi_calculator(-0.9568, 0, 9) == None
    assert emi_calculator(-0.45, -9, -7.5) == None

def test_octavia():
    assert 62639.69 == emi_calculator(3000000, 9.25, 5)
    assert emi_calculator(-0.2565, 0, 2) == None
    assert emi_calculator(-0.45, -9, -7.5) == None

