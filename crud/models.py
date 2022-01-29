from django.db import models
from django.utils import timezone as tz
from django.contrib.auth.models import User

# Create your models here.

class NoteStatus(models.IntegerChoices):
    to_do = -1, "To Do"
    doing = 0, "Doing"
    done = 1, "Done"

class Note(models.Model):
    user = models.ForeignKey(User, related_name='notes',  on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=NoteStatus.choices, default=-1)
    date = models.DateField(default=tz.now)
    
    def __str__(self):
        return self.title



