from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Timing
from .models import Ticket

admin.site.register(Timing)
admin.site.register(Ticket)
admin.site.unregister(Group) 