from django.contrib import admin
from .models import Member1

class MemberAdmin(admin.ModelAdmin):
    list_display="firstname","lastname"

admin.site.register(Member1,MemberAdmin)
# Register your models here.
