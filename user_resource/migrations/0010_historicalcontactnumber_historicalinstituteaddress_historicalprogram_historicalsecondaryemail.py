# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import user_resource.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_resource', '0009_auto_20151023_0325'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalContactNumber',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('number', models.CharField(max_length=16)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical contact number',
            },
        ),
        migrations.CreateModel(
            name='HistoricalInstituteAddress',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('room', models.CharField(max_length=8, null=True, blank=True)),
                ('hostel', models.CharField(blank=True, max_length=8, null=True, choices=[[b'1', b'Hostel 1'], [b'2', b'Hostel 2'], [b'3', b'Hostel 3'], [b'4', b'Hostel 4'], [b'5', b'Hostel 5'], [b'6', b'Hostel 6'], [b'7', b'Hostel 7'], [b'8', b'Hostel 8'], [b'9', b'Hostel 9'], [b'10', b'Hostel 10'], [b'10A', b'Hostel 10A'], [b'11', b'Hostel 11'], [b'12', b'Hostel 12'], [b'13', b'Hostel 13'], [b'14', b'Hostel 14'], [b'15', b'Hostel 15'], [b'16', b'Hostel 16'], [b'tansa', b'Tansa'], [b'qip', b'QIP']])),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical institute address',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProgram',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('department', models.CharField(blank=True, max_length=16, null=True, choices=[[b'AE', b'Aerospace Engineering'], [b'ANIM', b'Animation'], [b'ASC', b'Application Software Centre'], [b'AGP', b'Applied Geophysics'], [b'ASI', b'Applied Statistics and Informatics'], [b'BME', b'Biomedical Engineering'], [b'BB', b'Biosciences and Bioengineering'], [b'BIOTECH', b'Biotechnology'], [b'CASDE', b'Centre for Aerospace Systems Design and Engineering'], [b'CDEEP', b'Centre for Distance Engineering Education Programme'], [b'CESE', b'Centre for Environmental Science and Engineering'], [b'CFDVS', b'Centre for Formal Design and Verification of Software'], [b'CRNTS', b'Centre for Research in Nanotechnology and Science'], [b'CTARA', b'Centre for Technology Alternatives for Rural Areas'], [b'CUSE', b'Centre for Urban Science and Engineering'], [b'CSRE', b'Centre of Studies in Resources Engineering'], [b'CHE', b'Chemical Engineering'], [b'CH', b'Chemistry'], [b'CLE', b'Civil Engineering'], [b'CLS', b'Climate Studies'], [b'CC', b'Computer Centre'], [b'CSE', b'Computer Science & Engineering'], [b'CEP', b'Continuing Education Programme'], [b'CORRSCI', b'Corrosion Science and Engineering'], [b'DSCE', b'Desai Sethi Centre for Entrepreneurship'], [b'ES', b'Earth Sciences'], [b'ET', b'Educational Technology'], [b'EE', b'Electrical Engineering'], [b'ESE', b'Energy Science and Engineering'], [b'HSS', b'Humanities & Social Science'], [b'IITBMRA', b'IITB-Monash Research Academy'], [b'IDC', b'Industrial Design Centre'], [b'IDC', b'Industrial Design Centre'], [b'IEOR', b'Industrial Engineering and Operations Research'], [b'IM', b'Industrial Management'], [b'IxD', b'Interaction Design'], [b'KReSIT', b'Kanwal Rekhi School of Information Technology'], [b'MS', b'Material Science'], [b'MMM', b'Materials, Manufacturing and Modelling'], [b'MM', b'Mathematics'], [b'ME', b'Mechanical Engineering'], [b'MEMS', b'Metallurgical Engineering & Materials Science'], [b'MVD', b'Mobility and Vehicle Design'], [b'NCAIR', b'National Centre for Aerospace Innovation and Research'], [b'NCM', b'National Centre for Mathematics'], [b'PHE', b'Physical Education'], [b'PH', b'Physics'], [b'PMS', b'Physics, Material Science'], [b'PC', b'Preparatory Course'], [b'RE', b'Reliability Engineering'], [b'SJMSOM', b'Shailesh J. Mehta School of Management'], [b'SAIF', b'Sophisticated Analytical Instrument Facility'], [b'SCE', b'Systems and Control Engineering'], [b'TCTD', b'Tata Center for Technology and Design'], [b'VISCOM', b'Visual Communication'], [b'WRCB', b'Wadhwani Research Centre for Bioengineering'], [b'CPS', b'Centre for Policy Studies']])),
                ('join_year', models.PositiveSmallIntegerField(blank=True, null=True, validators=[user_resource.models.validate_join_year])),
                ('graduation_year', models.PositiveSmallIntegerField(blank=True, null=True, validators=[user_resource.models.validate_graduation_year])),
                ('degree', models.CharField(blank=True, max_length=16, null=True, choices=[[b'BTECH', b'Bachelor of Technology'], [b'MTECH', b'Master of Technology'], [b'DD', b'B.Tech. + M.Tech. Dual Degree'], [b'MSC', b'Master of Science'], [b'PHD', b'Doctor of Philosophy'], [b'BDES', b'Bachelor of Design'], [b'MDES', b'Master of Design'], [b'MPHIL', b'Master of Philosophy'], [b'MMG', b'Master of Management'], [b'MSEx', b'M.S. (Exit Degree)'], [b'MtechEx', b'Master of Technology (Exit Degree)'], [b'MtechPhDDD', b'M.Tech. + Ph.D. Dual Degree'], [b'PC', b'Preparatory Course'], [b'VS', b'Visiting Student'], [b'MPhilEx', b'Master of Philosophy (Exit Degree)'], [b'MScEx', b'Master of Science (Exit Degree)'], [b'MScMTechDD', b'M.Sc. + M.Tech. Dual Degree'], [b'MScPhDDD', b'M.Sc. + Ph.D. Dual Degree'], [b'MPhilPhDDD', b'M.Phil. + Ph.D. Dual Degree'], [b'EMBA', b'Executive MBA'], [b'FYBS', b'Four Year BS'], [b'IMTECH', b'Integrated M.Tech.'], [b'MSCBR', b'Master of Science By Research'], [b'TYMSC', b'Two Year M.Sc.'], [b'FYIMSC', b'Five Year Integrated M.Sc.'], [b'DIIT', b'D.I.I.T.'], [b'DIITEx', b'D.I.T.T. (Exit Degree)']])),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical program',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSecondaryEmail',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical secondary email',
            },
        ),
    ]
