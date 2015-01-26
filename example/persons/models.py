from django.db import models

class Person(models.Model):
    short_name = models.CharField(max_length=32, null=False, blank=False)
    full_name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(max_length=128, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.short_name, 
                          '(%s)' % self.full_name if self.full_name else '')
