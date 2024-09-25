from django.db import models

# Create your models here.

class MyModel(models.Model):
    user = models.CharField(max_length=100, blank=True, null=True)
    my_pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.user
    