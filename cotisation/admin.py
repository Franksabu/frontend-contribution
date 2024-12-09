from django.contrib import admin
from cotisation.models import Contribution, DetailContribution, TypeCotisation
# Register your models here.
from .models import Cotisation

admin.site.register(Cotisation)
admin.site.register(Contribution)
admin.site.register(DetailContribution)
admin.site.register(TypeCotisation)
# Register your models here.
