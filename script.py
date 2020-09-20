import requests
import json

def loadInfo(dest, arr):
    url = 'http://transportapi.com/v3/uk/places.json?query='+dest+'&type=train_station&app_id=94b4eb84&app_key=da370c2118b13a91dcf4378e0c45648a'
    r = requests.get(url, allow_redirects=True)
    open('destInfo.json', 'wb').write(r.content)
    url = 'http://transportapi.com/v3/uk/places.json?query='+arr+'&type=train_station&app_id=94b4eb84&app_key=da370c2118b13a91dcf4378e0c45648a'
    r = requests.get(url, allow_redirects=True)
    open('arrInfo.json', 'wb').write(r.content)
    

def readJSON(type):
    if type == 'dest':
        with open('destInfo.json') as json_file:
            destInfoData = json.load(json_file)
            for p in destInfoData['member']:
                destName = p['name']
                deststation_code = p['station_code']
                desttiploc_code = p['tiploc_code']
                return destName, deststation_code, desttiploc_code
    else:
        with open('arrInfo.json') as json_file:
            arrInfoData = json.load(json_file)
            for p in arrInfoData['member']:
                arrName = p['name']
                arrstation_code = p['station_code']
                arrtiploc_code = p['tiploc_code']
                return arrName, arrstation_code, arrtiploc_code

def getTimetable(dest, arr):
    url = 'https://transportapi.com/v3/uk/train/station/'+readJSON('dest')[1]+'///timetable.json?app_id=94b4eb84&app_key=da370c2118b13a91dcf4378e0c45648a&calling_at='+readJSON('arr')[1]+'&train_status=passenger'
    r = requests.get(url, allow_redirects=True)
    open('timetableInfo.json', 'wb').write(r.content)
    """
    with open('destInfo.json') as json_file:
        destInfoData = json.load(json_file)
        for p in destInfoData['member']:
            destName = p['name']
            deststation_code = p['station_code']
            desttiploc_code = p['tiploc_code']
            return destName, deststation_code, desttiploc_code
    """


destination = input('Where do you want to go')
arrival = input('Where do you want to leave from')

getTimetable(destination,arrival)

loadInfo(destination,arrival)

#https://transportapi.com/v3/uk/train/station/LDS///timetable.json?app_id=94b4eb84&app_key=da370c2118b13a91dcf4378e0c45648a&calling_at=MNN&train_status=passenger

print(readJSON('arr')[1] + '-->' + readJSON('dest')[1])
