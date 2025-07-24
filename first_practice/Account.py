import hashlib
import os
import AuthenticationError, ValidationError


class Account:
    """"A simple bank account class with a protected password"""

    def __init__(self, name: str, balance: float, password: str):
        self._salt = os.urandom(16)
        self._name = name
        self._balance = balance
        self._password_hash = self._password_hash(password)

    def _password_hash(self, password: str) -> str:
        """Returns a secure password hash using PBKDF2 with SHA-256"""
        return hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=password.encode(),
            salt=self._salt,
            iterations=100_000,
        ).hex()

    def _verify_password(self, password: str) -> str:
        """"Verifies the provided password against the stored hash"""
        test_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            self._salt,
            100_000,
        ).hex()
        return test_hash == self._password_hash(password)


    def withdraw(self, amount: float, password: str) -> float | None:
        if password != self._password_hash:
            print("Invalid Password")
            return None

        if amount > self._balance:
            print("Insufficient fund")
            return None

        if amount < 0:
            print("Invalid Amount")
            return None

        self._balance -= amount
        print(f" withdrawal successful. New balance{self._balance}")
        return self._balance

    def deposit(self, name: str, amount: float) -> float | None:
        if name != self._name:
            print("Wrong Account")
            return None

        if amount < 0:
            print("Invalid amount")
            return None

        self._balance += amount
        print(f"Deposit successful. New balance{self._balance}")
        return self._balance

    def get_balance(self, password: str) -> float | None:
        if password != self._password_hash:
            print("Invalid Password")
            return None
        return self._balance

    def change_password(self, old_password: str, new_password: str) -> bool:
        """"Changes the password of the account after verifying the old password"""
        if not self._verify_password(old_password):
            raise AuthenticationError

        self._salt = os.urandom(16)
        self._password_hash = self._password_hash(new_password)
