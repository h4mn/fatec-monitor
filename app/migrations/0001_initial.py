# Generated by Django 4.2.2 on 2023-06-29 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.TextField(max_length=15)),
                ('descricao', models.TextField(max_length=50)),
                ('faltas', models.IntegerField()),
                ('frequencias', models.FloatField()),
                ('media', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField(max_length=50)),
                ('data', models.DateField()),
                ('nota', models.FloatField()),
                ('fk_disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
            ],
        ),
    ]
