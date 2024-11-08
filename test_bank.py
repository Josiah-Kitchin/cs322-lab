import pytest
from bank import Account

@pytest.fixture
def test_account():
    return Account("Test")

def test_initial_balance():
    TestAccount = Account("Test")
    assert TestAccount.get_balance() == 0

def test_deposit():
    TestAccount = Account("Test", 0)
    assert TestAccount.deposit(100) == 100

def test_withdraw():
    TestAccount = Account("Test", 100)
    assert TestAccount.withdraw(100) == 0

def test_deposit_negative_amount():
    TestAccount = Account("Test",10)
    with pytest.raises(ValueError):
        TestAccount.deposit(-100)
    
def test_withdraw_more_than_balance():
    TestAccount = Account("Test",100)
    with pytest.raises(ValueError):
        TestAccount.withdraw(500)
    
def test_withdraw_negative_amount():
    TestAccount = Account("Test",100)
    with pytest.raises(ValueError):
        TestAccount.withdraw(-100)
    