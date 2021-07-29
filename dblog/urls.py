#from django.conf.urls.defaults import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]

# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = patterns('',
#     (r'^simpleblog/$', 'dblog.blog.views,index'),
#     (r'^scripts/(?P<path>.*)$',
#     'django.views.static.serve',
#                                 {'document_root':'./scripts'}),
#     (r'^admin/', include('django.contrib.admin.urls')),
# )
