# Generated by Django 2.1 on 2019-07-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190626_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='SIG',
            field=models.CharField(max_length=2, null=True),
        ),
    ]