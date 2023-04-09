# -*- coding:UTF-8 -*-
from django.contrib import admin
from AppModel.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
import logging,json,datetime
from django.utils.html import format_html
from django import forms
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
from django.utils.html import format_html,escape, mark_safe
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import time
import decimal
from datetime import datetime
import os,qrcode
from import_export.tmp_storages import CacheStorage
from  .resource import UserInfoResource


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
handler = logging.FileHandler("./lsapp.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


# 用户管理
@admin.register(UserInfo)
class UserInfoAdmin(ImportExportModelAdmin):
    tmp_storage_class = CacheStorage
    resource_class = UserInfoResource
    list_display=['user_name','weixin_openid','nick_name','gender','nation','policy_role','household','is_bd','job_status','id_card','phone_number','mig_worker','company_name','labour_union','join_union','pic_head','desc']
    search_fields =('user_name','weixin_openid','nick_name','gender','nation','policy_role','household','is_bd','job_status','id_card','phone_number','mig_worker','company_name','labour_union','join_union','pic_head','desc')
    fieldsets = [
       ('用户数据', {'fields': ['user_name','gender','nation','policy_role','household','is_bd','job_status','id_card','phone_number','mig_worker','company_name','labour_union','join_union','pic_head','desc'], 'classes': ['']}),
    ]
    list_per_page = 15



admin.site.site_title = "科研文献管理系统1.0"
admin.site.site_header = "科研文献管理系统1.0"


