# Generated by Django 3.2.5 on 2021-09-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sector', models.CharField(choices=[('Industrial', 'Industrial'), ('Medical', 'medical'), ('agricultural', 'agricultural'), ('┘ĆEducation', 'Education')], default=None, max_length=40)),
                ('description', models.TextField()),
                ('fund', models.CharField(max_length=100)),
            ],
        ),
    ]
