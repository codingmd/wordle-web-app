from django.contrib import admin

# Register your models here.
from .models import User
from wordle.models import Wordle

# set up automated slug creation
class UserAdmin(admin.ModelAdmin):
    pass

class WordleAdmin(admin.ModelAdmin):
    model = Wordle
    list_display = ('name', 'description', 'word', 'score', 'board',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Wordle, WordleAdmin)