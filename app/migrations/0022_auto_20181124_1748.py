# Generated by Django 2.0.3 on 2018-11-24 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20180726_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('view_project', 'Can view project'), ('download_project', 'Can download project'))},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('view_task', 'Can view task'), ('download_task', 'Can download task'))},
        ),
    ]
