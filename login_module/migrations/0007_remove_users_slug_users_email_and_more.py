# Generated by Django 4.0 on 2022-02-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_module', '0006_alter_users_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='slug',
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='email_verification_code',
            field=models.CharField(blank=True, max_length=72, null=True),
        ),
    ]
