from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from .models import Ticket
from .models import Timing




# Create your views here.

def index(request):

    timings = Timing.objects.all()
    
    return render(request, 'index.html', {'timings': timings})

def contact(request):

    timings = Timing.objects.all()
    
    return render(request, 'contact.html', {'timings': timings})

def contact_form(request):

    if request.method == 'POST':
       
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        to_email = 'info@funnfoodparks.com'

        data = {

            'name' : name,
            'email' : email,
            'phone' : phone,
            'subject' : subject,
            'message' : message,

        }

        message = '''

        Name: {}

        Email: {}

        Phone: {}

        Message: {}


        '''.format(data['name'], data['email'], data['phone'], data['message'])

        print('message')
        
        send_mail(data['subject'], message, '', [to_email] )
        return render(request, 'thanks.html')

def park_timings(request):

    timings = Timing.objects.all()
    
    return render(request, 'park-timings.html', {'timings': timings})

def water_park(request):

    timings = Timing.objects.all()
    
    return render(request, 'water-park.html', {'timings': timings})

def entry_tickets(request):

    tickets = Ticket.objects.all()
    timings = Timing.objects.all()

    
    return render(request, 'entry-tickets.html', {'ticket': tickets ,'timings': timings})

def coming_soon(request):
    
    return render(request, 'coming-soon.html')

def gallery(request):

    timings = Timing.objects.all()
    
    return render(request, 'gallery.html', {'timings': timings})

def thanks(request):
    
    return render(request, 'thanks.html')


# Create your views here.
