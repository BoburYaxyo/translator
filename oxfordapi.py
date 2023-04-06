import requests
import json

app_id = "f499f895"
app_key = "d0884db85ddec855f7e983c758dd0bb0"
language = "en-gb"


def get_definitons(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res=r.json()
    if 'error' in res.keys():
        return False

    output={}
    senses=res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions=[]
    for sense in senses:
        definitions.append(f"👉🏻 {sense['definitions'][0]}")
    output['definitions']='\n'.join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio']=res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output

if __name__ == '__main__':
    from pprint import pprint as print
    print(get_definitons('Great Britain'))
    print(get_definitons('america'))







