from django.contrib import admin
from .models import *



admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssuedBook)

admin.site.site_header  =  "Library Managment"  
admin.site.site_title  =  "Library Managment Admin Panel"
admin.site.index_title  =  "Admin Panel"
