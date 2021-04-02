# Generated by Django 3.1.7 on 2021-04-02 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('seen', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('N', 'Night')], default='M', max_length=1)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.anime')),
            ],
        ),
    ]
