# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Data_Pemohon'
        db.create_table(u'mahasiswa_data_pemohon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nama', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('NIM', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Status_Aktif', self.gf('django.db.models.fields.BooleanField')()),
            ('Prodi', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('Jenis_Kelamin', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('Agama', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('TTL', self.gf('django.db.models.fields.DateField')()),
            ('Email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('No_Tlp', self.gf('django.db.models.fields.BigIntegerField')()),
            ('Nama_Ayah', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('Nama_Ibu', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('Pekerjaan_Ortu', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('Alamat', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'mahasiswa', ['Data_Pemohon'])

        # Adding model 'Pemohon_Terpilih'
        db.create_table(u'mahasiswa_pemohon_terpilih', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nama', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mahasiswa.Data_Pemohon'])),
            ('NIM', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('Prodi', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'mahasiswa', ['Pemohon_Terpilih'])

        # Adding model 'Data_Ranking'
        db.create_table(u'mahasiswa_data_ranking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nama', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mahasiswa.Data_Pemohon'])),
            ('IPK_CF', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Jumlah_Penghasilan_Ortu_SF', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Nilai_Pemohon_CF', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=0, blank=True)),
            ('Nilai_Ideal_CF', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('Bobot_Nilai_CF', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Nilai_Pemohon_SF', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=0, blank=True)),
            ('Nilai_Ideal_SF', self.gf('django.db.models.fields.IntegerField')(default=4)),
            ('Bobot_Nilai_SF', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'mahasiswa', ['Data_Ranking'])


    def backwards(self, orm):
        # Deleting model 'Data_Pemohon'
        db.delete_table(u'mahasiswa_data_pemohon')

        # Deleting model 'Pemohon_Terpilih'
        db.delete_table(u'mahasiswa_pemohon_terpilih')

        # Deleting model 'Data_Ranking'
        db.delete_table(u'mahasiswa_data_ranking')


    models = {
        u'mahasiswa.data_pemohon': {
            'Agama': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'Alamat': ('django.db.models.fields.TextField', [], {}),
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'Jenis_Kelamin': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'Meta': {'object_name': 'Data_Pemohon'},
            'NIM': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Nama': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Nama_Ayah': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'Nama_Ibu': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'No_Tlp': ('django.db.models.fields.BigIntegerField', [], {}),
            'Pekerjaan_Ortu': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'Prodi': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'Status_Aktif': ('django.db.models.fields.BooleanField', [], {}),
            'TTL': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mahasiswa.data_ranking': {
            'Bobot_Nilai_CF': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Bobot_Nilai_SF': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'IPK_CF': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Jumlah_Penghasilan_Ortu_SF': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Meta': {'object_name': 'Data_Ranking'},
            'Nama': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mahasiswa.Data_Pemohon']"}),
            'Nilai_Ideal_CF': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'Nilai_Ideal_SF': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'Nilai_Pemohon_CF': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '0', 'blank': 'True'}),
            'Nilai_Pemohon_SF': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '0', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mahasiswa.pemohon_terpilih': {
            'Meta': {'object_name': 'Pemohon_Terpilih'},
            'NIM': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'Nama': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mahasiswa.Data_Pemohon']"}),
            'Prodi': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['mahasiswa']