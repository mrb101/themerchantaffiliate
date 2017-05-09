# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import (
    Merchant,
    Inquiry,
)

admin.site.register(Merchant)
admin.site.register(Inquiry)

