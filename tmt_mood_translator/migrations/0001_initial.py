# Generated by Django 3.2.8 on 2021-10-31 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=500)),
                ('translation', models.CharField(max_length=1000)),
                ('positivity', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]
