from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.full_name
