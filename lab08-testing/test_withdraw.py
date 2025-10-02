import pytest
from atm import ATM

@pytest.fixture
def atm():
    return ATM(pin="1234", balance=500)

def test_verify_pin_correct(atm):
    assert atm.verify_pin("1234") is True

def test_verify_pin_incorrect(atm):
    assert atm.verify_pin("0000") is False

def test_withdraw_success(atm):
    assert atm.withdraw(200) is True
    assert atm.balance == 300

def test_withdraw_insufficient_funds(atm):
    assert atm.withdraw(1000) is False
    assert atm.balance == 500

def test_withdraw_invalid_amount(atm):
    assert atm.withdraw(-50) is False
    assert atm.withdraw(0) is False
