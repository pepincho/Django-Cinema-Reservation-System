from django.conf.urls import url, patterns


urlpatterns = patterns('website.views',
                       url(r'^$', 'index')

                       )
