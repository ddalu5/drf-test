from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = str(self.name).lower().strip()
