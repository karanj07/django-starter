from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.


class School(models.Model):
	name = models.CharField(max_length=200)
	featured_image = models.ImageField(null=True, blank=True, upload_to="schools/")
	description = RichTextField()
	address = models.CharField(max_length=500)
	summary = RichTextField(default="", blank=True) # blank=true - field is not required
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
#	price = models.IntegerField(default=0)
#	offer = models.BooleanField(default=False)