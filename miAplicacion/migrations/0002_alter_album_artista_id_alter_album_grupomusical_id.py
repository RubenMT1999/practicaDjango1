# Generated by Django 4.0.4 on 2022-04-21 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artista_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.artista'),
        ),
        migrations.AlterField(
            model_name='album',
            name='grupoMusical_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='miAplicacion.grupo_musical'),
        ),
    ]
