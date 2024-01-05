class TRIBANTools:
    def __init__(self):
        self.bank_list = {
            '00100': {'name': 'ADABANK A.Ş', 'code': '00100', 'id': 1},
            '00046': {'name': 'AKBANK T.A.Ş', 'code': '00046', 'id': 2},
            '00143': {'name': 'AKTİF YATIRIM BANKASI A.Ş.', 'code': '00143', 'id': 3},
            '00203': {'name': 'ALBARAKA TÜRK KATILIM BANKASI A.Ş.', 'code': '00203', 'id': 4},
            '00124': {'name': 'ALTERNATİFBANK A.Ş.', 'code': '00124', 'id': 5},
            '00135': {'name': 'ANADOLUBANK A.Ş.', 'code': '00135', 'id': 6},
            '00091': {'name': 'ARAP TÜRK BANKASI', 'code': '00091', 'id': 7},
            '00129': {'name': 'BANK OF AMERICA YATIRIM BANK A.Ş', 'code': '00129', 'id': 8},
            '00149': {'name': 'BANK OF CHINA TURKEY A.Ş', 'code': '00149', 'id': 9},
            '00142': {'name': 'BANKPOZİTİF KREDİ VE KALK.BANK.A.Ş.', 'code': '00142', 'id': 10},
            '00029': {'name': 'BİRLEŞİK FON BANKASI A.Ş.', 'code': '00029', 'id': 11},
            '00125': {'name': 'BURGAN BANK A.Ş.', 'code': '00125', 'id': 12},
            '00092': {'name': 'CITIBANK A.Ş.', 'code': '00092', 'id': 13},
            '00151': {'name': 'D YATIRIM BANKASI A.Ş.', 'code': '00151', 'id': 14},
            '00134': {'name': 'DENİZBANK A.Ş.', 'code': '00134', 'id': 15},
            '00152': {'name': 'DESTEK YATIRIM BANKASI A.Ş.', 'code': '00152', 'id': 16},
            '00115': {'name': 'DEUTSCHE BANK A.Ş.', 'code': '00115', 'id': 17},
            '00138': {'name': 'DİLER YATIRIM BANKASI A.Ş.', 'code': '00138', 'id': 18},
            '00103': {'name': 'FİBABANKA A.Ş.', 'code': '00103', 'id': 19},
            '00150': {'name': 'GOLDEN GLOBAL YATIRIM BANKASI A.Ş.', 'code': '00150', 'id': 20},
            '00139': {'name': 'GSD YATIRIM BANKASI A.Ş.', 'code': '00139', 'id': 21},
            '00123': {'name': 'HSBC BANK A.Ş.', 'code': '00123', 'id': 22},
            '00212': {'name': 'HAYAT FİNANS KATILIM BANKASI A.Ş.', 'code': '00212', 'id': 23},
            '00109': {'name': 'ICBC TURKEY BANK A.Ş.', 'code': '00109', 'id': 24},
            '00099': {'name': 'ING BANK A.Ş.', 'code': '00099', 'id': 25},
            '00148': {'name': 'INTESA SANPAOLO S.P.A', 'code': '00148', 'id': 26},
            '00004': {'name': 'İLLER BANKASI A.Ş.', 'code': '00004', 'id': 27},
            '00132': {'name': 'İSTANBUL TAKAS VE SAKLAMA BANK. A.Ş.', 'code': '00132', 'id': 28},
            '00098': {'name': 'JPMORGAN CHASE BANK N.A.', 'code': '00098', 'id': 29},
            '00205': {'name': 'KUVEYT TÜRK KATILIM BANKASI A.Ş.', 'code': '00205', 'id': 30},
            '00806': {'name': 'MERKEZİ KAYIT KURULUŞU A.Ş.', 'code': '00806', 'id': 31},
            '00153': {'name': 'MİSYON YATIRIM BANKASI A.Ş.', 'code': '00153', 'id': 32},
            '00147': {'name': 'MUFG BANK TURKEY A.Ş.', 'code': '00147', 'id': 33},
            '00141': {'name': 'NUROL YATIRIM BANKASI A.Ş.', 'code': '00141', 'id': 34},
            '00146': {'name': 'ODEA BANK A.Ş.', 'code': '00146', 'id': 35},
            '00116': {'name': 'PASHA YATIRIM BANK A.Ş', 'code': '00116', 'id': 36},
            '00807': {'name': 'POSTA VE TELGRAF TEŞKİLATI A.Ş.', 'code': '00807', 'id': 37},
            '00137': {'name': 'RABOBANK A.Ş.', 'code': '00137', 'id': 38},
            '00122': {'name': 'SOCIETE GENERALE (SA', 'code': '00122', 'id': 39},
            '00121': {'name': 'STANDARD CHARTERED YATIRIM BANKASI TÜRK A.Ş.', 'code': '00121', 'id': 40},
            '00059': {'name': 'ŞEKERBANK T.A.Ş.', 'code': '00059', 'id': 41},
            '00032': {'name': 'T. EKONOMİ BANKASI A.Ş', 'code': '00032', 'id': 42},
            '00016': {'name': 'T. EXİMBANK', 'code': '00016', 'id': 43},
            '00062': {'name': 'T. GARANTİ BANKASI A.Ş.', 'code': '00062', 'id': 44},
            '00012': {'name': 'T. HALK BANKASI A.Ş.', 'code': '00012', 'id': 45},
            '00064': {'name': 'T. İŞ BANKASI A.Ş', 'code': '00064', 'id': 46},
            '00017': {'name': 'T. KALKINMA BANKASI A.Ş', 'code': '00017', 'id': 47},
            '00014': {'name': 'T. SINAİ KALKINMA BANKASI A.Ş.', 'code': '00014', 'id': 48},
            '00015': {'name': 'T. VAKIFLAR BANKASI T.A.O', 'code': '00015', 'id': 49},
            '00001': {'name': 'T.C. MERKEZ BANKASI', 'code': '00001', 'id': 50},
            '00010': {'name': 'T.C. ZİRAAT BANKASI A.Ş', 'code': '00010', 'id': 51},
            '00154': {'name': 'TERA YATIRIM BANKASI A.Ş.', 'code': '00154', 'id': 52},
            '00213': {'name': 'T.O.M. KATILIM BANKASI A.Ş.', 'code': '00213', 'id': 53},
            '00096': {'name': 'TURKISH BANK A.Ş.', 'code': '00096', 'id': 54},
            '00108': {'name': 'TURKLAND BANK A.S.', 'code': '00108', 'id': 55},
            '00211': {'name': 'TÜRKİYE EMLAK KATILIM BANKASI A.Ş', 'code': '00211', 'id': 56},
            '00206': {'name': 'TÜRKİYE FİNANS KATILIM BANKASI A.Ş', 'code': '00206', 'id': 57},
            '00210': {'name': 'VAKIF KATILIM BANKASI A.Ş.', 'code': '00210', 'id': 58},
            '00067': {'name': 'YAPI VE KREDİ BANKASI A.Ş.', 'code': '00067', 'id': 59},
            '00209': {'name': 'ZİRAAT KATILIM BANKASI A.Ş.', 'code': '00209', 'id': 60},
            '00155': {'name': 'Q YATIRIM BANKASI A.Ş.', 'code': '00155', 'id': 61},
            '00111': {'name': 'QNB FİNANSBANK A.Ş.', 'code': '00111', 'id': 62}
        }

    def validate(self, iban):
        iban = iban.replace(' ', '')

        # Checking IBAN length and prohibited characters
        if len(iban) != 26 or not iban.isalnum():
            return False

        # Converting IBAN letters to numbers
        iban_rearranged = iban[4:] + iban[:4]
        iban_numeric = ''
        for char in iban_rearranged:
            if char.isdigit():
                iban_numeric += char
            else:
                iban_numeric += str(ord(char.upper()) - 55)

        # Check according to MOD 97-10 algorithm
        return int(iban_numeric) % 97 == 1

    def get_bank_info(self, iban):
        iban = iban.replace(' ', '')
        bank_code = iban[4:9]
        return self.bank_list.get(bank_code, {'name': 'Unknown', 'code': bank_code, 'id': None})

    def get_account_number(self, iban, remove_leading_zeros=False):
        iban = iban.replace(' ', '')
        account_number = iban[10:]
        if remove_leading_zeros:
            # Remove leading zeros from the account number.
            account_number = account_number.lstrip('0')
        return account_number
