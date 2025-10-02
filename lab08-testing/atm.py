class ATM:
    def __init__(self, pin="1234", balance=1000):
        self._pin = pin
        self._balance = balance

    def verify_pin(self, input_pin: str) -> bool:
        return input_pin == self._pin

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            return False
        if amount > self._balance:
            return False
        self._balance -= amount
        return True

    @property
    def balance(self):
        return self._balance
