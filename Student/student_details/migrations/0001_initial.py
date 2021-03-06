# Generated by Django 3.2.5 on 2021-07-13 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('percentage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile_no', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='None', max_length=1)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('address', models.TextField()),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_details.education')),
            ],
        ),
    ]
