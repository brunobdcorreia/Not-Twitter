# Generated by Django 4.0.4 on 2022-05-26 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NotTwitter', '0002_profile_delete_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotATweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='NotTweets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]