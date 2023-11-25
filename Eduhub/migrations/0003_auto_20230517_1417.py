# Generated by Django 3.2.19 on 2023-05-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eduhub', '0002_courojt_details_courseinternship_details_courseojt_points_placements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('place', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('enq_msg', models.TextField(blank=True, default='', null=True)),
                ('enq_date', models.DateField(auto_now_add=True, null=True)),
                ('enq_status', models.CharField(blank=True, default='0', max_length=50, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='courseojt_points',
            new_name='courseojtPoints',
        ),
        migrations.RenameModel(
            old_name='enquiry',
            new_name='Enroll',
        ),
        migrations.RemoveField(
            model_name='course_description_list',
            name='course',
        ),
        migrations.DeleteModel(
            name='gallery',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
        migrations.DeleteModel(
            name='course_description_list',
        ),
    ]