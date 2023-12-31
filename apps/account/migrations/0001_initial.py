# Generated by Django 4.2.4 on 2023-08-17 14:33

import apps.account.managers
import common.upload_to_file
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('last_name', models.CharField(blank=True, max_length=40, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=40, verbose_name='Имя')),
                ('sur_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('avatar', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=common.upload_to_file.user_avatar, verbose_name='Обложка')),
                ('user_type', models.CharField(choices=[('student', 'Студент'), ('teacher', 'Преподаватель'), ('admin', 'Администратор'), ('director', 'Директор'), ('super_admin', 'Супер администратор')], default='student', max_length=40, verbose_name='Пользователь является:')),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'User',
            },
            managers=[
                ('objects', apps.account.managers.UserManager()),
            ],
        ),
    ]
