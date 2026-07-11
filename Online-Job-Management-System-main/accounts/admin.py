from django.contrib import admin
from accounts.models import User

class AdminUser(admin.ModelAdmin):
    items = ('username','role','gender','email','phone','skills','experience','education','location','interests','languages')
    
admin.site.register(User,AdminUser)

# Register your models here.
