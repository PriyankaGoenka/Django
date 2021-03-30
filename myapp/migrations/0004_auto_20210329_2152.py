# Generated by Django 2.2.5 on 2021-03-30 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210329_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.Python'),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.Place')),
                ('italian', models.BooleanField(default=False)),
                ('chinese', models.BooleanField(default=False)),
            ],
            bases=('myapp.place',),
        ),
    ]
