import django_tables2 as tables
from mahasiswa.models import Pemohon_Terpilih

class Pemohon_TerpilihTable(tables.Table):
    class Meta:
        model = Pemohon_Terpilih
