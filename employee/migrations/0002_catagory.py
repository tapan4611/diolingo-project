# Generated by Django 4.1 on 2022-09-13 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=20)),
                ('cname', models.CharField(max_length=20)),
                ('cdescription', models.CharField(max_length=50)),
            ],
        ),
    ]
