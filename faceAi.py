from urllib import request
from urllib import parse
import sys,json,ssl,urllib,base64

# client_id 为官网获取的AK， client_secret 为官网获取的SK
appKey = 'kZiCbFBX59Qx8uGQVnp5GfFy'
appSecretKey = 'zKRcdRYMoa6NLshwOqgAYisXDksUG91y'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+appKey+'&client_secret='+appSecretKey
req = request.Request(host)
req.add_header('Content-Type', 'application/json; charset=UTF-8')
with request.urlopen(req) as f:
    # print('Status:', f.status, f.reason)
    # for k, v in f.getheaders():
    #     print('%s: %s' % (k, v))
    res = json.loads(f.read().decode('utf-8'))

access_token = res['access_token']
print(access_token)

def getResult(urlName,data = {}):
    res = ''
    host = 'https://aip.baidubce.com/rest/2.0/face/v3/'+urlName+'?access_token=' + access_token
    path = 'd:/nv.jpg'
    if path != '':
        try:
            f = open(path, 'rb')
            img = base64.b64encode(f.read()).decode('ascii')
        except BaseException as e:
            print(e)

        # 参数image：图像base64编码
        #image = {'image': img}
    # print(img)
    # sys.exit()
    data = {"image":img,"image_type":"BASE64","face_field":"age,beauty,expression,face_shape,gender,glasses,landmark,race,quality,face_type"}
    data = urllib.parse.urlencode(data)
    data = bytes(data, 'utf8')
    try:
        req = request.Request(host, data)
        req.add_header('Content-Type', 'application/json')

        f = request.urlopen(req)
        print('Status:', f.status, f.reason)
        res = json.loads(f.read().decode('utf-8'))
    except BaseException as e:
        print('异常了',e)
    return res



print(getResult('detect'))



