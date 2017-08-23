"""This is a program for database"""
from django.db import models

# Create your models here.
class Chat(models.Model):
    """save text data"""
    class Meta:
        """meta info"""
        verbose_name = "data"
        verbose_name_plural = "data"
        ordering = ["-pub_date"]
    data_type = models.CharField(max_length=20)
    parent = models.CharField(max_length=20)
    pub_date = models.DateTimeField("date published")
    name_text = models.CharField(max_length=100)
    chat_text = models.CharField(max_length=200)

    def __str__(self):
        return self.chat_text

class Title(models.Model):
    class Meta:
        verbose_name = "data"
        ordering = ["-pub_date"]
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    default_name = models.CharField(max_length=20)
    pub_date = models.DateTimeField("date published")

class Tag(models.Model):
    class Meta:
        verbose_name = "data"
        ordering = ["-pub_date"]
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")

