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

# 文献管理

@admin.register(LiteratureInfo)
class LiteratureInfoAdmin(ImportExportModelAdmin):
    list_display=['literature_name','literature_auth','literature_date','literature_perm','literature_class','literature_subclass','is_permited','doc_path']
    search_fields =('literature_name','literature_auth','literature_date','literature_perm','literature_class','literature_subclass','is_permited','doc_path')
    fieldsets = [
       ('用户数据', {'fields': ['literature_name','literature_auth','literature_date','literature_perm','literature_class','literature_subclass','is_permited','doc_path'], 'classes': ['']}),
    ]
    list_per_page = 15
    

admin.site.site_title = "科研文献管理系统1.0"
admin.site.site_header = "科研文献管理系统1.0"


