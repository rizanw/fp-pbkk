from django.contrib.admin import ModelAdmin, StackedInline, register

from .models import APD, Hospital, Transaction, TransactionDetail


class TransactionDetailAdmin(StackedInline):
    view_on_site = False
    model = TransactionDetail


@register(APD)
class ApdAdmin(ModelAdmin):
    list_display = ('name', 'detail')
    list_per_page = 5


@register(Hospital)
class HospitalAdmin(ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('verified',)
    list_per_page = 5


@register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = ('hospital', 'date_created')
    list_filter = ('type',)
    readonly_fields = ('date_created',)
    inlines = (TransactionDetailAdmin,)
