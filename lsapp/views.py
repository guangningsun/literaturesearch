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



def dashboard(request):
    user_count = 1
    task_count = 2

    context = { 'user_count': user_count, 'task_count': task_count }
    return render(request, 'dashboard.html',context)


