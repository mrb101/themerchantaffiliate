# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('company', models.CharField(max_length=255)),
                ('salutation', models.CharField(choices=[('NONE', 'None'), ('MR', 'Mr'), ('MRS', 'Mrs'), ('MS', 'Ms'), ('DR', 'Dr'), ('PROF', 'Prof')], max_length=4)),
                ('f_name', models.CharField(max_length=255)),
                ('l_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('mobile', models.CharField(max_length=100, unique=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('industry', models.CharField(choices=[('NONE', 'None'), ('GENERAL RETAIL GOODS/SERVICES', 'General Retail Goods/Services'), ('FITNESS CENTER/GYM', 'Fitness Centre/Gym'), ('BEAUTY, HAIR AND SLIMING', 'Beauty, Hair and Slimming'), ('MOTO AND ECOMMERCE', 'MOTO and eCommerce'), ('EDUCATION', 'Education'), ('MLM/DIRECT SELLING', 'MLM/Direct Selling'), ('ALOCHOL/TOBACCO', 'Alcohol/Tobacco'), ('TRADING/FOREX', 'Trading/Forex'), ('RESTURANT/CAFE', 'Restaurant/Cafe'), ('BILL PAYMENT/MOBILE TOPUP', 'Bill Payment/Mobile Topup'), ('HANDPHONE SHOP/REPAIR', 'Handphone Shop/Repair'), ('RETAIL (SHOPPING MALL TENANT)', 'Retail (Shopping Mall Tenant)'), ('CLINIC/HEALTHCARE', 'Clinic/Healthcare'), ('TRANSPORTATION/CAR RENTAL', 'Transportation/Car Rental'), ('BAR/NIGHTCLUB', 'Bar/Nightclub')], max_length=255)),
                ('salay', models.IntegerField()),
                ('description', models.TextField()),
                ('bank', models.CharField(choices=[('ALLIANCE BANK', 'Alliance Bank'), ('AMBANK', 'AmBank'), ('BANK ISLAM', 'Bank Islam'), ('BANK MUAMALAT', 'Bank Muamalat'), ('BSN', 'BSN'), ('CIMB', 'CIMB'), ('CITIBANK', 'CitiBank'), ('GLOBAL PAYMENTS', 'Global Pyaments'), ('HONG LEONG', 'Hong Leong'), ('MAYBANK', 'MayBank'), ('OCBC', 'OCBC'), ('PUBLIC BANK', 'Public Bank'), ('RHB', 'RHB'), ('STANDARD CHARTERED', 'Standard Chartered'), ('SYNERGY', 'Synergy'), ('UOB', 'UOB')], max_length=50)),
                ('lead_source', models.CharField(choices=[('PHONE', 'Phone'), ('SEARCH ENGINE', 'Search Engine'), ('WORD OF MOUTH', 'Word Of MoUth'), ('EMPLOYEE REFERRAL', 'Employee Referral'), ('OTHER', 'Other')], max_length=100)),
                ('contact_method', models.CharField(choices=[('PHONE', 'Phone'), ('EMAIL', 'Email'), ('WHATSAPP', 'WhatsApp'), ('APPOITMENT', 'Appointment')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
