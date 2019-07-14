from django.contrib import admin
from .models import Expenses
from .models import Catagory

# Register your models here.
admin.site.register(Expenses)
admin.site.register(Catagory)

