from django.contrib import admin
from .models import stories, paintforcar, categories, mobile_phone
# Register your models here.

admin.site.register(stories)
admin.site.register(paintforcar)
admin.site.register(categories)
admin.site.register(mobile_phone)