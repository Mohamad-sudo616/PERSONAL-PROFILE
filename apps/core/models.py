from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()
    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.full_name
