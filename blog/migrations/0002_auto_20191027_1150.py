# Generated by Django 2.2.6 on 2019-10-27 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BloggerInfo'),
        ),
    ]
