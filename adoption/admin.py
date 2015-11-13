from django.contrib import admin

# Register your models here.
from .forms import AnimalForm
from .models import Animal

class AnimalAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "animal_type", "timestamp", "updated"]
	form = AnimalForm
	# class Meta:
	# 	model = Animal

admin.site.register(Animal, AnimalAdmin)