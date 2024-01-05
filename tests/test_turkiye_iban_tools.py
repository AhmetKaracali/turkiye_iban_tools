import unittest
from src.turkiye_iban_tools import TRIBANTools


class TestIBANTools(unittest.TestCase):

    def test_validate_valid_iban(self):
        valid_iban = "TR980006701000000048599796"  # This is an example IBAN of mine
        IBANTool = TRIBANTools()
        self.assertTrue(IBANTool.validate(valid_iban))

    def test_validate_invalid_iban(self):
        invalid_iban = "TR33000610051978645784132X"  # This is an example invalid IBAN
        IBANTool = TRIBANTools()
        self.assertFalse(IBANTool.validate(invalid_iban))

    def test_validate_valid_iban_with_empty_space(self):
        valid_iban = "TR98 0006 7010 0000 0048 5997 96"  # This is an example IBAN of mine with empty space
        IBANTool = TRIBANTools()
        self.assertTrue(IBANTool.validate(valid_iban))

    def test_validate_invalid_iban_with_empty_space(self):
        invalid_iban = "TR33 0006 1005 1978 6457 8413 2X"  # This is an example invalid IBAN with empty space
        IBANTool = TRIBANTools()
        self.assertFalse(IBANTool.validate(invalid_iban))

    def test_get_bank_info(self):
        iban = "TR980006701000000048599796"
        IBANTool = TRIBANTools()
        bank_info = IBANTool.get_bank_info(iban)
        self.assertEqual(bank_info['name'], 'YAPI VE KREDİ BANKASI A.Ş.')  # Example bank name

    def test_get_account_number_with_leading_zeros(self):
        iban = "TR980006701000000048599796"
        IBANTool = TRIBANTools()
        account_number = IBANTool.get_account_number(iban)
        self.assertEqual(account_number, "1000000048599796")  # Example account number with leading zeros

    def test_get_account_number_without_leading_zeros(self):
        iban = "TR090010300000000041954799"
        IBANTool = TRIBANTools()
        account_number = IBANTool.get_account_number(iban, True)
        self.assertEqual(account_number, "41954799")  # Example account number without leading zeros


if __name__ == '__main__':
    unittest.main()
