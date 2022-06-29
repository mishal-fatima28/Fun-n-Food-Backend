"""funnfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from funnfoodapp import views
from django.views.static import serve

from django.conf import settings

urlpatterns = [
	
	path('', views.index,name='index'),
	path('admin/', admin.site.urls),
    path('index/',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('park-timings/',views.park_timings, name='park-timings'),
    path('water-park/',views.water_park, name='water-park'),
    path('entry-tickets/',views.entry_tickets, name='entry-tickets'),
    path('coming-soon/',views.coming_soon, name='coming-soon'),
    path('book-online/',views.book_online, name='book-online'),
    path('gallery/',views.gallery, name='gallery'),
    path('contactsub/',views.contact_form, name='contactsub'),
    path('bookingsub/',views.booking_form, name='bookingsub'),
    path('thanks/',views.thanks, name='thanks'),
    path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

