from django.db import models


# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.


class Subscribe(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)

    def __str__(self):
        return self.name + '|' + self.email
