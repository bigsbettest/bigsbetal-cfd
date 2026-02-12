# -*- coding: utf-8 -*-
"""Translate AZ and KY guides. Add See also blocks to DE, PL, AZ, KY."""

# Azerbaijani translations
AZ = {
    "Home": "Əsas səhifə",
    "Registration": "Qeydiyyat",
    "Payments": "Ödənişlər",
    "Bonuses": "Bonuslar",
    "Mobile": "Mobil",
    "Home → Registration": "Əsas səhifə → Qeydiyyat",
    "Home → Payments": "Əsas səhifə → Ödənişlər",
    "Home → Bonuses": "Əsas səhifə → Bonuslar",
    "Home → Mobile play": "Əsas səhifə → Mobil versiya",
    "BigsBet Registration: Complete Guide from A to Z": "BigsBet qeydiyyatı: A-dan Z-yə tam təlimat",
    "Registration: Step-by-step Guide": "Qeydiyyat: addım-addım təlimat",
    "Account, currency, KYC and 2FA": "Hesab, valyuta, KYC və 2FA",
    "Contents": "Mündəricat",
    "4 Registration Methods": "4 qeydiyyat üsulu",
    "Account Currency Selection": "Hesab valyutasının seçimi",
    "KYC Verification": "KYC yoxlaması",
    "2FA: Account Protection": "2FA: hesab mühafizəsi",
    "Password Recovery": "Parol bərpası",
    "Common Mistakes": "Ümumi səhvlər",
    "Method 1: Email": "1-ci üsul: Email",
    "Method 2: Phone": "2-ci üsul: Telefon",
    "Method 3: Social Networks": "3-cü üsul: Sosial şəbəkələr",
    "Method 4: One Click": "4-cü üsul: Bir klik",
    "Start Registration": "Qeydiyyata başlayın",
    "Play responsibly": "Məsuliyyətlə oynayın",
    "Important:": "Vacib:",
    "Tip:": "Məsləhət:",
    "See also:": "Həmçinin bax:",
}

# Kyrgyz translations  
KY = {
    "Home": "Башкы бет",
    "Registration": "Катталуу",
    "Payments": "Төлөмдөр",
    "Bonuses": "Бонусдар",
    "Mobile": "Мобилдик",
    "Home → Registration": "Башкы бет → Катталуу",
    "Home → Payments": "Башкы бет → Төлөмдөр",
    "Home → Bonuses": "Башкы бет → Бонусдар",
    "Home → Mobile play": "Башкы бет → Мобилдик версия",
    "BigsBet Registration: Complete Guide from A to Z": "BigsBet катталуу: А дан З ге чейин толук колдонмо",
    "Registration: Step-by-step Guide": "Катталуу: кадамдын-кадамы менен колдонмо",
    "Account, currency, KYC and 2FA": "Каттоо, валюта, KYC жана 2FA",
    "Contents": "Мазмуну",
    "4 Registration Methods": "4 катталуу ыкмасы",
    "Account Currency Selection": "Каттоо валютасын тандоо",
    "KYC Verification": "KYC текшерүүсү",
    "2FA: Account Protection": "2FA: каттоо коргоосу",
    "Password Recovery": "Сыр сөздү калыбына келтирүү",
    "Common Mistakes": "Кеңири таралган каталар",
    "Method 1: Email": "1-ыкма: Email",
    "Method 2: Phone": "2-ыкма: Телефон",
    "Method 3: Social Networks": "3-ыкма: Социялдык тармактар",
    "Method 4: One Click": "4-ыкма: Бир басуу",
    "Start Registration": "Катталууну баштоо",
    "Play responsibly": "Жоопкерчиликтүү ойноңуз",
    "Important:": "Маанилүү:",
    "Tip:": "Кеңеш:",
    "See also:": "Ошондой эле караңыз:",
}

# DE See also
DE_LINKS = '<p style="margin-top:24px;font-size:14px;color:#8f8ca0">Siehe auch: <a href="registratsiya-guide.html">Registrierung</a> · <a href="platezhi-guide.html">Zahlungen</a> · <a href="bonus-guide.html">Bonusse</a> · <a href="mobile-guide.html">Mobile</a></p>'

# PL See also  
PL_LINKS = '<p style="margin-top:24px;font-size:14px;color:#8f8ca0">Zobacz też: <a href="registratsiya-guide.html">Rejestracja</a> · <a href="platezhi-guide.html">Płatności</a> · <a href="bonus-guide.html">Bonusy</a> · <a href="mobile-guide.html">Mobile</a></p>'

def add_see_also():
    """Add See also blocks to DE, PL, AZ, KY guides."""
    guides = {
        'registratsiya-guide': {
            'de': 'Siehe auch: <a href="platezhi-guide.html">Zahlungen</a> · <a href="bonus-guide.html">Bonusse</a> · <a href="mobile-guide.html">Mobile</a>',
            'pl': 'Zobacz też: <a href="platezhi-guide.html">Płatności</a> · <a href="bonus-guide.html">Bonusy</a> · <a href="mobile-guide.html">Mobile</a>',
            'az': 'Həmçinin bax: <a href="platezhi-guide.html">Ödənişlər</a> · <a href="bonus-guide.html">Bonuslar</a> · <a href="mobile-guide.html">Mobil</a>',
            'ky': 'Ошондой эле караңыз: <a href="platezhi-guide.html">Төлөмдөр</a> · <a href="bonus-guide.html">Бонусдар</a> · <a href="mobile-guide.html">Мобилдик</a>',
        },
        'platezhi-guide': {
            'de': 'Siehe auch: <a href="registratsiya-guide.html">Registrierung</a> · <a href="bonus-guide.html">Bonusse</a> · <a href="mobile-guide.html">Mobile</a>',
            'pl': 'Zobacz też: <a href="registratsiya-guide.html">Rejestracja</a> · <a href="bonus-guide.html">Bonusy</a> · <a href="mobile-guide.html">Mobile</a>',
            'az': 'Həmçinin bax: <a href="registratsiya-guide.html">Qeydiyyat</a> · <a href="bonus-guide.html">Bonuslar</a> · <a href="mobile-guide.html">Mobil</a>',
            'ky': 'Ошондой эле караңыз: <a href="registratsiya-guide.html">Катталуу</a> · <a href="bonus-guide.html">Бонусдар</a> · <a href="mobile-guide.html">Мобилдик</a>',
        },
        'bonus-guide': {
            'de': 'Siehe auch: <a href="registratsiya-guide.html">Registrierung</a> · <a href="platezhi-guide.html">Zahlungen</a> · <a href="mobile-guide.html">Mobile</a>',
            'pl': 'Zobacz też: <a href="registratsiya-guide.html">Rejestracja</a> · <a href="platezhi-guide.html">Płatności</a> · <a href="mobile-guide.html">Mobile</a>',
            'az': 'Həmçinin bax: <a href="registratsiya-guide.html">Qeydiyyat</a> · <a href="platezhi-guide.html">Ödənişlər</a> · <a href="mobile-guide.html">Mobil</a>',
            'ky': 'Ошондой эле караңыз: <a href="registratsiya-guide.html">Катталуу</a> · <a href="platezhi-guide.html">Төлөмдөр</a> · <a href="mobile-guide.html">Мобилдик</a>',
        },
        'mobile-guide': {
            'de': 'Siehe auch: <a href="registratsiya-guide.html">Registrierung</a> · <a href="platezhi-guide.html">Zahlungen</a> · <a href="bonus-guide.html">Bonusse</a>',
            'pl': 'Zobacz też: <a href="registratsiya-guide.html">Rejestracja</a> · <a href="platezhi-guide.html">Płatności</a> · <a href="bonus-guide.html">Bonusy</a>',
            'az': 'Həmçinin bax: <a href="registratsiya-guide.html">Qeydiyyat</a> · <a href="platezhi-guide.html">Ödənişlər</a> · <a href="bonus-guide.html">Bonuslar</a>',
            'ky': 'Ошондой эле караңыз: <a href="registratsiya-guide.html">Катталуу</a> · <a href="platezhi-guide.html">Төлөмдөр</a> · <a href="bonus-guide.html">Бонусдар</a>',
        },
    }
    
    for guide, langs in guides.items():
        for lang, link_block in langs.items():
            path = f'{lang}/{guide}.html'
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    c = f.read()
                if 'Siehe auch' in c or 'Zobacz też' in c or 'Həmçinin bax' in c or 'Ошондой эле караңыз' in c:
                    continue  # Already has block
                # Add before </main>
                insert = f'    <p style="margin-top:24px;font-size:14px;color:#8f8ca0">{link_block}</p>\n  </main>'
                if '</main>' in c and insert not in c:
                    c = c.replace('  </main>', f'\n    <p style="margin-top:24px;font-size:14px;color:#8f8ca0">{link_block}</p>\n  </main>')
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(c)
                    print(f'Added See also to {path}')
            except Exception as e:
                print(f'Error {path}: {e}')

if __name__ == '__main__':
    add_see_also()
    print('See also blocks done')
