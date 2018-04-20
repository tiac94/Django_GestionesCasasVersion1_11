# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Persona, Cases, Factura

admin.site.register(Persona)
admin.site.register(Cases)
admin.site.register(Factura)