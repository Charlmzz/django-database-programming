# Generated by Django 4.0.1 on 2022-03-17 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('color_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sql.color')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sql.state')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False, verbose_name='player_id')),
                ('uniform_num', models.IntegerField(verbose_name='uniform_num')),
                ('first_name', models.CharField(max_length=256, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=256, verbose_name='last_name')),
                ('mpg', models.IntegerField(verbose_name='mpg')),
                ('ppg', models.IntegerField(verbose_name='ppg')),
                ('rpg', models.IntegerField(verbose_name='rpg')),
                ('apg', models.IntegerField(verbose_name='apg')),
                ('spg', models.FloatField(verbose_name='spg')),
                ('bpg', models.FloatField(verbose_name='bpg')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sql.team', verbose_name='team_id')),
            ],
        ),
    ]