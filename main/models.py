# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TimeStampModel(models.Model):
    """ Abstract Model for Timestamp """
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True


class Inquiry(TimeStampModel):
    """ Model that contains the about page information """
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)


class Merchant(TimeStampModel):
    """ Model that contain the information for merchants who wants to signup"""
    NONE = 'NONE'
    MR = 'MR'
    MRS = 'MRS'
    MS = 'MS'
    DR = 'DR'
    PROF = 'PROF'
    GN = 'GENERAL RETAIL GOODS/SERVICES'
    FT = 'FITNESS CENTER/GYM'
    BHS = 'BEAUTY, HAIR AND SLIMING'
    MOTO = 'MOTO AND ECOMMERCE'
    EDU = 'EDUCATION'
    DS = 'MLM/DIRECT SELLING'
    AT = 'ALOCHOL/TOBACCO'
    FOX = 'TRADING/FOREX'
    REST = 'RESTURANT/CAFE'
    TOP = 'BILL PAYMENT/MOBILE TOPUP'
    HAND = 'HANDPHONE SHOP/REPAIR'
    RET = 'RETAIL (SHOPPING MALL TENANT)'
    HEAL = 'CLINIC/HEALTHCARE'
    TRANS = 'TRANSPORTATION/CAR RENTAL'
    BAR = 'BAR/NIGHTCLUB'
    ALL = 'ALLIANCE BANK'
    AM = 'AMBANK'
    BIS = 'BANK ISLAM'
    BMU = 'BANK MUAMALAT'
    BSN = 'BSN'
    CIMB = 'CIMB'
    CIT = 'CITIBANK'
    GP = 'GLOBAL PAYMENTS'
    HL = 'HONG LEONG'
    MYB = 'MAYBANK'
    OC = 'OCBC'
    PUB = 'PUBLIC BANK'
    RHB = 'RHB'
    STD = 'STANDARD CHARTERED'
    SYN = 'SYNERGY'
    UOB = 'UOB'
    PHONE = 'PHONE'
    SEARCH = 'SEARCH ENGINE'
    WORD = 'WORD OF MOUTH'
    EMPREF = 'EMPLOYEE REFERRAL'
    OTH = 'OTHER'
    PH = 'PHONE'
    EM = 'EMAIL'
    WA = 'WHATSAPP'
    APP = 'APPOITMENT'
    company = models.CharField(max_length=255, null=False, blank=False)
    SALUTATION = (
        (NONE, 'None'),
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MS, 'Ms'),
        (DR, 'Dr'),
        (PROF, 'Prof')
    )
    salutation = models.CharField(choices=SALUTATION, max_length=4, null=False, blank=False)
    f_name = models.CharField(max_length=255, null=False, blank=False)
    l_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    mobile = models.CharField(max_length=100, null=False, blank=False, unique=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    INDUSTRY = (
        (NONE, 'None'),
        (GN, 'General Retail Goods/Services'),
        (FT, 'Fitness Centre/Gym'),
        (BHS, 'Beauty, Hair and Slimming'),
        (MOTO, 'MOTO and eCommerce'),
        (EDU, 'Education'),
        (DS, 'MLM/Direct Selling'),
        (AT, 'Alcohol/Tobacco'),
        (FOX, 'Trading/Forex'),
        (REST, 'Restaurant/Cafe'),
        (TOP, 'Bill Payment/Mobile Topup'),
        (HAND, 'Handphone Shop/Repair'),
        (RET, 'Retail (Shopping Mall Tenant)'),
        (HEAL, 'Clinic/Healthcare'),
        (TRANS, 'Transportation/Car Rental'),
        (BAR, 'Bar/Nightclub'),
    )
    industry = models.CharField(choices=INDUSTRY, max_length=255, null=False, blank=False)
    salay = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    BANK = (
        (ALL, 'Alliance Bank'),
        (AM, 'AmBank'),
        (BIS, 'Bank Islam'),
        (BMU, 'Bank Muamalat'),
        (BSN, 'BSN'),
        (CIMB, 'CIMB'),
        (CIT, 'CitiBank'),
        (GP, 'Global Pyaments'),
        (HL, 'Hong Leong'),
        (MYB, 'MayBank'),
        (OC, 'OCBC'),
        (PUB, 'Public Bank'),
        (RHB, 'RHB'),
        (STD, 'Standard Chartered'),
        (SYN, 'Synergy'),
        (UOB, 'UOB'),
    )
    bank = models.CharField(choices=BANK, max_length=50, null=False, blank=False)
    SOURCE = (
        (PHONE, 'Phone'),
        (SEARCH, 'Search Engine'),
        (WORD, 'Word Of MoUth'),
        (EMPREF, 'Employee Referral'),
        (OTH, 'Other')
    )
    lead_source = models.CharField(choices=SOURCE, max_length=100, null=False, blank=False)
    CONTACT = (
        (PH, 'Phone'),
        (EM, 'Email'),
        (WA, 'WhatsApp'),
        (APP, 'Appointment')
    )
    contact_method = models.CharField(choices=CONTACT, max_length=50, null=False, blank=False)
