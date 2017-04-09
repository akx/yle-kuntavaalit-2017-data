import argparse
import glob
import json

from kvd_utils import download_json, get_session

ext_url_template = 'https://vaalit.yle.fi/content/kv2017/{version}/electorates/{electorate}/municipalities/{municipality}/pollingDistricts/{district}/partyAndCandidateResults.json'


def download_ext_data(version):
    sess = get_session()
    for muni_fn in glob.glob('data/{version}/*.json'.format(version=version)):
        with open(muni_fn, encoding='utf-8') as infp:
            muni = json.load(infp)
        name = muni['calculationStatus']['name']['fi']
        perc = float(muni['calculationStatus']['calculationStatusPercent'])
        if perc < 100:
            print('%s: %.2f%% less than 100%% percent!' % (name, perc))
        for district in muni['pollingDistricts']:
            url = ext_url_template.format(
                version=version,
                electorate=muni['calculationStatus']['edid'],
                municipality=muni['calculationStatus']['muid'],
                district=district['pdid'],
            )
            output_file = 'ext_data/{version}/{name}/{district}.json'.format(
                version=version,
                name=name,
                district=district['name']['fi'].replace(' ', '_'),
            )
            download_json(sess, url, output_file)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('version', type=int)
    args = ap.parse_args()
    download_ext_data(version=args.version)
