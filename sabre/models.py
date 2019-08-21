from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class MyModelName(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    ...

    # Metadata
    class Meta:
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name


class UserAccount(models.Model):
    """
       A typical class defining a model, derived from the Model class.
       """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, default=None, blank=True, null=True, verbose_name=('Имя'))
    last_name = models.CharField(max_length=200, default=None, blank=True, null=True, verbose_name=('Фамилия'))
    email = models.EmailField(default=None, blank=True, null=True)

    class Meta:
        permissions = (('can_delete', 'can_create'),)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('account_view', kwargs={'user': self.user.username})