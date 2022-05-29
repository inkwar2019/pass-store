from pyexpat import model
from django.db import models
from django.urls import reverse


class Password(models.Model):
    title = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.BooleanField(default=False, blank=True)

    def get_absolute_url(self):
        return reverse("password-details", kwargs={"pk": self.pk})

    def get_success_url(self, **kwargs):
        return reverse("password-details", kwargs={'pk': self.object.pk})

    def __str__(self):
        return self.title
