


def getSource():
    url = 'https://my-json-server.typicode.com/KhangHoang12/GIoT-Firmware/firmware'
    response = requests.get(url)
    data = json.loads(response.text)
    exec(data['source'])