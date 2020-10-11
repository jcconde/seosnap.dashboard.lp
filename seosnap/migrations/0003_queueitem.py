# Generated by Django 3.0.2 on 2020-02-02 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seosnap', '0002_website_cache_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueueItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('unscheduled', 'Unscheduled'), ('scheduled', 'Scheduled'), ('completed', 'completed'), ('failed', 'Failed')], default='unscheduled', max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queue_items', to='seosnap.Page')),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queue_items', to='seosnap.Website')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]