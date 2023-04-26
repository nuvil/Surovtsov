from django.db import models
from django.contrib.auth.models import User

# Create your models here.
choice_of_status = [
    ('h', 'host'),
    ('g', 'guest'),
    ('n', 'noone')
]


class Users(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='имя', null=True)
    last_name = models.CharField(max_length=30, verbose_name='фамилия', null=True)
    age = models.IntegerField(verbose_name='возраст', null=True)
    photo = models.ImageField(default='default.jpg', upload_to='user_photo', blank=False)
    email = models.CharField(max_length=50, verbose_name='почта', null=True)
    address = models.CharField(max_length=100, verbose_name='адрес', null=True)
    status = models.CharField(max_length=1, choices=choice_of_status, default='n', verbose_name='статус')
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    hobbies = models.ManyToManyField('Hobbies')

    def __str__(self):
        return f"{self.first_name}"

    class Meta:
        ordering = ['first_name']
        verbose_name_plural = "Пользователи"


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


class User_rating(models.Model):
    user_rating = models.PositiveIntegerField(verbose_name='рейтинг пользователя', null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user_rating}"


class Meetings(models.Model):
    meeting_name = models.CharField(max_length=200, verbose_name='названиие встречи')
    meeting_description = models.CharField(max_length=300, verbose_name="описание встречи", null=True)
    date_meeting = models.DateField(verbose_name="Дата встречи", null=True)
    time_meeting = models.TimeField(verbose_name='Время встречи', null=True)
    user = models.ManyToManyField(Users)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.meeting_name}"

    class Meta:
        verbose_name_plural = "Встречи"


class Meetings_rating(models.Model):
    meetings_rating = models.PositiveIntegerField(verbose_name='рейтинг встречи', null=True)
    meetings = models.ForeignKey(Meetings, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.meetings_rating}"


class Hobbies(models.Model):
    name = models.CharField(max_length=30, verbose_name='хобби', null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Хобби"


class Place(models.Model):
    place_name = models.CharField(max_length=100, verbose_name='название')
    address = models.CharField(max_length=100, verbose_name='адрес')
    place_site = models.URLField(max_length=50, verbose_name='сайт заведения', null=True)
    place_phone = models.CharField(max_length=20, verbose_name='телефон')
    place_photo = models.ImageField(upload_to='place_photo', null=True, blank=True)

    def __str__(self):
        return f"{self.place_name}"

    class Meta:
        verbose_name_plural = "Заведения"


class Restaurant(Place):
    average_paycheck = models.FloatField(verbose_name='средний чек(BYN)', null=True)
    description = models.CharField(max_length=400, verbose_name="описание заведения", null=True)

    def __str__(self):
        return f"{self.place_name}"

    class Meta:
        verbose_name_plural = "Ресторан"


class Bar(Place):
    average_paycheck = models.FloatField(verbose_name='средний чек(BYN)', null=True)
    description = models.CharField(max_length=400, verbose_name="описание заведения", null=True)

    def __str__(self):
        return f"{self.place_name}"

    class Meta:
        verbose_name_plural = "Бар"


class Cafe(Place):
    average_paycheck = models.FloatField(verbose_name='средний чек(BYN)', null=True)
    description = models.CharField(max_length=400, verbose_name="описание заведения", null=True)

    def __str__(self):
        return f"{self.place_name}"

    class Meta:
        verbose_name_plural = "Кафе"


class Place_rating(models.Model):
    place_rating = models.PositiveIntegerField(verbose_name='рейтинг заведения', null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.place_rating}"

    class Meta:
        abstract = True


class Rating(Place_rating, User_rating, Meetings_rating):
    comment = models.CharField(max_length=300, verbose_name='комментарий', null=True)

    def __str__(self):
        return f"{self.comment}"

    class Meta:
        verbose_name_plural = "Рейтинг"
