# Generated by Django 5.0.7 on 2024-08-06 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='subtask',
            options={'ordering': ['-created_at'], 'verbose_name': 'SubTask'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at'], 'verbose_name': 'Task'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('in_progress', 'In progress'), ('pending', 'Pending'), ('blocked', 'Blocked'), ('done', 'Done')], default='new', max_length=20),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='myapp.task'),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='categories',
            field=models.ManyToManyField(related_name='tasks', to='myapp.category'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('in_progress', 'In progress'), ('pending', 'Pending'), ('blocked', 'Blocked'), ('done', 'Done')], default='new', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name',)},
        ),
        migrations.AlterUniqueTogether(
            name='subtask',
            unique_together={('title',)},
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('title', 'deadline')},
        ),
        migrations.AlterModelTable(
            name='category',
            table='task_manager_category',
        ),
        migrations.AlterModelTable(
            name='subtask',
            table='task_manager_subtask',
        ),
        migrations.AlterModelTable(
            name='task',
            table='task_manager_task',
        ),
    ]