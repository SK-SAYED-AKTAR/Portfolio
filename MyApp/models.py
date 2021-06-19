from django.db import models
import datetime
# Create your models here.

class ProjectTable(models.Model):
    date = models.DateTimeField(auto_created=True, default=datetime.datetime.now())
    clientName = models.CharField(max_length=150)
    projectName = models.CharField(max_length=150)
    Skill = models.CharField(max_length=150)
    projectDesc = models.CharField(max_length=500)

    def __str__(self):
        return str(str(self.clientName)+"  =>  "+str(self.projectName))

