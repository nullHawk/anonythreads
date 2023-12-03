from django.contrib import admin
from .models import Confession

class ConfessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'pub_date', 'content', 'likes', 'dislikes','subject')  # Add relevant fields here

admin.site.register(Confession, ConfessionAdmin)