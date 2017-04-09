import os

import requests


def download_json(sess, url, output_file):
    if os.path.exists(output_file) and os.stat(output_file).st_size > 0:
        return False
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)
    resp = sess.get(url)
    if resp.status_code >= 400:
        print(url, resp.status_code, resp.content)
        return False
    try:
        resp.json()
    except:
        print(url, 'not json')
        return False
    with open(output_file, 'wb') as outf:
        outf.write(resp.content)
    print('ok', url)

def get_session():
    sess = requests.Session()
    sess.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3063.4 Safari/537.36'
    sess.headers['referer'] = 'https://vaalit.yle.fi/'
    return sess
