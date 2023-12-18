# Generated by Django 3.2.22 on 2023-11-15 19:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModuleAssessment',
            fields=[
                ('studentModuleAssessmentID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('assessmentMark', models.FloatField(default=100, validators=[django.core.validators.MinValueValidator(0, message='Value must be greater than or equal to 0.'), django.core.validators.MaxValueValidator(100, message='Value must be less than or equal to 100.')])),
            ],
        ),
        migrations.RemoveField(
            model_name='modulelecturer',
            name='lecturerID',
        ),
        migrations.RemoveField(
            model_name='modulelecturer',
            name='moduleID',
        ),
        migrations.RemoveField(
            model_name='studentmoduleassesment',
            name='assessmentID',
        ),
        migrations.RemoveField(
            model_name='studentmoduleassesment',
            name='studentModuleID',
        ),
        migrations.AddField(
            model_name='lecturer',
            name='lecturerModules',
            field=models.ManyToManyField(to='database.Module'),
        ),
        migrations.AddField(
            model_name='module',
            name='careers',
            field=models.ManyToManyField(blank=True, to='database.Career'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='assessmentID',
            field=models.CharField(auto_created=True, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='assessmentWeight',
            field=models.FloatField(default=20),
        ),
        migrations.AlterField(
            model_name='career',
            name='careerID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='lecturerName',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='module',
            name='moduleDescription',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='student',
            name='currentPathwayMark',
            field=models.FloatField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='studentmodule',
            name='stuModMark',
            field=models.FloatField(default=0, editable=False),
        ),
        migrations.DeleteModel(
            name='CareerModule',
        ),
        migrations.DeleteModel(
            name='ModuleLecturer',
        ),
        migrations.DeleteModel(
            name='StudentModuleAssesment',
        ),
        migrations.AddField(
            model_name='studentmoduleassessment',
            name='assessmentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.assessment'),
        ),
        migrations.AddField(
            model_name='studentmoduleassessment',
            name='studentModuleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.studentmodule'),
        ),
    ]
