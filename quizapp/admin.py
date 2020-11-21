from django.contrib import admin
from .models import Mymodel
# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display = ['question','option1','option2','option3','option4','anwers']
admin.site.register(Mymodel,empadmin)
