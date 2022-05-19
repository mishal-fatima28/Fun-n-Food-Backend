from django.urls import path
from funnfoodapp import views

urlpatterns = [
	
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


]