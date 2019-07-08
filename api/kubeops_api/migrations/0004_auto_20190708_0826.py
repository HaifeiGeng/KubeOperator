# Generated by Django 2.1.2 on 2019-07-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0003_auto_20190624_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='config_path',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='status',
            field=models.CharField(choices=[('RUNNING', 'running'), ('INSTALLING', 'installing'), ('DELETING', 'deleting'), ('READY', 'ready'), ('ERROR', 'error'), ('WARNING', 'warning')], default='READY', max_length=128),
        ),
    ]
