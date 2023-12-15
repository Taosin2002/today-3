from django.db import models

# Create your models here.
class Task(models.Model):
    task_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    assignDate=models.DateField()

    def __str__(self):
        return self.title
    