# Generated by Django 2.2.4 on 2019-08-29 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0010_auto_20190828_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='quickstart.Student')),
                ('grade', models.CharField(choices=[('A', 'a'), ('B', 'b'), ('C', 'c')], default='A', max_length=10)),
                ('total_marks', models.IntegerField(default=0)),
                ('percentage', models.FloatField(default=0)),
                ('remarks', models.CharField(max_length=50)),
                ('subjects', models.ManyToManyField(to='quickstart.Subject')),
            ],
        ),
    ]
