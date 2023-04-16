# -*- coding:UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
import datetime
from django.utils.html import format_html
from AppModel import *
from multiselectfield import MultiSelectField


class LiteratureInfo(models.Model):
    class_choice = [
        ("0", "工程技术"),
        ("1", "数学与统计"),
        ("2", "自然科学类"),
    ]
    subclass_choice =[
        ("0", "计算机科学类"),
        ("1", "建筑工程类"),
        ("2", "数学类"),
        ("3", "统计学类"),
        ("4", "物理学"),
        ("5", "化学"),
        ("6", "生物学"),
    ]
    literature_name = models.CharField(max_length=200,verbose_name='文献标题')
    literature_auth = models.CharField(max_length=200,verbose_name='文献作者')
    literature_date = models.DateField(verbose_name='文献日期',default=datetime.date.today)
    literature_perm = models.CharField(max_length=200,verbose_name='文献权限')
    literature_class = models.CharField(max_length=200,verbose_name='文献分类',choices=class_choice,default=0)
    literature_subclass = models.CharField(max_length=200,verbose_name='文献子类',choices=subclass_choice,default=0)
    is_permited = models.BooleanField(verbose_name='是否通过审批',default="False")
    doc_path = models.FileField(upload_to='uploads/',verbose_name='文献路径')
    upload_user = models.CharField(max_length=200,verbose_name='上传用户')
    


class UserInfo(models.Model):
    gender_choice = [
        ("0", "女"),
        ("1", "男"),
    ]
    nations = [
        ("0","汉族"),
        ("1","回族"),
        ("2","满族"),
    ]
    policy_roles = [
        ("0","党员"),
        ("1","团员"),
        ("2","群众"),
    ]
    user_name = models.CharField(max_length=200,verbose_name='用户名')
    nick_name = models.CharField(max_length=200,verbose_name='微信名')
    gender = models.CharField(max_length=20,verbose_name='性别', choices=gender_choice,default=1)
    nation = models.CharField(max_length=200,verbose_name='民族', choices=nations,default=0)
    policy_role = models.CharField(max_length=20,verbose_name='政治面貌', choices=policy_roles,default=2)
    household = models.CharField(max_length=200,verbose_name='户籍类型',default="非农业")
    is_bd = models.BooleanField(verbose_name='是否八大群体',default="True")
    job_status = models.BooleanField(verbose_name='就业状态',default="True")
    id_card = models.CharField(max_length=200,verbose_name='身份证号')
    phone_number = models.CharField(max_length=200,verbose_name='手机号码')
    mig_worker = models.BooleanField(verbose_name='是否农民工',default="True")
    company_name = models.CharField(max_length=200,verbose_name='单位名称')
    labour_union = models.CharField(max_length=200,verbose_name='所属工会')
    join_union = models.DateField(verbose_name='入会时间',default=datetime.date.today)
    weixin_openid = models.CharField(max_length=200,verbose_name='微信ID')
    pic_head = models.ImageField(u'头像',null=True, blank=True, upload_to='head_image')
    desc = models.CharField(max_length=200,verbose_name='备注',default='-')
    
    
    
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    
    def __str__(self):
        return self.user_name

