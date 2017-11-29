import re
import time
import requests


def get(target_url):
    r = requests.get(target_url)
    if r.status_code == 200:
        __save(target_url, r.text)


def __save(url, html):
    html = re.sub('\r\n', '\n', html)
    file_name = re.findall('\.(.*?)\.', url)[0]
    print(file_name)
    file_name = 'pages/{}.html'.format(file_name)
    # open(file_name, 'w').close()
    with open(file_name) as a:
        old = a.read()
    if str(old) != str(html):
        with open(file_name + time.strftime('%m%d-%H:%M', time.localtime()), 'w') as a:
            a.write(old)
        with open(file_name, 'w') as a:
            a.write(html)
            print('Saved!')
