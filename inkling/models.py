from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=250, default='Untitled')
    
    def __str__(self):
        return self.name

class Document(models.Model):
    title = models.CharField(max_length=250)
    project= models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    content = models.CharField(default = '')

    def __str__(self):
        return self.title
