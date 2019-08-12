import requests
from urllib.request import urlopen

userName = input('Enter Pinterest Username:')
boardId = input('Enter Pinterest Board Name:')
try:
    response = requests.get(
        'https://api.pinterest.com/v3/pidgets/boards/' + userName+'/'+boardId+'/pins/')
    imageDatas = response.json()['data']['pins']
    for imageData in imageDatas:
        imageUrl = imageData['images']['564x']['url']
        imageDesc = imageData['description'][0:20]
        imageDesc = ''.join(
            e for e in imageDesc if e.isalnum())+imageData['id']
        extensions = imageUrl.split('.')
        extension = extensions[len(extensions)-1]
        f = open(str(imageDesc)+"."+extension, 'wb')
        f.write(urlopen(imageUrl).read())
        f.close()
except:
    print("Error in fetching pins from pinterest API")
