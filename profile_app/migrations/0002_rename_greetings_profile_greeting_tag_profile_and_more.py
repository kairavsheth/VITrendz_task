# Generated by Django 4.1.4 on 2023-01-01 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='greetings',
            new_name='greeting',
        ),
        migrations.AddField(
            model_name='tag',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='profile_app.profile'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tag_Profile',
        ),
    ]
