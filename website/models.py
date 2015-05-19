from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rating = models.FloatField()

    def __str__(self):
        return "{} - {}".format(self.name, self.rating)

    def __hash__(self):
        return hash(self.__str__())


class Projection(models.Model):
    movie_id = models.ForeignKey(Movie)
    proj_type = models.CharField(max_length=20)
    date = models.DateField()
    time = models.DateTimeField()

    def __str__(self):
        return "{} - {} - {}".format(self.movie_id.name, self.proj_type, self.time.time())

    def __hash__(self):
        return hash(self.__str__())


class Reservation(models.Model):
    username = models.CharField(max_length=100, unique=True)
    projection_id = models.ForeignKey(Projection)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{} - {} - row:{} - col:{}".format(self.username, self.projection_id.time, self.row, self.col)
