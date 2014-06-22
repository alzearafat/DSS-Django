from mahasiswa.models import Data_Pemohon, Pemohon_Terpilih, Data_Ranking
from django.contrib import admin




class Data_PemohonAdmin(admin.ModelAdmin):
    search_fields = ['NIM' , 'Nama']
    list_filter = ('Nama', 'NIM')
    ordering = ['Nama', 'NIM',]
    list_display = ('NIM', 'Nama', 'Prodi',)

class Pemohon_TerpilihAdmin(admin.ModelAdmin):
    search_fields = ['NIM' , 'Nama']
    list_display = ('NIM', 'Nama', 'Prodi',)

class POAdmin(admin.ModelAdmin):
	list_display = ('qty', 'cost', 'total')

class Data_RankingAdmin(admin.ModelAdmin):
	search_fields = ['NIM' , 'Nama']
#	ordering = ['Final']
	list_display = ('Nama', 'IPK_CF', 'Jumlah_Penghasilan_Ortu_SF', 'Nilai_Pemohon_CF', 'Nilai_Ideal_CF', 'GAP_CF', 'Bobot_Nilai_CF', 'Nilai_Pemohon_SF', 'Nilai_Ideal_SF', 'GAP_SF', 'Bobot_Nilai_SF', 'NCF', 'NSF', 'Ni_CF', 'Ni_SF', 'Ni' , 'Final')

admin.site.register(Data_Pemohon, Data_PemohonAdmin)
admin.site.register(Pemohon_Terpilih, Pemohon_TerpilihAdmin)
admin.site.register(Data_Ranking, Data_RankingAdmin)