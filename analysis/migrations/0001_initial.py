# Generated by Django 5.1.7 on 2025-03-08 07:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiabetesSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('bmi', models.FloatField()),
                ('activity_level', models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')], max_length=10)),
                ('frequent_urination', models.PositiveIntegerField(choices=[(1, 'No'), (5, 'Sometimes'), (10, 'Yes')])),
                ('excessive_thirst', models.PositiveIntegerField(choices=[(1, 'No'), (5, 'Sometimes'), (10, 'Yes')])),
                ('weight_loss', models.PositiveIntegerField(choices=[(1, 'No'), (5, 'Sometimes'), (10, 'Yes')])),
                ('extreme_hunger', models.PositiveIntegerField(choices=[(1, 'No'), (5, 'Sometimes'), (10, 'Yes')])),
                ('blurry_vision', models.PositiveIntegerField(choices=[(1, 'No'), (5, 'Sometimes'), (10, 'Yes')])),
                ('fatigue', models.PositiveIntegerField(choices=[(1, 'No'), (5, 'Sometimes'), (10, 'Yes')])),
                ('slow_healing_wounds', models.PositiveIntegerField(choices=[(1, 'No'), (5, 'Sometimes'), (10, 'Yes')])),
                ('numbness_tingling', models.PositiveIntegerField(choices=[(1, 'No'), (5, 'Sometimes'), (10, 'Yes')])),
                ('dry_mouth_skin', models.PositiveIntegerField(choices=[(1, 'No'), (5, 'Sometimes'), (10, 'Yes')])),
                ('family_history', models.PositiveIntegerField(choices=[(1, 'No'), (5, 'Sometimes'), (10, 'Yes')])),
                ('risk_level', models.CharField(choices=[('Low Risk', 'Low Risk'), ('Medium Risk', 'Medium Risk'), ('High Risk', 'High Risk'), ('Severe Risk', 'Severe Risk')], default='Unknown', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
