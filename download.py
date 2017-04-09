from kvd_utils import download_json, get_session

sess = get_session()

with open('municipalities.json', 'wb') as outf:
    resp = sess.get('https://vaalit.yle.fi/content/kv2017/municipalities.json')
    outf.write(resp.content)
    muni_data = resp.json()['municipalities']

latest_version_data = sess.get('https://vaalit.yle.fi/content/kv2017/latestVersion.json').json()
url_template = 'https://vaalit.yle.fi/content/kv2017/{version}/electorates/{electorate}/municipalities/{municipality}/partyAndCandidateResults.json'

for version in range(latest_version_data['mainVersion'], 1, -1):
    for muni in muni_data:
        url = url_template.format(version=version, electorate=muni['edid'], municipality=muni['muid'])
        output_file = 'data/{version}/{name}.json'.format(version=version, name=muni['name']['fi'])
        download_json(sess, url, output_file)
