# Generated by Django 2.2.10 on 2021-11-09 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('question_type', models.IntegerField(choices=[(1, 'Plain Text'), (2, 'Single Choice'), (3, 'Multiple Choices')])),
                ('choices', models.ManyToManyField(blank=True, to='api.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('questions', models.ManyToManyField(blank=True, to='api.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('text', models.CharField(max_length=255)),
                ('choices', models.ManyToManyField(blank=True, to='api.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question')),
            ],
        ),
    ]
