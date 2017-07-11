from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from myproject.core.views import taskanswer, TaskAnswerCreate


urlpatterns = [
    url(r'^taskanswer1/$', taskanswer, name='taskanswer1'),
    url(r'^taskanswer2/$', TaskAnswerCreate.as_view(), name='taskanswer2'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
