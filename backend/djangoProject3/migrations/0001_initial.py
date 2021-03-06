from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePlayer', models.CharField(max_length=50)),
                ('nameTeam', models.CharField(max_length=50)),
                ('nameLeague', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('year', models.PositiveIntegerField()),
                ('valuePlayer', models.BigIntegerField()),
                ('role', models.CharField(max_length=100)),
                ('games', models.PositiveIntegerField()),
                ('goals', models.PositiveIntegerField()),
                ('assists', models.PositiveIntegerField()),
                ('minutes', models.PositiveIntegerField()),
                ('goalsConceded', models.PositiveIntegerField()),
                ('cleanSheets', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameTeam', models.CharField(max_length=50)),
                ('nameLeague', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('avgAge', models.FloatField()),
                ('valueTeam', models.BigIntegerField()),
                ('numberPlayers', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),

    ]
