# Generated by Django 4.1.5 on 2023-01-29 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_latecomer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='face_encoding',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user', to='users.userencoding'),
        ),
    ]