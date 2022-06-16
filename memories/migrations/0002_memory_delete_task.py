# Generated by Django 4.0.5 on 2022-06-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='Название места')),
                ('comments', models.TextField(verbose_name='Комментарий')),
                ('latitude', models.FloatField(null=True, verbose_name='Широта')),
                ('longitude', models.FloatField(null=True, verbose_name='Долгота')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]