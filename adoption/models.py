from django.db import models

# Create your models here.

class Animal(models.Model):
	# attribute
	animal_name = models.CharField(max_length = 100, null=True, default="New Animal")
	DOG='D'
	CAT='C'
	ANIMAL_CHOICES = (
		(DOG, 'Dog'),
		(CAT, 'Cat'),
		)
	animal_type = models.CharField(max_length=1, blank=False, choices = ANIMAL_CHOICES)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	# function
	def is_cat(self):
		return self.animal_type in self.CAT

	def is_dog(self):
		return self.animal_type in self.DOG

	def __unicode__(self):
		return self.animal_name