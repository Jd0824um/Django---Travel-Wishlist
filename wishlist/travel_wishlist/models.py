from django.db import models

# Create your models here.


class Place(models.Model): ##Creates a database model that has 2 fields. Name and Boolean visited
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return '%s visited? %s' % (self.name, self.visited)
