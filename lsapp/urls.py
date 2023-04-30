from django.contrib import admin
from lsapp import views
from django.conf.urls import include, url
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from AppModel import admin as appadmin
from django.views.generic.base import RedirectView

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from social_django.urls import (
    urlpatterns as social_django_urls,
    )
# from django.conf.urls import url, include
# from django.contrib.auth.decorators import login_required
# from django.views.generic import TemplateView

# from simpleui_auth.urls import (
#     urlpatterns as simpleui_auth_urls,
#     )

urlpatterns = [
    url('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.+)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^comments/', include('django_comments.urls')),
    path('tasks/dashboard/', views.dashboard, name='dashboard'),
    url(r'^social-auth/', include(social_django_urls)),
    url(r'^restricted/', login_required(TemplateView.as_view(template_name='restricted.html'))),
    # url(r'^simpleui_auth/', include(simpleui_auth_urls)),
    # url(r'^restricted/', login_required(TemplateView.as_view(template_name='restricted.html'))),
    

] 
 
