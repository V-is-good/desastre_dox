#desastredox vasado en doxxer tolkit
import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[30m'  # VARIABLE BUAT WARNA CUYY
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


# utilities

# decorator for attaching run_banner to a function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)


    return wrapper


# FUNCTIONS FOR MENU
@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")  # INPUT IP ADDRESS
    print()
    print(f' {Wh}============= {Mage}SHOW INFORMATION IP ADDRESS {Wh}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n IP target       :{Mage}", ip)
    print(f"{Wh} Type IP         :{Mage}", ip_data["type"])
    print(f"{Wh} Country         :{Mage}", ip_data["country"])
    print(f"{Wh} Country Code    :{Mage}", ip_data["country_code"])
    print(f"{Wh} City            :{Mage}", ip_data["city"])
    print(f"{Wh} Continent       :{Mage}", ip_data["continent"])
    print(f"{Wh} Continent Code  :{Mage}", ip_data["continent_code"])
    print(f"{Wh} Region          :{Mage}", ip_data["region"])
    print(f"{Wh} Region Code     :{Mage}", ip_data["region_code"])
    print(f"{Wh} Latitude        :{Mage}", ip_data["latitude"])
    print(f"{Wh} Longitude       :{Mage}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} Maps            :{Mage}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} EU              :{Mage}", ip_data["is_eu"])
    print(f"{Wh} Postal          :{Mage}", ip_data["postal"])
    print(f"{Wh} Calling Code    :{Mage}", ip_data["calling_code"])
    print(f"{Wh} Capital         :{Mage}", ip_data["capital"])
    print(f"{Wh} Borders         :{Mage}", ip_data["borders"])
    print(f"{Wh} Country Flag    :{Mage}", ip_data["flag"]["emoji"])
    print(f"{Wh} ASN             :{Mage}", ip_data["connection"]["asn"])
    print(f"{Wh} ORG             :{Mage}", ip_data["connection"]["org"])
    print(f"{Wh} ISP             :{Mage}", ip_data["connection"]["isp"])
    print(f"{Wh} Domain          :{Mage}", ip_data["connection"]["domain"])
    print(f"{Wh} ID              :{Mage}", ip_data["timezone"]["id"])
    print(f"{Wh} ABBR            :{Mage}", ip_data["timezone"]["abbr"])
    print(f"{Wh} DST             :{Mage}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} Offset          :{Mage}", ip_data["timezone"]["offset"])
    print(f"{Wh} UTC             :{Mage}", ip_data["timezone"]["utc"])
    print(f"{Wh} Current Time    :{Mage}", ip_data["timezone"]["current_time"])


@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}Enter phone number target {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}")  # INPUT NUMBER PHONE
    default_region = "ID"  # DEFAULT NEGARA INDONESIA

    parsed_number = phonenumbers.parse(User_phone, default_region)  # VARIABLE PHONENUMBERS
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)
    print(f"\n {Wh}========== {Mage} DOXNUMBERS {Wh}==========")
    print(f"\n {Wh}Location             :{Mage} {location}")
    print(f" {Wh}Region Code          :{Mage} {region_code}")
    print(f" {Wh}Timezone             :{Mage} {timezoneF}")
    print(f" {Wh}Operator             :{Mage} {jenis_provider}")
    print(f" {Wh}Valid number         :{Mage} {is_valid_number}")
    print(f" {Wh}Possible number      :{Mage} {is_possible_number}")
    print(f" {Wh}International format :{Mage} {formatted_number}")
    print(f" {Wh}Mobile format        :{Mage} {formatted_number_for_mobile}")
    print(f" {Wh}Original number      :{Mage} {parsed_number.national_number}")
    print(
        f" {Wh}E.164 format         :{Mage} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{Mage} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{Mage} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{Mage} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{Mage} This is a fixed-line number")
    else:
        print(f" {Wh}Type                 :{Mage} This is another type of number")


@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}Enter Username : {Gr}")
        results = {}
        social_media = [
                        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"},
            {"url": "https://www.clover.space/s/u/{}", "name": "clover space"},
            {"url": "https://aminoapps.com/u/{}", "name": "Amino"},
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}Username not found {Ye}!")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Mage}========== {Mage}SHOW INFORMATION USERNAME {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Mage}[ {Mage}+ {Mage}] {site} : {Mage}{url}")

# OPTIONS
options = [
    {
        'num': 1,
        'text': 'IP scan',
        'func': IP_Track
    },
    
    {
        'num': 3,
        'text': 'Phone Number Tracker',
        'func': phoneGW
    },
    
    {
        'num': 4,
        'text': 'Username Tracker',
        'func': TrackLu
    },
    
    {
        'num': 0,
        'text': 'Exit',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Mage}[ {Mage} ⏈⃟𝒦⃟⚖ {Mage}] {Mage}Presione continuar')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Mage}[ {Mage}! {Mage}] {Mage}Exit')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Mage}[ {opt["num"]} ] {Mage}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # BANNER TOOLS
    clear()
    stderr.writelines(f""" {Mage}
⡏⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢾⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡥⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢧⢩⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⡄⠀⠠⠈⢢⢃⠧⡀⠹⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠀⢎⠲⡑⢀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣦⠀⠀⠀⠀⢏⢀⣿⣷⡄⠙⠽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀
⡿⠿⠀⠀⠀⠀⠀⡜⣿⣿⣿⣧⡀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣾⡇⠀⠠⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠇⡣⢄⡄⡉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣾⣿⣷⡀⠀⠀⠀⠀⠀⠀⢀⣀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡟⢰⠡⡇⡜⢀⣾⣦⣍⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢋⣥⣶⣿⣿⣷⣮⣝⣿⡿⢿⣟⣋⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣾⣿⣿⣿⣿⣶⣶⡤⢀⣠⣾⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⢋⠐⠣⢓⡜⢰⣿⣿⣿⣿⢐⠢⡌⡙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⣴⣿⣿⣿⡿⣛⣛⣻⣿⣔⣿⣿⣿⣿⣿⣧⣤⣤⣭⣉⡙⠯⢿⣟⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢾⣿⣿⣿⣿⣿⣿⣿⢣⣿⣿⣿⣿⣿⣿
⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⢀⣤⣛⠿⣿⣿⠏⣌⠳⣘⠥⡓⢤⢨⣙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣾⣿⣿⡟⣵⣛⣭⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡩⢉⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢒⠆⠹⣿⣿⣿⣿⣿⠇⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣶⣶⣦⣁⠻⠿⠿⠒⠀⠈⠈⠣⢣⢎⡱⢊⢈⣿⣿⣶⣬⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⣿⡿⢃⣴⣾⣿⣿⣿⣿⣿⣿⣿⡟⡟⠳⠾⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠠⡑⠪⢜⡡⢌⡛⠯⣉⠀⣰⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠈⠰⢀⠁⠢⡀⠌⡐⠋⣼⣿⣿⣿⣿⣿⡇⢌⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠉⣴⣾⣿⣿⣿⣿⣿⡿⠟⠋⡁⢦⣾⣿⡷⢒⣲⣤⣤⣈⢭⣛⢿⣿⢿⠿⣿⣷⡉⣟⢿⣿⢏⣭⣥⣤⣉⢛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡁⠰⢡⠘⡡⢎⡔⢣⡜⡱⡌⢠⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠂⠁⠄⠃⣠⣾⣯⣻⢿⣿⣿⣿⠃⡎⡜⡱⢌⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣧⣷⣙⠻⣿⣿⣿⠟⡡⢆⡻⠀⡇⡘⣿⡟⣠⣵⣶⣶⣮⣝⠳⣮⢳⣮⡑⠦⡍⢻⣧⢿⣷⡜⣿⣿⣿⣿⣿⣷⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣵⣷⠀⢃⠜⣐⠣⡜⡡⠎⡱⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠻⣿⣿⣿⣿⣷⣮⣻⠟⡘⡴⣉⠶⣉⠖⠸⣮⣝⠿⣿⣿⣿⣿⣿⠋⣿⡿⣳⣤⣷⠀⣠⠗⢠⠁⡇⢠⠱⣹⣍⠿⣿⣿⣿⣿⣿⣷⡘⣧⢻⣷⡔⢙⡀⠿⣿⣿⡟⣿⣿⣿⣿⣿⣿⠇⢸⣿⣿⣿⣿⣿⣿⣿⠟⠀⣾⣿⣿⣷⣄⠊⠴⣉⢖⡡⢀⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡕⢻⣟⠻⣿⡿⠟⢁⠰⣀⢁⠊⢖⡡⠞⢡⣿⣿⣿⣮⣙⢿⠟⣭⢰⢏⡾⢫⡟⠁⢰⡝⠂⡼⢀⡇⠘⣦⠈⠽⣷⣮⣛⠿⣿⣿⡿⣡⢹⢸⣿⢟⣼⡅⡛⣶⡝⠷⣿⣿⣋⠬⣭⣛⢾⣸⣿⣿⣿⣿⣿⡿⠋⠀⢀⠙⣿⣿⣿⣿⣿⣶⣬⣤⣥⡠⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠛⠉⠁⡀⠢⠌⢒⠠⢊⠌⠤⣈⠃⣾⣿⣿⣿⣿⡿⠃⣬⡏⢹⢸⡇⠋⡔⡁⢺⠄⣸⠁⡸⢠⡄⠈⠈⠦⡙⠚⠿⠿⠶⠆⣐⠃⠊⠘⠳⠟⡋⣾⣿⢸⡇⢀⡐⠻⠿⣟⣢⡙⢷⣜⢿⣿⣿⣿⡿⠁⢠⠘⡄⢂⠘⢿⣿⣿⣿⣿⣿⣿⣿⢱⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⡐⠀⠡⢈⠂⠡⠊⡄⠣⢀⣾⣿⣯⣻⣿⣿⡇⡇⣭⡵⠌⠈⠃⠰⢠⠃⠀⡴⠃⢠⠇⢚⣛⣀⠠⣦⣈⠳⣶⣶⠶⠛⢁⣨⡐⠶⣘⠛⠇⢛⣣⠞⢡⣦⡉⢡⣾⡿⣋⣼⢇⢻⡜⣿⣿⡿⠁⡐⠢⢡⠘⡄⠣⡀⢙⠻⢿⣿⣿⣿⣧⣿⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⠑⢢⠀⠌⠀⢁⣠⣶⣿⣿⣿⣿⣿⡿⢟⣣⢻⡜⣿⣯⣤⠀⡇⠃⠠⠐⠁⡰⠉⡤⠛⠿⢛⢷⣈⢻⣷⣶⣤⡤⠀⠉⢤⣤⣤⠀⠁⢈⡀⢶⡟⣮⡻⣿⡃⠀⣚⣫⣷⠟⣼⠇⣿⣿⠁⡀⠡⢃⠢⡁⢆⠱⢈⠆⡱⢂⠬⣩⠁⠌⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡠⢶⣾⣶⣬⣉⡛⠛⢍⣩⣵⣶⢻⣿⣿⠷⣙⠦⠉⠁⠀⠀⡀⢤⠄⠀⠀⢀⣴⣶⣐⠠⣬⡝⣷⣬⣝⣩⣵⢦⡴⣾⣿⣫⡾⢰⡰⡆⡈⠻⣮⡻⢦⣝⣓⣛⣋⡥⠚⡛⣸⢿⡇⡄⢣⠐⠁⢆⡑⢨⠐⡡⢊⠴⣉⠖⡡⠈⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣀⣠⣭⣭⣭⣵⣾⣿⣿⣿⠿⠸⠐⣾⣿⣿⠁⣾⣶⡔⠃⢱⠂⢠⠁⢠⢳⣎⣙⣟⣫⣝⣷⢋⣿⣿⣿⣿⡷⢸⣿⣿⣿⡏⠈⡧⠁⢿⠀⢹⡻⢷⣬⣭⣭⢖⡴⢟⣴⣿⣷⣅⢼⡈⣷⣌⡀⠘⠤⡑⠄⢣⠘⡤⠋⠄⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣻⣭⣶⣿⣿⣿⣿⣿⣿⣿⡿⢟⣯⣶⣿⣆⠀⠘⢿⣿⢀⠙⣁⣴⠎⢀⠴⠁⢀⠸⣅⠹⣿⣿⣿⣿⣿⢛⣹⣿⣿⣿⣿⡄⠻⣿⡿⠼⠂⠀⠗⡠⣷⢸⣿⡷⢂⡭⣱⣶⡾⣸⣿⣿⣿⣿⣷⣤⡈⠙⣿⣶⣤⣌⣈⣀⠃⢀⣁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣛⣽⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣛⣵⣾⣿⣿⣿⣿⣿⠷⢦⣄⣀⠐⠀⠉⠐⠀⠁⢐⡀⠁⠐⠈⠁⠙⣿⣿⣿⣿⠈⣡⣤⣌⢻⣿⣿⣶⡄⢀⣀⠌⠂⠈⠑⠊⠃⠨⠤⢨⠾⠿⢟⣱⣭⡻⣿⣿⣿⣿⣿⣿⣶⣬⣛⣺⢿⢿⣛⠿⡿⣏⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⣶⣿⣿⠟⠵⣿⣿⣿⣿⣿⡿⢟⣫⣶⣿⣿⣿⣿⡿⠟⠛⠩⠶⠿⢷⣦⣭⣅⡀⢂⠉⣡⣶⠟⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣌⡛⢛⣡⣾⡿⠟⠋⡀⠀⠉⠶⣌⣁⣂⡀⢀⣤⣥⢹⣿⣿⣿⣷⣍⠻⢦⣝⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣝⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣾⣿⢿⡟⣩⣴⣿⣿⣿⡿⢟⣭⣶⣿⣿⣿⡿⠟⠉⡁⠄⣀⠬⣐⠦⡘⢤⡀⠩⠙⠿⡐⠿⠛⢁⠀⡤⠖⠁⡀⠴⠀⠀⠀⢀⡆⠉⠛⠻⠟⠉⠀⠀⠀⠈⠑⠂⠀⠀⣈⣤⠴⠿⢿⣿⣇⢿⠟⠋⣥⣴⣿⣦⣉⠛⢮⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡙⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠱⣋⣭⣋⣵⣾⣿⣿⡿⢟⣭⣾⣿⣿⣿⣿⠟⠉⠠⢄⠣⢀⢲⠡⢞⡡⣚⠱⣆⡙⠦⣍⠒⡈⠹⣷⠆⣼⣿⣿⣿⣿⣿⣶⣤⡠⣭⣥⣷⣤⣀⣤⢶⣷⣽⣦⣿⣿⣾⣿⣿⣎⢿⣿⣿⣷⡌⠛⠀⢀⠉⠉⡙⠫⠿⢿⣦⠀⠉⠻⣮⣙⢿⣿⣿⣿⣿⡻⢿⣿⣿⣿⣿⣿⣮⡹⢽⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⣴⣿⣿⣿⣿⣿⠿⣛⣵⣾⣿⣿⣿⣿⠿⠋⠀⡔⠢⠌⢠⠸⡌⡖⣌⢣⠝⡢⢍⡳⢰⣉⠦⢥⠀⢿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⡍⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⣿⣿⠏⠁⢀⠠⠘⡀⢂⢡⡀⡄⡈⠛⠖⣀⠀⠹⣿⣾⣝⠿⣿⣿⣷⡸⣝⠿⣿⣿⣿⣿⣷⣮⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣴⣿⣿⣿⣿⣷⣾⡶⣿⣿⣿⣿⣿⣿⡿⠋⠀⠄⠣⢐⣁⣬⣤⣭⣬⣬⣬⣬⣌⣁⡃⠜⡡⢎⡜⢆⣃⠸⣿⣿⣿⣿⣿⣿⣷⣭⣛⠿⣣⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠁⢀⣐⣈⣀⡁⠦⣉⠦⡱⢬⡑⡲⢄⡠⠁⠀⡙⠿⣿⣿⣶⣽⣛⣣⣿⣿⣮⣛⢿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢿⣿⣿⣿⡿⢟⣥⣾⣿⣿⣿⣿⠿⢉⠀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣬⡘⠨⢆⠀⡟⢿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣷⣄⠙⠿⣿⣿⣿⣿⣿⠟⠋⣠⣾⣿⣿⣿⣿⣿⣿⣶⣦⣥⡒⠥⡓⡜⡰⢃⡆⣈⢢⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣷⡝⣿⣿⣿⠄⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠙⠛⠩⠶⢿⣿⣿⣿⣿⠟⠁⣠⣴⣾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⡀⠀⠀⠈⠍⠙⠉⣉⣥⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣌⡙⢋⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⡒⣍⠣⡜⢆⠆⠁⣆⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⣿⢏⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣭⣟⣛⣛⣛⣩⡔⢠⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢘⣤⣾⣷⣿⣿⣿⣿⣿⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠂⠹⣌⠞⠀⣿⣿⣦⣝⣛⣿⣿⣿⣿⣿⣯⢗⣧⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣾⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣷⢙⣩⡥⢆⣛⣿⣗⣈⣙⣛⣈⣛⠿⣯⣝⡛⣛⣻⡟⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡐⢬⠚⢰⣿⣿⣿⣿⣿⣿⣿⣿⠇⣪⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⢏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⣻⣿⢏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⣶⣿⣿⣿⣿⣿⣿⡟⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢼⣿⣿⡸⣿⡿⠿⠿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⢇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣴⣿⣿⣿⣿⡿⣛⠟⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⡿⢋⣴⣾⣿⣟⡀⣭⣶⣿⣿⣶⣭⡻⣿⡿⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⠟⣫⡶⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⠟⣴⣿⣿⣿⡿⢠⢸⣿⣿⣿⣿⣿⣿⠟⣀⡶⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣿⣿⣶⠿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣻⣿⣿⡟⡅⡎⠊⣿⣿⣿⣿⣿⠋⣼⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠈⠀⠈⡅⢿⣿⣿⣿⠏⣼⡿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⠟⣁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠿⣿⣿⡆⠀⠀⣴⣿⣿⣿⣷⢸⢯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⢹⣿⣿⣄⣼⣿⣿⣿⣿⠇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⣌⠀⢻⡿⠿⢹⡿⣿⡿⠏⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢃⠖⠈⢀⣠⠌⡁⢀⣻⡇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣘⢃⡞⣰⣿⣿⣷⣎⣿⣿⠳⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⠏⣜⣷⣿⣿⣿⣿⣿⣿⣿⣦⢻⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢨⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣜⢦⢈⣛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣕⢍⣻⣶⣭⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣱⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⣉⣩⣥⣶⣶⣶⣮⣑⠻⠿⣯⣷⢯⡿⣽⣻⣽⣻⡿⡟⠃⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⢹⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⠞⢉⣄⣩⣙⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⣡⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣭⣉⣛⣙⡛⣙⣉⣩⣤⣀⠰⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢠⠈⠙⠾⣷⣯⣿⣻⢿⡿⣿⢿⣿⣻⣟⠿⠛⠛⠛⣥⣮⣗⡪⠝⣻⢸⣿⠶⣭⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣠⣾⣿⣿⣯⣭⣝⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠳⢦⠄⣄⣈⠁⠉⠛⠙⠊⢉⡨⠅⣀⣤⣴⣶⣷⣶⣿⣿⣿⣿⣾⣷⡻⣷⣝⢳⣕⢬⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣉⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣝⡻⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⠾⢋⣀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠋⠶⠘⣿⣿⣿⣿⣿⡿⢋⣥⣾⣿⣿⣿⣿⣿⣿⡿⣛⣭⣛⡿⣿⣿⣜⢿⣿⣜⢳⣍⠎⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⠿⠃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣟⠚⡀⣼⣿⣶⡜⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢀⠢⣿⣿⣿⣿⢛⣴⣿⣿⣿⣿⣿⣿⣿⣿⡟⣱⣿⣿⣿⣿⣾⣿⣿⣷⣙⢿⣷⣍⣿⣶⡉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣿⠃⣾⣱⣿⣿⣿⣿⣆⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⣖⠈⢿⡝⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣆⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢡⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡇⢸⣿⣿⣿⣿⣿⣿⣿⣧⠀⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣾⡷⢨⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⢻⣿⣿⣿⣿⣿⣿⣿⣇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⢸⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿


              {Mage}[   ⏈⃟𝒦⃟⚖  ]  D E S A S T R E [   ⏈⃟𝒦⃟⚖  ]
    """)

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Mage}

        """)
    time.sleep(0.5)
    

def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Mage}\n [ ⏈⃟𝒦⃟⚖ ] {Mage}Select Option : {Mage}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Mage}[ {Mage}! {Mage}] {Mage}Please input number')
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()
