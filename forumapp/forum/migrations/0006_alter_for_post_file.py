# Generated by Django 3.2.10 on 2022-04-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_for_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='for_post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='user/files/'),
        ),
    ]
