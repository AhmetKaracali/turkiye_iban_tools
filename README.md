# TURKIYE IBAN Tools

Bu kütüphane, Türkiye'deki IBAN numaraları için IBAN doğrulama, IBAN Numarasından banka adı öğrenme ve IBAN Numarasından Hesap Numarası alma işlevlerini sağlar.

Banka listesi [TCMB Ödeme Sistemleri Katılımcıları Listesi](https://www.tcmb.gov.tr/wps/wcm/connect/a7931555-51dd-4cf4-90ac-862a015f3eb3/TCMB+%C3%96deme+Sistemleri+Kat%C4%B1l%C4%B1mc%C4%B1lar%C4%B1.pdf?MOD=AJPERES)'nden ***05.01.2024*** tarihinde çekilmiş, ve hardcoded olarak TRIBANTools sınıfına eklenmiştir.

IBAN Doğrulaması [10 Ekim 2008 tarihli, 27020 numaralı resmi gazetede belirtilen kurallara](https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Bottom+Menu/IBAN/Communique) göre yapılmaktadır.

Geliştirme ve test kapsamı tüm case'leri içermemektedir. Prod ortamına alınmadan önce dikkatli olunuz.

## Özellikler

- IBAN doğrulama
- IBAN'dan banka bilgisi alma
- IBAN'dan hesap numarası alma

## Kurulum

Bu kütüphaneyi kullanmak için, kodu klonlayabilir veya pip komutu ile paket olarak projenize dahil edebilirsiniz;


```bash
pip install turkiye_iban_tools
```

## Kullanım

```python
from turkiye_iban_tools import TRIBANTools

# Initialize
IBANTool = TRIBANTools()

# IBAN doğrulama
valid = IBANTool.validate('your_iban_number')
print(valid)

# Banka bilgisi alma
bank_info = IBANTool.get_bank_info('your_iban_number')
print(bank_info)

# Hesap numarası alma (Başında 0 ile)
account_number = IBANTool.get_account_number('your_iban_number')
print(account_number)

# Hesap numarası alma (Başında 0 olmadan)
account_number = IBANTool.get_account_number('your_iban_number',True)
print(account_number)
```
## License
Bu proje MIT Lisansı kapsamında lisanslıdır; ayrıntılar için [LICENSE.md](LICENSE.md) dosyasına bakınız.