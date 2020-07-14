# Generated by Django 3.0.7 on 2020-06-23 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, unique=True)),
                ('category', models.CharField(max_length=200, null=True)),
                ('supervisor', models.CharField(choices=[('Anand Kumar Shah', 'Anand Kumar Shah'), ('Basanta Joshi', 'Basanta Joshi'), ('Daya Sagar Baral', 'Daya Sagar Baral'), ('Dibakar Pant', 'Dibakar Pant'), ('Dinesh Kumar Sharma', 'Dinesh Kumar Sharma'), ('Jitendra Kumar Manadhar', 'Jitendra Kumar Manadhar'), ('Nanda Bikram Adhikari', 'Nanda Bikram Adhikari'), ('Ram Krishna Maharjan', 'Ram Krishna Maharjan'), ('Ranju Kumar Shiwakoti', 'Ranju Kumar Shiwakoti'), ('Sanjeeb Prasad Panday', 'Sanjeeb Prasad Panday'), ('Subarna Shakya', 'Subarna Shakya'), ('Surendra Shrestha', 'Surendra Shrestha')], max_length=200, null=True)),
            ],
            options={
                'unique_together': {('title', 'category', 'supervisor')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('batch', models.CharField(max_length=200, null=True)),
                ('program', models.CharField(choices=[('BEX', 'BEX'), ('BEX', 'BCT')], max_length=200, null=True)),
                ('roll_number', models.CharField(max_length=200, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dbprojects.Project')),
            ],
            options={
                'unique_together': {('name', 'project')},
            },
        ),
    ]
