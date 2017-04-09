import os

import requests
import json

sess = requests.Session()
sess.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3063.4 Safari/537.36'
sess.headers['referer'] = 'https://vaalit.yle.fi/'

muni_data = json.load(open('muni.json', encoding='utf-8'))
latest_version_data = sess.get('https://vaalit.yle.fi/content/kv2017/latestVersion.json').json()
url_template = 'https://vaalit.yle.fi/content/kv2017/{version}/electorates/{electorate}/municipalities/{municipality}/partyAndCandidateResults.json'

for version in range(latest_version_data['mainVersion'], 1, -1):
    for muni in muni_data:
        url = url_template.format(version=version, electorate=muni['electorate'], municipality=muni['municipality'])
        output_file = 'data/{version}/{name}.json'.format(version=version, name=muni['name'])
        if os.path.exists(output_file):
            continue
        output_dir = os.path.dirname(output_file)
        os.makedirs(output_dir, exist_ok=True)
        resp = sess.get(url)
        if resp.status_code >= 400:
            print(url, resp.status_code, resp.content)
            continue
        with open(output_file, 'wb') as outf:
            outf.write(resp.content)
        print('ok', version, muni)
