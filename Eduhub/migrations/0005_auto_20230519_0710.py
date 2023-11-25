# Generated by Django 3.2.19 on 2023-05-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eduhub', '0004_auto_20230518_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('offer_dics', models.TextField(blank=True, default='', null=True)),
                ('offer_status', models.CharField(blank=True, default=0, max_length=10, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='courseinternship_details',
        ),
    ]
