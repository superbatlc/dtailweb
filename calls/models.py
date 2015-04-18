from django.db import models

class Call(models.Model):

    """
    Class Call

    Call Detail Record
    """
    system_id = models.IntegerField()
    calldate = models.DateTimeField('Data chiamata')
    trunk_src = models.CharField('Fascio Originante', max_length=10)
    line_src = models.CharField('Linea Originante', max_length=10)
    trunk_dst = models.CharField('Fascio Terminante', max_length=10)
    line_dst = models.CharField('Linea Terminante', max_length=10)
    src = models.CharField('Sorgente', max_length=80)
    dst = models.CharField('Destinazione', max_length=80)
    access_code = models.CharField('Codice Accesso', max_length=10)
    duration = models.IntegerField('Durata')
    billsec = models.IntegerField()
    route = models.IntegerField()
    calltype = models.IntegerField()
    price = models.DecimalField('Prezzo', max_digits=7, decimal_places=4)

