from django.contrib import admin
from .models import Cafe, Cake, ColdDrink
# Register your models here.
admin.site.register(Cafe)
admin.site.register(Cake)
admin.site.register(ColdDrink)

'''
Difference from abstract model:
Parent model (Cafe) as well as child models (Cake and ColdDrink) can be registered and can have their own tables'''