
import urequests as requests
import ujson as json

def getTime():
    url = 'http://worldtimeapi.org/api/timezone/Asia/Ho_Chi_Minh'
    response = requests.get(url)
    data = json.loads(response.text)
    datetime = data['datetime']
    time = dict() 
    time['year'] = datetime[0:4]
    time['month'] = datetime[5:7]
    time['day'] = datetime[8:10]
    time['hour'] = datetime[11:13]
    time['minute'] = datetime[14:16]
    time['second'] = datetime[17:19]
    
    return time