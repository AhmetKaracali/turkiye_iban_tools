# TURKIYE IBAN Tools

This library provides functions for IBAN validation, retrieving bank information from IBAN numbers, and extracting account numbers from IBANs in Turkey.

The bank list is taken from the [TCMB Payment Systems Participants List](https://www.tcmb.gov.tr/wps/wcm/connect/a7931555-51dd-4cf4-90ac-862a015f3eb3/TCMB+%C3%96deme+Sistemleri+Kat%C4%B1l%C4%B1mc%C4%B1lar%C4%B1.pdf?MOD=AJPERES) as of ***January 5, 2024***, and is hardcoded into the TRIBANTools class.

IBAN validation is conducted according to the rules specified in the [Official Gazette dated October 10, 2008, number 27020](https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Bottom+Menu/IBAN/Communique).

Development and testing do not cover all cases. Please be cautious before deploying to a production environment.

## Features

- IBAN validation
- Retrieving bank information from IBAN
- Extracting account number from IBAN

## Installation

To use this library, you can clone the code or include it in your project as a package via pip command:

```bash
pip install turkiye_iban_tools
```

## Usage

```python
from turkiye_iban_tools import TRIBANTools

# Initialize
IBANTool = TRIBANTools()

# IBAN validation
valid = IBANTool.validate('your_iban_number')
print(valid)

# Retrieving bank information
bank_info = IBANTool.get_bank_info('your_iban_number')
print(bank_info)

# Extracting account number (with leading zeros)
account_number = IBANTool.get_account_number('your_iban_number')
print(account_number)

# Extracting account number (without leading zeros)
account_number = IBANTool.get_account_number('your_iban_number', True)
print(account_number)
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
