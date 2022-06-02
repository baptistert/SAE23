from django.contrib import admin
from .models import Machine
from .models import PC
from .models import Personne
# Register your models here.

admin.site.register(Machine)
admin.site.register(PC)
admin.site.register(Personne)