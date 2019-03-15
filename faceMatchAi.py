from urllib import request
from urllib import parse
import sys,json,ssl,urllib,base64
# try:
#     request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1541991500&di=ac572baf493d7814e69ca3038138cd17&imgtype=jpg&er=1&src=http%3A%2F%2Ff.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2Feac4b74543a982267a3d54978a82b9014b90eb86.jpg'
#                     ,'d:/scenery.jpg')
# except Exception as e:
#     print('下载图片异常', e)
# client_id 为官网获取的AK， client_secret 为官网获取的SK
appKey = 'kZiCbFBX59Qx8uGQVnp5GfFy'
appSecretKey = 'zKRcdRYMoa6NLshwOqgAYisXDksUG91y'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+appKey+'&client_secret='+appSecretKey
req = request.Request(host)
req.add_header('Content-Type', 'application/json; charset=UTF-8')
with request.urlopen(req) as f:
    res = json.loads(f.read().decode('utf-8'))

access_token = res['access_token']
print(access_token)

def getResult(urlName):
    res = ''
    host = 'https://aip.baidubce.com/rest/2.0/face/v3/'+urlName+'?access_token=' + access_token
    image1 = getBase64('d:/jd.jpg')
    image2 = getBase64('d:/zcl1.jpg')
    data = [{"image": image1, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},{"image": image2, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"}]
    data = json.dumps(data)
    #data = urllib.parse.urlencode(data)
    data = bytes(data, 'utf8')
    # print(data)
    # print(json.dumps(data))
    # sys.exit()
    try:
        req = request.Request(host, data)
        req.add_header('Content-Type', 'application/json')

        f = request.urlopen(req)
        print('Status:', f.status, f.reason)
        res = json.loads(f.read().decode('utf-8'))
    except BaseException as e:
        print('异常了',e)
    return res
def getBase64(path):
    try:
        f = open(path, 'rb')
        image = base64.b64encode(f.read()).decode('ascii')
    except BaseException as e:
        print(e)
    return image

print(getResult('match'))



