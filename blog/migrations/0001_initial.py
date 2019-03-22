# Generated by Django 2.1.7 on 2019-03-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('detail', models.TextField()),
            ],
        ),
    ]
