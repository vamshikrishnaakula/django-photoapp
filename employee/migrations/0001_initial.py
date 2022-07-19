# Generated by Django 3.2.14 on 2022-07-14 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('Rollno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('FatherName', models.EmailField(blank=True, db_column='FatherName', max_length=20, null=True)),
                ('Gender', models.CharField(blank=True, db_column='Gender', max_length=20, null=True)),
                ('DOB', models.CharField(blank=True, db_column='DOB', max_length=20, null=True)),
                ('BIB', models.CharField(blank=True, db_column='BIB', max_length=20, null=True)),
                ('chipcode1', models.CharField(blank=True, db_column='chipcode1', max_length=20, null=True)),
                ('chipcode2', models.CharField(blank=True, db_column='chipcode2', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Applicants',
            },
        ),
    ]
