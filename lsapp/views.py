# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import viewsets, filters,permissions
from AppModel.serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from collections import OrderedDict
from AppModel.models import *
from django.db.models import Avg, Count, Min, Sum
import hashlib,urllib,random,logging,requests,base64
import json,time,django_filters,xlrd,uuid
from rest_framework import status
import time, datetime
import requests,configparser
from django.conf import settings
import qrcode,os
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
handler = logging.FileHandler("./lsapp.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


conf_dir = settings.CONF_DIR
cf = configparser.ConfigParser()
cf.read(conf_dir)
logger.info("成功加载配置文件 %s " % (conf_dir))

# 内部方法用于返回json消息
# done
def _generate_json_message(flag, message):
    if flag:
        return HttpResponse("{\"error\":0,\"msg\":\""+message+"\"}",
                            content_type='application/json',
                            )
    else:
        return HttpResponse("{\"error\":1,\"msg\":\""+message+"\"}",
                            content_type='application/json',
                            )
@api_view(['GET'])
def get_qrcode(request):
    if request.method == 'GET':
        return render(request, "qrcode.html")                 



# weixin 获取用户信息
@api_view(['POST'])
def weixin_gusi(request):
    if request.method == 'POST':
        appId = cf.get("WEIXIN", "weixin_appid")
        openid = request.POST['openid']
        try:
            sessionKey = WeixinSessionKey.objects.get(weixin_openid=openid).weixin_sessionkey
            encryptedData = request.POST['encryptedData']
            iv = request.POST['iv']
            pc = WXBizDataCrypt(appId, sessionKey)
            res_data = pc.decrypt(encryptedData, iv)
            phone_number = res_data["phoneNumber"]
            res_data["is_exist"] = "0" #不存在
            # 增加创建用户动作 openid phonenumber nickname
            try:
                # 用户登录时判断用户是否存在
                # userinfo = UserInfo.objects.get(weixin_openid=openid)
                userinfo = UserInfo.objects.get(weixin_openid=openid)
                res_data["is_exist"] = "1"
                return HttpResponse(json.dumps(res_data),content_type='application/json')
            except :
                try:
                    ui = UserInfo.objects.get(phone_number=phone_number)
                    ui.weixin_openid=openid
                    ui.save()
                    res_data["is_exist"] = "1"
                    return HttpResponse(json.dumps(res_data),content_type='application/json')
                except:
                    res_data["is_exist"] = "0"
                    return HttpResponse(json.dumps(res_data),content_type='application/json')
        except:
            return HttpResponse(json.dumps("{\"error\":1}"),content_type='application/json')


def __weixin_send_message(touser,date3,thing6,phrase1):
    # get access token
    APPID = cf.get("WEIXIN", "weixin_appid")
    SECRET = cf.get("WEIXIN", "weixin_secret")
    get_access_token_request_data = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+APPID+"&secret="+SECRET+""
    req_access = requests.get(get_access_token_request_data)
    access_token = json.loads(req_access.content)['access_token']
    body = {
            "access_token":access_token,
            "touser": touser,
            "template_id": cf.get("WEIXIN", "weixin_template_id"),
            "miniprogram_state": cf.get("WEIXIN", "miniprogram_state"),
            "data":{
                "date3": {
                    "value": date3
                },
                "thing6":{
                    "value": thing6
                },
                "phrase1":{
                    "value": phrase1
                }
            }

    }
    requst_data = "https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token="+access_token+""
    response = requests.post(requst_data, data = json.dumps(body))
    logger.info("通知用户 %s  内容为 %s  微信服务器返回结果为 %s" % (touser, json.dumps(body),response.content))
    return 0
