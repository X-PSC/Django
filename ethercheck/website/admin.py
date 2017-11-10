from django.contrib import admin

# Register your models here.

from website.models import Transaction

admin.site.register(Transaction)
