import json
import requests

CACHE_FNAME = "cache_file_name.json"

try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    cache_diction = json.loads(cache_contents)
    cache_file.close()

except:
    cache_diction = {}

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get_from_datamuse_caching(rhymes_with):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {}
    params_diction["rel_rhy"] = rhymes_with
    unique_ident = params_unique_combination(baseurl,params_diction)
    if unique_ident in cache_diction:
        return cache_diction[unique_ident]
    else:
        resp = requests.get(baseurl, params_diction)
        cache_diction[unique_ident] = json.loads(resp.text)
        dumped_json_cache = json.dumps(cache_diction, indent=4)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return cache_diction[unique_ident]

class RhymeData(object):
    def __init__(self, diction, search_term):
        self.rhymes_with = search_term
        self.word = diction['word']
    def __str__(self):
        return "{} rhymes with {} and has {} nummber of syllables".format(self.word,self.rhymes_with,self.numSyllables)
rhyme_word_lst = []
rhyme_data = get_from_datamuse_caching("pear")




app_id = 'dff9da73'
app_key = '56ab115671f322739705c62f04b85818'
lemma = input("type a word here")
url = 'https://od-api.oxforddictionaries.com:443/api/v1/words/' + lemma

def get_from_dict_caching(word):
    unique_ident = params_unique_combination(url, params_d={})
    if unique_ident in cache_diction:
        return cache_diction[unique_ident]
    else:
        resp = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        cache_diction[unique_ident] = json.loads(resp.text)
        dumped_json_cache = json.dumps(cache_diction, indent=4)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return cache_diction[unique_ident]
print(get_from_dict_caching(lemma))
#music_results = get_from_itunes_caching("jayz")


#print("code {}\n".format(r.status_code))
#print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))


#def get_from_musix_caching(song_lyrics):
    #baseurl = "https://od-api.oxforddictionaries.com:443/api/v1/entries/"
    #params_diction = {}
    #params_diction["app_key"] = ox_app_key
    #params_diction[]
    #params_diction["app_id"] = ox_app_id
    #params_diction["word"] = word_id
    #params_diction["entity"] = "song"
    #unique_ident = params_unique_combination(baseurl,params_diction)
    #if unique_ident in cache_diction:
        #return cache_diction[unique_ident]
    #else:
        #resp = requests.get(baseurl, params_diction)
        #cache_diction[unique_ident] = json.loads(resp.text)
        #dumped_json_cache = json.dumps(cache_diction, indent=4)
        #fw = open(CACHE_FNAME,"w")
        #fw.write(dumped_json_cache)
        #fw.close() # Close the open file
        #return cache_diction[unique_ident]
