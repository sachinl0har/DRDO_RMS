from django.contrib import admin

# Register your models here.

from .models import Room, User, BookUser

admin.site.register(User)
admin.site.register(Room)
admin.site.register(BookUser)

admin.site.site_header = 'DRDO Resourse Management System Admin Portal'
