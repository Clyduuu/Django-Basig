# Generated by Django 5.0 on 2023-12-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardGame', '0002_collection_pokemoncard_trainer_delete_basemodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemoncard',
            name='card_type',
            field=models.CharField(blank=True, choices=[('Fire', 'Fire'), ('Water', 'Water'), ('Grass', 'Grass'), ('Electric', 'Electric'), ('Psychic', 'Psychic'), ('Ice', 'Ice'), ('Dragon', 'Dragon'), ('Dark', 'Dark'), ('Normal', 'Normal'), ('Fighting', 'Fighting'), ('Flying', 'Flying'), ('Poison', 'Poison'), ('Ground', 'Ground'), ('Rock', 'Rock'), ('Bug', 'Bug'), ('Ghost', 'Ghost'), ('Steel', 'Steel'), ('Fairy', 'Fairy')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
