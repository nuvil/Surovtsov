from django.db import models

# Create your models here.
status_choises = [
    ('h', 'host'),
    ('g', 'guest'),
    ('f', 'friend'),
    ('n', 'noone')
]


class Users(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=30, verbose_name='фамилия')
    age = models.IntegerField(verbose_name='возраст')
    email = models.CharField(max_length=50, verbose_name='почта')
    address = models.CharField(max_length=100, verbose_name='адрес')
    status = models.CharField(max_length=1, choices=status_choises, default='n', verbose_name='статус')
    hobbies = models.ManyToManyField('Hobbies')

    def __str__(self):
        return f"{self.first_name}"


class Host(Users):
    class Meta:
        proxy = True

    def hosts_status(self):
        self.status = 'h'
        return self.status

    def __str__(self):
        return f"{self.first_name}"


class Guest(Users):
    class Meta:
        proxy = True

    def guest_status(self):
        self.status = 'g'
        return self.status

    def __str__(self):
        return f"{self.first_name}"


class User_Ratings(models.Model):
    rating = models.PositiveIntegerField(verbose_name='рейтинг пользователя')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.rating}"


class Meetings(models.Model):
    meeting_name = models.CharField(max_length=200, verbose_name='название встречи')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.meeting_name}"


class Hobbies(models.Model):
    name = models.CharField(max_length=30, verbose_name='хобби')

    def __str__(self):
        return f"{self.name}"


class Place(models.Model):
    place_name = models.CharField(max_length=100, verbose_name='название')
    address = models.CharField(max_length=100, verbose_name='адрес')
    place_phone = models.CharField(max_length=20, verbose_name='телефон')

    def __str__(self):
        return f"{self.place_name}"


class Restaurant(Place):
    free_table = models.IntegerField(verbose_name='свободные места')
    average_paycheck = models.FloatField(verbose_name='средний чек')

    def __str__(self):
        return f"{self.place_name}"


class Bar(Place):
    free_table = models.IntegerField(verbose_name='свободные места')
    average_paycheck = models.FloatField( verbose_name='средний чек')

    def __str__(self):
        return f"{self.place_name}"


class Cafe(Place):
    free_table = models.IntegerField(verbose_name='свободные места')
    average_paycheck = models.FloatField(verbose_name='средний чек')

    def __str__(self):
        return f"{self.place_name}"


class Place_rating(models.Model):
    rating = models.PositiveIntegerField(verbose_name='рейтинг')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.rating}"


class Rating(Place_rating, User_Ratings):
    comment = models.CharField(max_length=100, verbose_name='комментарий')

    def __str__(self):
        return f"{self.rating}"
