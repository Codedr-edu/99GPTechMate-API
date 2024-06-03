from django.db import models

# Create your models here.


class ImageSaver(models.Model):
    image = models.ImageField(upload_to="/images/saved")


class DocumentSaver(models.Model):
    document = models.FileField(upload_to="document/saved")


class UniversitySaver(models.Model):
    document = models.FileField(upload_to="document/university")
