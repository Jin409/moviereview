# Generated by Django 4.0.1 on 2022-01-17 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='user/'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_introduce',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_repassword',
            field=models.CharField(max_length=30),
        ),
    ]
