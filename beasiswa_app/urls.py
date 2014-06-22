from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beasiswa_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', TemplateView.as_view(template_name='base.html'), name="home"),
    url(r'^penerima-beasiswa/$', 'mahasiswa.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls'))
)
