# Generated by Django 2.2.7 on 2019-12-03 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API_torneo', '0003_auto_20191124_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('imagen', models.ImageField(blank=True, upload_to='Entrenador')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API_torneo.Equipo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='TipoAmonestaciones',
        ),
    ]
