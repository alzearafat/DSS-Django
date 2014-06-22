from django.db import models
from decimal import Decimal

class Data_Pemohon(models.Model):
    Nama = models.CharField(max_length = 50, null=False)
    NIM = models.CharField(max_length=10, null=False)
    Status_Aktif = models.BooleanField(null=False)
    PRODI = (
        ('AG', 'Agro'),
        ('IK', 'Ilmu Komunikasi'),
        ('PS', 'Psikologi'),
        ('SI', 'Sistem Informasi'),
        ('TI', 'Teknik Informatika'),
        )
    JENIS_KELAMIN = (
        ('P', 'Pria'),
        ('W', 'Wanita'),
        )
    AGAMA = (
        ('IM', 'Islam'),
        ('KR', 'Kristen'),
        ('KT','Katolik'),
        ('HD', 'Hindu'),
        ('BD', 'Budha'),
        )

    Prodi = models.CharField(max_length=20, choices=PRODI)
    Jenis_Kelamin = models.CharField(max_length=20, choices=JENIS_KELAMIN)
    Agama = models.CharField(max_length=20, choices=AGAMA)
    TTL = models.DateField()
    Email = models.EmailField(max_length = 50)
    No_Tlp = models.BigIntegerField()
    Nama_Ayah = models.CharField(max_length = 50, null=True)
    Nama_Ibu = models.CharField(max_length = 50, null=True)
    Pekerjaan_Ortu = models.CharField(max_length = 50, null=True)
    Alamat = models.TextField()

    class Meta:
        verbose_name_plural = "Data Pemohon"

    def __unicode__(self):
        return self.Nama


class Pemohon_Terpilih(models.Model):
    PRODI = (
        ('AG', 'Agro'),
        ('IK', 'Ilmu Komunikasi'),
        ('PS', 'Psikologi'),
        ('SI', 'Sistem Informasi'),
        ('TI', 'Teknik Informatika'),
        )
    Nama = models.ForeignKey(Data_Pemohon)
    NIM = models.CharField(max_length=10, null=True)
    Prodi = models.CharField(max_length=30, choices=PRODI, null=False)

    class Meta:
        verbose_name_plural = "Pemohon Terpilih"

    def __unicode__(self):
        return unicode(self.Nama)


#class PO(models.Model):
#    qty = models.IntegerField(null=True)
#    cost = models.IntegerField(null=True)
#
#    def _get_total(self):
#       "Returns the total"
#       return self.qty + self.cost
#    total = property(_get_total)



class Data_Ranking(models.Model):
    IPK = (
        ('1', '< 2,5'),
        ('2', '> 2,5 dan <= 3'),
        ('3', '> 3 dan <= 3,5'),
        ('4', '> 3,5'),
        )

    PENGHASILAN_ORTU = (
        ('4', '<=1.000.000'),
        ('3', '>1.000.000 <=3.000.000'),
        ('2', '>3.000.000 <=5.000.000'),
        ('1', '>=5.000.000'),
        )

    NILAI_PEMOHON = (
    (Decimal("1"), '1.0'),
    (Decimal("2"), '2.0'),
    (Decimal("3"), '3.0'),
    (Decimal("4"), '4.0'),
    )

    Nama = models.ForeignKey(Data_Pemohon)
    
    IPK_CF = models.CharField(max_length=30, choices=IPK, null=False)
    Jumlah_Penghasilan_Ortu_SF = models.CharField(max_length=30, choices=PENGHASILAN_ORTU, null=False)
    
    Nilai_Pemohon_CF = models.DecimalField(max_digits=11, decimal_places=0, choices=NILAI_PEMOHON, blank=True, null=False, help_text='Berikan nilai 1-5.')
    Nilai_Ideal_CF = models.IntegerField(blank=False, default=3, null=False, help_text='3 adalah nilai ideal CF yang dicari.')
    Bobot_Nilai_CF = models.FloatField(blank=True, null=True, help_text='Klik <a href="#">DISINI</a> untuk petunjuk Bobot Nilai.')

    Nilai_Pemohon_SF = models.DecimalField(max_digits=11, decimal_places=0, choices=NILAI_PEMOHON, blank=True, null=False, help_text='Berikan nilai 1-5.')
    Nilai_Ideal_SF = models.IntegerField(blank=False, default=4, null=False, help_text='4 adalah nilai ideal SF yang dicari.')
    Bobot_Nilai_SF = models.FloatField(blank=True, null=True, help_text='Klik <a href="#">DISINI</a> untuk petunjuk Bobot Nilai.')
    
    Final = models.FloatField(null=False)

    @property
    def Final(self):
        return self.Ni * 0.3

    def _get_GAP_CF(self):
       "Returns the total"
       return self.Nilai_Pemohon_CF - self.Nilai_Ideal_CF
    GAP_CF = property(_get_GAP_CF)

    def _get_GAP_SF(self):
       "Returns the total"
       return self.Nilai_Pemohon_SF - self.Nilai_Ideal_SF
    GAP_SF = property(_get_GAP_SF)

    
    def _get_NCF(self):
       "Returns the total"
       return self.Bobot_Nilai_CF / 1
    NCF = property(_get_NCF)

    def _get_NSF(self):
       "Returns the total"
       return self.Bobot_Nilai_SF / 1
    NSF = property(_get_NSF)

    def _get_Ni_CF(self):
       "Returns the total"
       return self.Bobot_Nilai_CF * 0.6
    Ni_CF = property(_get_Ni_CF)

    def _get_Ni_SF(self):
       "Returns the total"
       return self.Bobot_Nilai_SF * 0.4
    Ni_SF = property(_get_Ni_SF)

    def _get_Ni(self):
       "Returns the total"
       return self.Ni_CF + self.Ni_SF
    Ni = property(_get_Ni)

#    def _get_Final(self):
#       "Returns the total"
#       return self.Ni * 0.3
#    Final = property(_get_Final)

    class Meta:
        verbose_name_plural = "Data Ranking"



#    def save(self, *args, **kwargs):
#       "update number available on save"
#        self.GAP = self.Nilai_Pemohon - self.Nilai_Standard
#        super(Data_GAP, self).save(*args, **kwargs)

#    def save(self):
#        if not self.id:
#            self.Nilai_Standard = 3
#            super(Data_GAP, self).save()
