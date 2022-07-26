# Generated by Django 4.0.6 on 2022-07-21 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicar', '0002_horario_agenda'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together={('medico', 'dia')},
        ),
        migrations.AddField(
            model_name='horario',
            name='agenda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='medicar.agenda'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='horario',
            unique_together={('agenda', 'horario')},
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='horarios',
        ),
    ]
