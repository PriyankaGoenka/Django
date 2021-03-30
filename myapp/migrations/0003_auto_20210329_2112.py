# Generated by Django 2.2.5 on 2021-03-30 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_python_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.Python'),
        ),
    ]