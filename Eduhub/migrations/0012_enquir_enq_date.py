# Generated by Django 4.1 on 2023-05-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eduhub', '0011_alter_enquir_enq_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquir',
            name='enq_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
