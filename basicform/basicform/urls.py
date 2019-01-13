from django.conf.urls import url,include
from django.contrib import admin
from basicapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url('admin/', admin.site.urls),
    url(r'^formpage/',views.form_name_view,name='form_name'),
]
