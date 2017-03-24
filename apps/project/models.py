from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MinLengthValidator
# Create your models here.


class Quote(models.Model):
    user = models.ForeignKey('auth.User')
    quoted_by = models.CharField(max_length=255, validators = [MinLengthValidator(4)])
    quote = models.TextField(validators = [MinLengthValidator(11)])
    created = models.DateTimeField( auto_now_add=True)
    favorites = models.ManyToManyField('auth.User', related_name='favorite_quotes')


    def get_absolute_url(self):
        return reverse('edit', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('delete', kwargs={'id': self.id})
