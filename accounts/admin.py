from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(profile)
admin.site.register(Cart)
admin.site.register(CartItem)