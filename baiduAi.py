from urllib import request
from urllib import parse
import sys,json,ssl,urllib,base64

# client_id 为官网获取的AK， client_secret 为官网获取的SK
appKey = 'g7MzRi4sV1TBFD8C9hWGfhgP'
appSecretKey = 'Y6u359W9NxbybH3BrL4S5qHIZzIl24Pl'
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

def getResult(urlName,data = {},path = ''):
    #print(data)
    res = ''
    host = 'https://aip.baidubce.com/rest/2.0/ocr/v1/'+urlName+'?access_token=' + access_token
    if path != '':
        try:
            f = open(path, 'rb')
            img = base64.b64encode(f.read())
        except BaseException as e:
            print(e)

        # 参数image：图像base64编码
        image = {'image': img}
        data = dict(image,**data)
    #print(data)
    data = urllib.parse.urlencode(data)
    data = bytes(data, 'utf8')
    try:
        req = request.Request(host, data)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')

        f = request.urlopen(req)
        print('Status:', f.status, f.reason)
        res = json.loads(f.read().decode('utf-8'))
    except BaseException as e:
        print('异常了',e)
    return res

urlName= 'webimage'
path = 'd:/car.jpg'
data = {"url": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1537970010891&di=56766ae408f2181248689bb8ef20d72f&imgtype=0&src=http%3A%2F%2Fdik.img.lgdsy.com%2Fpic%2F20%2F13625%2Fae7a987f6be8481a.jpg"}
# print(getResult(urlName,{},path))
#
# print(getResult(urlName,{'url':'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1538039153719&di=c658d4b63bf880c2430b827139becb79&imgtype=0&src=http%3A%2F%2Fn6.cmsfile.pg0.cn%2Fgroup2%2FM00%2FA1%2FE7%2FCgqg2lg1U2mAe_QKAADH8lDg0Fw408.jpg'}))
# print(getResult('license_plate',{},'d:/2.jpg'))
# print(getResult('license_plate',{},'d:/3.jpg'))
# print(getResult('license_plate',{},'d:/408.jpg'))
# print(getResult('license_plate',{},'d:/5.jpg'))

print(getResult('idcard',{'id_card_side':'front'},'c:/Users/zhuangchenglong/Desktop/zcl.jpg'))
print(getResult('idcard',{'id_card_side':'back'},'d:/id2.jpg'))
print(getResult('vehicle_license',{},'d:/jiazhao.jpg'))



