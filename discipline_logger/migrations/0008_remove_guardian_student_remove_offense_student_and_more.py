# Generated by Django 4.1.3 on 2022-12-20 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discipline_logger', '0007_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian',
            name='student',
        ),
        migrations.RemoveField(
            model_name='offense',
            name='student',
        ),
        migrations.DeleteModel(
            name='Action',
        ),
        migrations.DeleteModel(
            name='Guardian',
        ),
        migrations.DeleteModel(
            name='Offense',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
