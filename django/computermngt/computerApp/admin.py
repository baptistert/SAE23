from django.contrib import admin
from .models import Equipement
from .models import Compte
from .models import Infrastructure
# Register your models here.


admin.site.index_title = "IT MANAGEMENT"
admin.site.site_url = "../computerApp/"


admin.site.register(Equipement)
admin.site.register(Compte)
admin.site.register(Infrastructure)