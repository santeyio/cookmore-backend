# Generated by Django 2.2.4 on 2019-09-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=100, null=True, unique=True)),
                ('first_name', models.CharField(max_length=100, null=True, unique=True)),
                ('last_name', models.CharField(max_length=100, null=True, unique=True)),
                ('date_joined', models.DateTimeField(null=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Is the user allowed to have access to the admin', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Is the user account currently active', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
