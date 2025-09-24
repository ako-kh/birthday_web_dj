from django.db import models
from django.urls import reverse


class BirthdayModel(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    gift_idea = models.TextField(max_length=120, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('bdays:bday-list')

    def __str__(self):
        return self.name