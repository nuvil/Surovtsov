# Generated by Django 4.1.6 on 2023-04-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_users_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(null=True, verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=30, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=30, null=True, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='user_photo'),
        ),
    ]
