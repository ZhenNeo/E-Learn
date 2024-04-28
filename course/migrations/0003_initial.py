# Generated by Django 4.2.7 on 2024-04-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0002_remove_course_students_remove_questionpaper_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.CharField(choices=[('Tech Courses', 'Tech Courses'), ('CBSE Courses', 'CBSE Courses')], default='Tech Courses', max_length=100)),
                ('grade', models.CharField(blank=True, max_length=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='staticfiles/course_images/')),
            ],
        ),
    ]
