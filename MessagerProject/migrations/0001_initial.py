# Generated by Django 4.2.1 on 2023-06-03 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Сorrespondence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('users', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('correspondence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MessagerProject.сorrespondence')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MessagerProject.user')),
            ],
        ),
    ]
