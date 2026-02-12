# -*- coding: utf-8 -*-
"""Apply AZ and KY translations to guide pages."""
import os

# Azerbaijani - apply to az/*.html
AZ_REPLACEMENTS = [
    # Nav
    ('<a href="index.html" style="color:#8f8ca0">Home</a>', '<a href="index.html" style="color:#8f8ca0">Əsas səhifə</a>'),
    ('<a href="registratsiya-guide.html" style="color:#F9820F">Registration</a>', '<a href="registratsiya-guide.html" style="color:#F9820F">Qeydiyyat</a>'),
    ('<a href="platezhi-guide.html" style="color:#F9820F">Payments</a>', '<a href="platezhi-guide.html" style="color:#F9820F">Ödənişlər</a>'),
    ('<a href="bonus-guide.html" style="color:#F9820F">Bonuses</a>', '<a href="bonus-guide.html" style="color:#F9820F">Bonuslar</a>'),
    ('<a href="mobile-guide.html" style="color:#F9820F">Mobile</a>', '<a href="mobile-guide.html" style="color:#F9820F">Mobil</a>'),
    ('<a href="registratsiya-guide.html" style="color:#8f8ca0">Registration</a>', '<a href="registratsiya-guide.html" style="color:#8f8ca0">Qeydiyyat</a>'),
    ('<a href="platezhi-guide.html" style="color:#8f8ca0">Payments</a>', '<a href="platezhi-guide.html" style="color:#8f8ca0">Ödənişlər</a>'),
    ('<a href="bonus-guide.html" style="color:#8f8ca0">Bonuses</a>', '<a href="bonus-guide.html" style="color:#8f8ca0">Bonuslar</a>'),
    ('<a href="mobile-guide.html" style="color:#8f8ca0">Mobile</a>', '<a href="mobile-guide.html" style="color:#8f8ca0">Mobil</a>'),
    # Crumbs
    ('<div class="crumbs">Home → Registration</div>', '<div class="crumbs">Əsas səhifə → Qeydiyyat</div>'),
    ('<div class="crumbs">Home → Payments</div>', '<div class="crumbs">Əsas səhifə → Ödənişlər</div>'),
    ('<div class="crumbs">Home → Bonuses</div>', '<div class="crumbs">Əsas səhifə → Bonuslar</div>'),
    ('<div class="crumbs">Home → Mobile play</div>', '<div class="crumbs">Əsas səhifə → Mobil versiya</div>'),
    # Footer
    ('18+ | Play responsibly', '18+ | Məsuliyyətlə oynayın'),
    # Registratsiya
    ('BigsBet Registration: Complete Guide from A to Z', 'BigsBet qeydiyyatı: A-dan Z-yə tam təlimat'),
    ('Registration: Step-by-step Guide', 'Qeydiyyat: addım-addım təlimat'),
    ('Account, currency, KYC and 2FA', 'Hesab, valyuta, KYC və 2FA'),
    ('Contents', 'Mündəricat'),
    ('4 Registration Methods', '4 qeydiyyat üsulu'),
    ('Account Currency Selection', 'Hesab valyutasının seçimi'),
    ('KYC Verification', 'KYC yoxlaması'),
    ('2FA: Account Protection', '2FA: hesab mühafizəsi'),
    ('Password Recovery', 'Parol bərpası'),
    ('Common Mistakes', 'Ümumi səhvlər'),
    ('Method 1: Email', '1-ci üsul: Email'),
    ('Method 2: Phone', '2-ci üsul: Telefon'),
    ('Method 3: Social Networks', '3-cü üsul: Sosial şəbəkələr'),
    ('Method 4: One Click', '4-cü üsul: Bir klik'),
    ('Start Registration', 'Qeydiyyata başlayın'),
    # Platezhi
    ('BigsBet Deposits and Withdrawals: Complete Financial Guide', 'BigsBet depozit və çəkimlər: tam maliyyə təlimatı'),
    ('Payments: Deposit and Withdrawal', 'Ödənişlər: depozit və çəkim'),
    ('cards and crypto', 'kartlar və kripto'),
    ('Methods Summary Table', 'Üsullar cədvəli'),
    ('Limits and Fees', 'Limitlər və ödənişlər'),
    ('What to Do If Payment Fails', 'Ödəniş uğursuz olsa nə etməli'),
    ('Method', 'Üsul'),
    ('Min. deposit', 'Min. depozit'),
    ('Withdrawal', 'Çəkim'),
    ('Fee', 'Ödəniş'),
    ('usually 0%', 'adətən 0%'),
    ('up to 24 h', '24 saata qədər'),
    ('Go to Deposit', 'Depozitə keçin'),
    # Bonus
    ('BigsBet Bonuses: Complete Guide and Calculations', 'BigsBet bonusları: tam təlimat və hesablamalar'),
    ('Bonuses: Terms and Benefits', 'Bonuslar: şərtlər və üstünlüklər'),
    ('Welcome, free spins, cashback and VIP', 'Xoş gəldiniz, pulsuz fırlanmalar, keşbek və VIP'),
    ('Welcome Bonus', 'Xoş gəldiniz bonusu'),
    ('Wagering Calculation', 'Veycer hesablaması'),
    ('Free Spins', 'Pulsuz fırlanmalar'),
    ('Cashback', 'Keşbek'),
    ('VIP Programme', 'VIP proqramı'),
    ('Should You Take a Bonus?', 'Bonus götürməli misiniz?'),
    ('Activate Bonus', 'Bonusu aktivləşdirin'),
    # Mobile
    ('BigsBet Mobile Version: Complete Guide', 'BigsBet mobil versiyası: tam təlimat'),
    ('Mobile Version', 'Mobil versiya'),
    ('iOS / Android, speed and security', 'iOS / Android, sürət və təhlükəsizlik'),
    ('Open Mobile Version', 'Mobil versiyanı açın'),
    # Body paragraphs - registratsiya
    ('This guide explains registration in detail: four ways to create an account, currency selection, KYC verification, enabling 2FA and password recovery. Written for beginners from CIS, including users from Tashkent, Samarkand, Bishkek and Baku. Example currency — €, but you can choose another at registration.', 'Bu təlimat qeydiyyatı ətraflı izah edir: hesab yaratmağın dörd üsulu, valyuta seçimi, KYC yoxlaması, 2FA aktivləşdirmə və parol bərpası. ADT-dən yeni başlayanlar üçün, o cümlədən Bakı, Tbilisi və İrəvandan istifadəçilər üçün. Misal valyuta — ₼, qeydiyyatda başqa seçə bilərsiniz.'),
    ('BigsBet typically offers several sign-up options: via email, phone, social networks and a simplified "one-click" option. Choose the one that best fits future account recovery.', 'BigsBet adətən bir neçə qeydiyyat variantı təklif edir: e-poçt, telefon, sosial şəbəkələr və sadələşdirilmiş "bir klik" variantı. Gələcək hesab bərpası üçün ən uyğun olanı seçin.'),
    ('<li>Open the site and click "Register".</li>', '<li>Saytı açın və "Qeydiyyat"a klikləyin.</li>'),
    ('<li>Enter your email and create a strong password.</li>', '<li>E-poçtunuzu daxil edin və güclü parol yaradın.</li>'),
    ('<li>Confirm your email via the link.</li>', '<li>E-poçtu link vasitəsilə təsdiqləyin.</li>'),
    ('<li>Complete your profile: name, date of birth, address.</li>', '<li>Profilinizi doldurun: ad, doğum tarixi, ünvan.</li>'),
    ('<div class="note">Important: use a real email. It receives bonus confirmations and withdrawal notifications.</div>', '<div class="note">Vacib: real e-poçt istifadə edin. Bonus təsdiqləri və çəkim bildirişləri ora gəlir.</div>'),
    ('<li>Select phone registration.</li>', '<li>Telefon qeydiyyatını seçin.</li>'),
    ('<li>Enter your number and wait for the SMS code.</li>', '<li>Nömrənizi daxil edin və SMS kodunu gözləyin.</li>'),
    ('<li>Create a password and confirm sign-in.</li>', '<li>Parol yaradın və daxil olmanı təsdiqləyin.</li>'),
    ('<div class="tip">Tip: keep your phone number in your profile — it speeds up account recovery.</div>', '<div class="tip">Məsləhət: telefon nömrənizi profilə əlavə edin — hesab bərpasını sürətləndirir.</div>'),
    ('Registration via social networks is sometimes available. It is faster but ties your account to an external service. Good for users who change devices often and want 1–2 click sign-in.', 'Sosial şəbəkələr vasitəsilə qeydiyyat bəzən mövcuddur. Daha sürətlidir, amma hesabı xarici xidmətə bağlayır. Tez-tez cihaz dəyişən və 1–2 kliklə daxil olmaq istəyənlər üçün uyğundur.'),
    ('Simplified registration usually requires minimal data. The downside: you will still need to complete your profile for withdrawals later.', 'Sadələşdirilmiş qeydiyyat adətən minimum məlumat tələb edir. Mənfi cəhəti: sonradan çəkimlər üçün profili tamamlamalı olacaqsınız.'),
    ('Currency choice affects fees, limits and payment convenience. If you use Uzcard, Payme or Click, choose local currency or € to avoid conversion. If planning crypto — consider USDT or BTC, but be aware of network fees.', 'Valyuta seçimi ödənişlərə, limitlərə və rahatlığa təsir edir. Uzcard, Payme və ya Click istifadə edirsinizsə, çevirmədən yayınmaq üçün yerli valyutanı və ya ₼ seçin. Kripto planlaşdırırsınızsa — USDT və ya BTC nəzərdən keçirin, şəbəkə ödənişlərini unutmayın.'),
    ('<div class="note">Important: currency is set at registration. To change it you usually need to create a new account.</div>', '<div class="note">Vacib: valyuta qeydiyyatda təyin olunur. Dəyişdirmək üçün adətən yeni hesab lazımdır.</div>'),
    ('KYC is standard identity verification. It is required for security and withdrawals. Usually they request an ID document, proof of address and sometimes a selfie.', 'KYC standart şəxsiyyət yoxlamasıdır. Təhlükəsizlik və çəkimlər üçün lazımdır. Adətən şəxsiyyət vəsiqəsi, ünvan sübutu və bəzən selfi tələb olunur.'),
    ('<li>Upload a photo of your passport or ID card.</li>', '<li>Pasport və ya ID kartının şəklini yükləyin.</li>'),
    ('<li>Add proof of address (utility bill, bank statement).</li>', '<li>Ünvan sübutu əlavə edin (kommunal hesab, bank hesabı).</li>'),
    ('<li>Wait for verification (usually 24–48 hours).</li>', '<li>Yoxlamanı gözləyin (adətən 24–48 saat).</li>'),
    ('<div class="tip">Tip: scan documents in good quality, without glare or cropped edges.</div>', '<div class="tip">Məsləhət: sənədləri yaxşı keyfiyyətdə, parıltı və kəsilmiş kənarlar olmadan skan edin.</div>'),
    ('<h2>2FA: Why and How to Enable</h2>', '<h2>2FA: nə üçün və necə aktivləşdirmək</h2>'),
    ('Two-factor authentication protects your account from hacking. Enabling takes 2–3 minutes and significantly improves security.', 'İki faktorlu identifikasiya hesabı hakerdən qoruyur. Aktivləşdirmə 2–3 dəqiqə çəkir və təhlükəsizliyi əhəmiyyətli artırır.'),
    ('<li>Go to "Security settings".</li>', '<li>"Təhlükəsizlik parametrləri"nə keçin.</li>'),
    ('<li>Select authenticator app.</li>', '<li>Autentifikator tətbiqini seçin.</li>'),
    ('<li>Scan the QR code and save the backup key.</li>', '<li>QR kodu skan edin və ehtiyat açarı saxlayın.</li>'),
    ('<div class="note">Important: without the backup code, 2FA recovery can take time.</div>', '<div class="note">Vacib: ehtiyat kod olmadan 2FA bərpası vaxt aparır.</div>'),
    ('If you forgot your password, use the recovery form. For email registration — email link; for phone — SMS. Make sure contact details are up to date.', 'Parolu unutmusunuzsa, bərpa formasından istifadə edin. E-poçt qeydiyyatı üçün — e-poçt linki; telefon üçün — SMS. Əlaqə məlumatlarının aktual olduğundan əmin olun.'),
    ('<li>Click "Forgot password?"</li>', '<li>"Parolu unutmusunuz?"a klikləyin.</li>'),
    ('<li>Enter your email or phone number.</li>', '<li>E-poçt və ya telefon nömrənizi daxil edin.</li>'),
    ('<li>Confirm the code and set a new password.</li>', '<li>Kodu təsdiqləyin və yeni parol təyin edin.</li>'),
    ('<h2>Common Registration Mistakes</h2>', '<h2>Ümumi qeydiyyat səhvləri</h2>'),
    ('<li>Wrong email or phone number entered.</li>', '<li>Yanlış e-poçt və ya telefon nömrəsi daxil edilib.</li>'),
    ('<li>Password too weak and fails validation.</li>', '<li>Parol çox zəifdir və yoxlamadan keçmir.</li>'),
    ('<li>Profile not completed before first withdrawal.</li>', '<li>İlk çəkimdən əvvəl profil tamamlanmayıb.</li>'),
    ('<li>Attempting to change currency after registration.</li>', '<li>Qeydiyyatdan sonra valyuta dəyişdirməyə cəhd.</li>'),
    ('To avoid issues, complete your profile immediately, use real data and store 2FA backup codes safely.', 'Problemlərdən yayınmaq üçün profili dərhal tamamlayın, real məlumat istifadə edin və 2FA ehtiyat kodlarını təhlükəsiz saxlayın.'),
]

# Kyrgyz - apply to ky/*.html  
KY_REPLACEMENTS = [
    ('<a href="index.html" style="color:#8f8ca0">Home</a>', '<a href="index.html" style="color:#8f8ca0">Башкы бет</a>'),
    ('<a href="registratsiya-guide.html" style="color:#F9820F">Registration</a>', '<a href="registratsiya-guide.html" style="color:#F9820F">Катталуу</a>'),
    ('<a href="platezhi-guide.html" style="color:#F9820F">Payments</a>', '<a href="platezhi-guide.html" style="color:#F9820F">Төлөмдөр</a>'),
    ('<a href="bonus-guide.html" style="color:#F9820F">Bonuses</a>', '<a href="bonus-guide.html" style="color:#F9820F">Бонусдар</a>'),
    ('<a href="mobile-guide.html" style="color:#F9820F">Mobile</a>', '<a href="mobile-guide.html" style="color:#F9820F">Мобилдик</a>'),
    ('<a href="registratsiya-guide.html" style="color:#8f8ca0">Registration</a>', '<a href="registratsiya-guide.html" style="color:#8f8ca0">Катталуу</a>'),
    ('<a href="platezhi-guide.html" style="color:#8f8ca0">Payments</a>', '<a href="platezhi-guide.html" style="color:#8f8ca0">Төлөмдөр</a>'),
    ('<a href="bonus-guide.html" style="color:#8f8ca0">Bonuses</a>', '<a href="bonus-guide.html" style="color:#8f8ca0">Бонусдар</a>'),
    ('<a href="mobile-guide.html" style="color:#8f8ca0">Mobile</a>', '<a href="mobile-guide.html" style="color:#8f8ca0">Мобилдик</a>'),
    ('<div class="crumbs">Home → Registration</div>', '<div class="crumbs">Башкы бет → Катталуу</div>'),
    ('<div class="crumbs">Home → Payments</div>', '<div class="crumbs">Башкы бет → Төлөмдөр</div>'),
    ('<div class="crumbs">Home → Bonuses</div>', '<div class="crumbs">Башкы бет → Бонусдар</div>'),
    ('<div class="crumbs">Home → Mobile play</div>', '<div class="crumbs">Башкы бет → Мобилдик версия</div>'),
    ('18+ | Play responsibly', '18+ | Жоопкерчиликтүү ойноңуз'),
    # Registratsiya
    ('BigsBet Registration: Complete Guide from A to Z', 'BigsBet катталуу: А дан З ге чейин толук колдонмо'),
    ('Registration: Step-by-step Guide', 'Катталуу: кадамдын-кадамы менен колдонмо'),
    ('Account, currency, KYC and 2FA', 'Каттоо, валюта, KYC жана 2FA'),
    ('Contents', 'Мазмуну'),
    ('4 Registration Methods', '4 катталуу ыкмасы'),
    ('Account Currency Selection', 'Каттоо валютасын тандоо'),
    ('KYC Verification', 'KYC текшерүүсү'),
    ('2FA: Account Protection', '2FA: каттоо коргоосу'),
    ('Password Recovery', 'Сыр сөздү калыбына келтирүү'),
    ('Common Mistakes', 'Кеңири таралган каталар'),
    ('Method 1: Email', '1-ыкма: Email'),
    ('Method 2: Phone', '2-ыкма: Телефон'),
    ('Method 3: Social Networks', '3-ыкма: Социялдык тармактар'),
    ('Method 4: One Click', '4-ыкма: Бир басуу'),
    ('Start Registration', 'Катталууну баштоо'),
    # Platezhi
    ('BigsBet Deposits and Withdrawals: Complete Financial Guide', 'BigsBet депозит жана акча алуу: толук каржылык колдонмо'),
    ('Payments: Deposit and Withdrawal', 'Төлөмдөр: депозит жана акча алуу'),
    ('cards and crypto', 'карталар жана крипто'),
    ('Methods Summary Table', 'Ыкмалардын таблицасы'),
    ('Limits and Fees', 'Чектөөлөр жана төлөмдөр'),
    ('What to Do If Payment Fails', 'Төлөм ийгиликтүү болбосо эмне кылуу керек'),
    ('Method', 'Ыкма'),
    ('Min. deposit', 'Миң. депозит'),
    ('Withdrawal', 'Акча алуу'),
    ('Fee', 'Төлөм'),
    ('usually 0%', 'адатта 0%'),
    ('up to 24 h', '24 саатка чейин'),
    ('Go to Deposit', 'Депозитке өтүү'),
    # Bonus
    ('BigsBet Bonuses: Complete Guide and Calculations', 'BigsBet бонусдары: толук колдонмо жана эсептөөлөр'),
    ('Bonuses: Terms and Benefits', 'Бонусдар: шарттар жана пайдалар'),
    ('Welcome, free spins, cashback and VIP', 'Кош келиңиз, бекер айландыруулар, кэшбэк жана VIP'),
    ('Welcome Bonus', 'Кош келиңиз бонусу'),
    ('Wagering Calculation', 'Вейдер эсептөөсү'),
    ('Free Spins', 'Бекер айландыруулар'),
    ('Cashback', 'Кэшбэк'),
    ('VIP Programme', 'VIP программасы'),
    ('Should You Take a Bonus?', 'Бонус алуу керекпи?'),
    ('Activate Bonus', 'Бонусту активдештирүү'),
    # Mobile
    ('BigsBet Mobile Version: Complete Guide', 'BigsBet мобилдик версиясы: толук колдонмо'),
    ('Mobile Version', 'Мобилдик версия'),
    ('iOS / Android, speed and security', 'iOS / Android, ылдамдык жана коопсуздук'),
    ('Open Mobile Version', 'Мобилдик версияны ачуу'),
    # Body paragraphs - registratsiya KY
    ('This guide explains registration in detail: four ways to create an account, currency selection, KYC verification, enabling 2FA and password recovery. Written for beginners from CIS, including users from Tashkent, Samarkand, Bishkek and Baku. Example currency — €, but you can choose another at registration.', 'Бул колдонмо катталууну толук түшүндүрөт: каттоо түзүүнүн төрт ыкмасы, валюта тандашуу, KYC текшерүү, 2FA иштетүү жана сыр сөздү калыбына келтирүү. Бишкек, Ош жана башка шаарлардан жаңы баштагандар үчүн. Мисал валюта — сом, катталууда башка тандоого болот.'),
    ('BigsBet typically offers several sign-up options: via email, phone, social networks and a simplified "one-click" option. Choose the one that best fits future account recovery.', 'BigsBet адатта бир нече катталуу вариантын сунуштайт: email, телефон, социалдык тармактар жана жөнөкөйлөштүрүлгөн "бир басуу" варианты. Келечекте каттоону калыбына келтирүү үчүн ылайыктуусун тандаңыз.'),
    ('<li>Open the site and click "Register".</li>', '<li>Сайтты ачыңыз жана "Катталуу"ны басыңыз.</li>'),
    ('<li>Enter your email and create a strong password.</li>', '<li>Email киргизиңиз жана бекем сыр сөз түзүңүз.</li>'),
    ('<li>Confirm your email via the link.</li>', '<li>Emailди шилтеме аркылуу ырастаңыз.</li>'),
    ('<li>Complete your profile: name, date of birth, address.</li>', '<li>Профилиңизди толуктаңыз: ысым, туулган күн, дарек.</li>'),
    ('<div class="note">Important: use a real email. It receives bonus confirmations and withdrawal notifications.</div>', '<div class="note">Маанилүү: чыныгы email колдонуңуз. Бонус ырастоолорун жана акча алуу билдирүүлөрүн алат.</div>'),
    ('<li>Select phone registration.</li>', '<li>Тефон менен катталууну тандаңыз.</li>'),
    ('<li>Enter your number and wait for the SMS code.</li>', '<li>Номериңизди киргизиңиз жана SMS кодун күтүңүз.</li>'),
    ('<li>Create a password and confirm sign-in.</li>', '<li>Сыр сөз түзүңүз жана кирүүнү ырастаңыз.</li>'),
    ('<div class="tip">Tip: keep your phone number in your profile — it speeds up account recovery.</div>', '<div class="tip">Кеңеш: профилиңизде телефон номериңизди сактаңыз — каттоону калыбына келтирүүнү ылдамдатат.</div>'),
    ('Registration via social networks is sometimes available. It is faster but ties your account to an external service. Good for users who change devices often and want 1–2 click sign-in.', 'Социалдык тармактар аркылуу катталуу кээде жеткиликтүү. Тезүрөөк, бирок каттоону тышкы кызматка байланат. Тез-тез түзмөктөрдү алмаштырган жана 1–2 басуу менен кирүүнү каалагандар үчүн ылайыктуу.'),
    ('Simplified registration usually requires minimal data. The downside: you will still need to complete your profile for withdrawals later.', 'Жөнөкөйлөштүрүлгөн катталуу адатта минималдуу маалыматты талап кылат. Кемчилиги: акча алуу үчүн профилди толукташыңыз керек болот.'),
    ('Currency choice affects fees, limits and payment convenience. If you use Uzcard, Payme or Click, choose local currency or € to avoid conversion. If planning crypto — consider USDT or BTC, but be aware of network fees.', 'Валюта тандашы төлөмдөргө, чектөөлөргө жана ыңгайлуулукка таасир этет. Uzcard, Payme же Click колдонсоңуз, конвертациядан алыс болуу үчүн жергиликтүү валютаны же сомду тандаңыз. Крипто пландаштырсаңыз — USDT же BTC караңыз, тармак төлөмдөрүн унутпаңыз.'),
    ('<div class="note">Important: currency is set at registration. To change it you usually need to create a new account.</div>', '<div class="note">Маанилүү: валюта катталууда белгиленет. Өзгөртүү үчүн адатта жаңы каттоо керек.</div>'),
    ('KYC is standard identity verification. It is required for security and withdrawals. Usually they request an ID document, proof of address and sometimes a selfie.', 'KYC — стандарттуу жеке кимдигин текшерүү. Коопсуздук жана акча алуу үчүн керек. Адатта ID документ, дарек далили жана кээде селфи сурашат.'),
    ('<li>Upload a photo of your passport or ID card.</li>', '<li>Паспорт же ID картасынын сүрөтүн жүктөңүз.</li>'),
    ('<li>Add proof of address (utility bill, bank statement).</li>', '<li>Дарек далилин кошуңуз (коммуналык төлөм, банктык эсеп).</li>'),
    ('<li>Wait for verification (usually 24–48 hours).</li>', '<li>Текшерүүнү күтүңүз (адатта 24–48 саат).</li>'),
    ('<div class="tip">Tip: scan documents in good quality, without glare or cropped edges.</div>', '<div class="tip">Кеңеш: документтерди жакшы сапатта, чагылга жана кесилген четтери жок сканерлеңиз.</div>'),
    ('<h2>2FA: Why and How to Enable</h2>', '<h2>2FA: эмне үчүн жана кантип иштетүү</h2>'),
    ('Two-factor authentication protects your account from hacking. Enabling takes 2–3 minutes and significantly improves security.', 'Эки факторлуу аутентификация каттоону хакерден коргойт. Иштетүү 2–3 мүнөт талап кылат жана коопсуздугун айрыкча жогорулатат.'),
    ('<li>Go to "Security settings".</li>', '<li>"Коопсуздук параметрлери"не өтүңүз.</li>'),
    ('<li>Select authenticator app.</li>', '<li>Аутентификатор тиркемесин тандаңыз.</li>'),
    ('<li>Scan the QR code and save the backup key.</li>', '<li>QR кодду сканерлеңиз жана резервдик ачкычты сактаңыз.</li>'),
    ('<div class="note">Important: without the backup code, 2FA recovery can take time.</div>', '<div class="note">Маанилүү: резервдик кодсуз 2FA калыбына келтирүү убакыт алышы мүмкүн.</div>'),
    ('If you forgot your password, use the recovery form. For email registration — email link; for phone — SMS. Make sure contact details are up to date.', 'Сыр сөздү унутуп калсаңыз, калыбына келтирүү формасын колдонуңуз. Email катталуу үчүн — email шилтеме; телефон үчүн — SMS. Байланыш маалыматтары актуалдуу экенин текшериңиз.'),
    ('<li>Click "Forgot password?"</li>', '<li>"Сыр сөздү унутуп калдыңызбы?"ны басыңыз.</li>'),
    ('<li>Enter your email or phone number.</li>', '<li>Email же телефон номериңизди киргизиңиз.</li>'),
    ('<li>Confirm the code and set a new password.</li>', '<li>Кодду ырастаңыз жана жаңы сыр сөз коюңуз.</li>'),
    ('<h2>Common Registration Mistakes</h2>', '<h2>Кеңири таралган катталуу каталары</h2>'),
    ('<li>Wrong email or phone number entered.</li>', '<li>Туура эмес email же телефон номери киргизилген.</li>'),
    ('<li>Password too weak and fails validation.</li>', '<li>Сыр сөз өтө начар жана текшерүүдөн өтпөйт.</li>'),
    ('<li>Profile not completed before first withdrawal.</li>', '<li>Биринчи акча алуудан мурун профил толукталбаган.</li>'),
    ('<li>Attempting to change currency after registration.</li>', '<li>Катталуудан кийин валютаны өзгөртүүгө аракет.</li>'),
    ('To avoid issues, complete your profile immediately, use real data and store 2FA backup codes safely.', 'Маселелерден алыс болуу үчүн профилди дароо толуктаңыз, чыныгы маалымат колдонуңуз жана 2FA резервдик коддорун коопсуз сактаңыз.'),
]

def apply_replacements(path, repl_list):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    for old, new in repl_list:
        c = c.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

def main():
    for fname in os.listdir('az'):
        if fname.endswith('-guide.html') or fname == 'index.html':
            apply_replacements(f'az/{fname}', AZ_REPLACEMENTS)
            print(f'AZ: {fname}')
    for fname in os.listdir('ky'):
        if fname.endswith('-guide.html') or fname == 'index.html':
            apply_replacements(f'ky/{fname}', KY_REPLACEMENTS)
            print(f'KY: {fname}')
    print('Nav/crumbs/footer done')

if __name__ == '__main__':
    main()
