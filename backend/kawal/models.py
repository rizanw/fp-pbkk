from django.db import models
from django.utils import timezone


class ModelBase(models.Model):
    name = models.CharField(max_length=40)
    detail = models.CharField(max_length=280)

    def __str__(self):
        return self.name


class APD(ModelBase):
    class Meta:
        verbose_name = "Alat Pelindung Diri"
        verbose_name_plural = "Alat Pelindung Diri"

    pass


class Hospital(ModelBase):
    class Meta:
        verbose_name = "Rumah Sakit"
        verbose_name_plural = "Rumah Sakit"

    address = models.CharField(max_length=140)
    verified = models.BooleanField(default=False)


class Transaction(models.Model):
    class Type(models.TextChoices):
        INPUT = '1', 'Pemasukan'
        REQUEST = '2', 'Permintaan'

    class Meta:
        verbose_name = "Transaksi"
        verbose_name_plural = "Transaksi"

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=Type.choices,
                            default=Type.INPUT)
    date_created = models.DateTimeField('created', default=timezone.now)

    def __str__(self):
        return f"{self.hospital} - {self.type} - {self.date_created}"


class TransactionDetail(models.Model):
    apd = models.ForeignKey(APD, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.apd}@{self.count} for {self.transaction}"
