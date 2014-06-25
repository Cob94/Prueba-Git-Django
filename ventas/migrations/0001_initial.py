# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'ventas_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'ventas', ['Cliente'])

        # Adding model 'Producto'
        db.create_table(u'ventas_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('stock', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ventas', ['Producto'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table(u'ventas_cliente')

        # Deleting model 'Producto'
        db.delete_table(u'ventas_producto')


    models = {
        u'ventas.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'ventas.producto': {
            'Meta': {'object_name': 'Producto'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'stock': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['ventas']