from django.contrib.admin import ModelAdmin, register
from .models import APD, Hospital, Transaction, TransactionDetail


@register(APD)
class ApdAdmin(ModelAdmin):
    list_display = ('name', 'detail')


@register(Hospital)
class HospitalAdmin(ModelAdmin):
    list_display = ('name', 'address')


@register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = ('hospital', 'date_created')