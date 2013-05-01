from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
from datetime import datetime 

class ModelSave(models.Model):
    name = models.CharField(max_length = 100)
    action = models.CharField(max_length = 100)
    time = models.DateField()

@receiver(post_save)
def post_save_handler(sender, **kwargs):
    modelsave = ModelSave(name = sender.__name__, action = 'Save', time = datetime.now() )
    modelsave.save()

@receiver(post_delete)
def post_delete_handler(sender, **kwargs):
    modelsave = ModelSave(name = sender.__name__, action = 'Delete', time = datetime.now() )
    modelsave.save()