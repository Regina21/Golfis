import tweepy
import json
import math
import glob
import csv
import zipfile
import zlib
from tweepy import TweepError
from time import sleep

users= ['DjokerNole','ThiemDomi', 'RafaelNadal', 'rogerfederer', 'keinishikori ‏',
'KAndersonATP', 'delpotrojuan', 'JohnIsner', 'StefTsitsipas', 'cilic_marin',
'karenkhachanov', 'borna_coric', 'milosraonic', 'DaniilMedwed', 'fabiofogna',
'Gael_Monfils', 'nikolozbasilash', 'David__Goffin', 'pablocarreno91',
'kyle8edmund', 'denis_shapo', 'dieschwartzman', 'BautistaAgut', 'alexdeminaur',
'GillesSimon84','richardgasquet1', 'GrigorDimitrov', 'la_pouille', 'guido_pella',
'FTiafoe', 'FerVerdasco', 'stanwawrinka', 'SJohnson_89', 'johnhmillman', 'jimchardy',
'joaosousa30', 'Kohlscribbler', 'Dutzee', 'Struffitennis', 'RaduAlbot',
'p2hugz', 'mattebden', 'cam_norrie', 'DzumhurDamir', 'AdrianMannarino',
'Taylor_Fritz97', 'felixtennis', 'M_Jaziri', 'jamunar_38', 'YacaMayer',
'yoshihitotennis', 'robin_haase', 'juanlondero', 'benoitpaire', 'SamQuerrey',
'AljazBedene', 'deniskudla', 'tarodaniel93', 'MariusCopil', 'ugo_dellien',
'ivokarlovic', 'NicoJarry', 'guidoandreozzi', 'berankisr', 'FedeDelbonis',
'PabloCuevas22', 'albertramos88', 'AndujarPablo', 'Pojd_Tomas', 'TennysSandgren',
'BradleyKlahn', 'feliciano_lopez', 'CasperRuud98', 'AndreyRublev97', 'jiri_vesely']
for user in users:

    with open('api_keys.json') as f:
        keys = json.load(f)

    auth = tweepy.OAuthHandler('JfC0pEsb4HHURc2ZaeKtkYM3I', 'LIWEgZVOT09lr5Dd55TObI1xL0WCy67wKqChKi3FPlsOHGZUMo')
    auth.set_access_token('1098609809740447745-3Q8VVxFQI1P5xgzDtL6HcLc9klFoGK', 'KK9MJZpMr1ZaphXZif35LTYAmTcKxxKX8y2mmsojgVxcW')
    api = tweepy.API(auth)
    user = user.lower()
    output_file = '{}.json'.format(user)
    output_file_short = '{}_short.json'.format(user)
    compression = zipfile.ZIP_DEFLATED

    with open('all_ids.json') as f:
        ids = json.load(f)

    print('total ids: {}'.format(len(ids)))

    all_data = []
    start = 0
    end = 100
    limit = len(ids)
    i = math.ceil(limit / 100)

    for go in range(i):
        print('currently getting {} - {}'.format(start, end))
        sleep(6)  # needed to prevent hitting API rate limit
        id_batch = ids[start:end]
        start += 100
        end += 100
        tweets = api.statuses_lookup(id_batch)
        for tweet in tweets:
            all_data.append(dict(tweet._json))

    print('metadata collection complete')
    print('creating master json file')
    with open(output_file, 'w') as outfile:
        json.dump(all_data, outfile)

    print('creating ziped master json file')
    zf = zipfile.ZipFile('{}.zip'.format(user), mode='w')
    zf.write(output_file, compress_type=compression)
    zf.close()

    results = []

    def is_retweet(entry):
        return 'retweeted_status' in entry.keys()

    def get_source(entry):
        if '<' in entry["source"]:
            return entry["source"].split('>')[1].split('<')[0]
        else:
            return entry["source"]

    with open(output_file) as json_data:
        data = json.load(json_data)
        for entry in data:
            t = {
                "created_at": entry["created_at"],
                "text": entry["text"],
                "in_reply_to_screen_name": entry["in_reply_to_screen_name"],
                "retweet_count": entry["retweet_count"],
                "favorite_count": entry["favorite_count"],
                "source": get_source(entry),
                "id_str": entry["id_str"],
                "is_retweet": is_retweet(entry)
            }
            results.append(t)

    print('creating minimized json master file')
    with open(output_file_short, 'w') as outfile:
        json.dump(results, outfile)

    with open(output_file_short) as master_file:
        data = json.load(master_file)
        fields = ["favorite_count", "source", "text", "in_reply_to_screen_name", "is_retweet", "created_at", "retweet_count", "id_str"]
        print('creating CSV version of minimized json master file')
        f = csv.writer(open('{}.csv'.format(user), 'w'))
        f.writerow(fields)
        for x in data:
            f.writerow([x['favorite_count'], x['source'], x['text'], x['in_reply_to_screen_name'], x['is_retweet'], x['created_at'], x['retweet_count'], x['id_str']])
