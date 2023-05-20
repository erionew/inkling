from django.contrib import admin
from .models import Project
from .models import Document

admin.site.register({Document, Project})