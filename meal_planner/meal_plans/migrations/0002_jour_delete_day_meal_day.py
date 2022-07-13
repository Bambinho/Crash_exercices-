# Generated by Django 4.0.6 on 2022-07-12 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(default=True, max_length=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.AddField(
            model_name='meal',
            name='day',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='meal_plans.jour'),
        ),
    ]
