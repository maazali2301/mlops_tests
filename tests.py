import unittest
from wallet import Wallet

class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet()

    def test_initial_balance(self):
        self.assertEqual(self.wallet.check_balance(), 0)

    def test_add_cash(self):
        self.wallet.add_cash(100)
        self.assertEqual(self.wallet.check_balance(), 100)

    def test_withdraw(self):
        self.wallet.add_cash(100)
        self.wallet.withdraw(50)
        self.assertEqual(self.wallet.check_balance(), 50)

    def test_withdraw_insufficient_funds(self):
        self.wallet.add_cash(50)
        with self.assertRaises(ValueError):
            self.wallet.withdraw(100)

if __name__ == '__main__':
    unittest.main()
