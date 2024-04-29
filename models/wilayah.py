from odoo import models, fields, api


class RefPropinsi(models.Model):
    _name = 'ref.propinsi'
    _description = 'Ref Propinsi'

    name = fields.Char(string='Nama propinsi', required=True)
    kode = fields.Char(string='Kode propinsi')
    singkat = fields.Char(string='Singkatan')
    keterangan = fields.Text(string='Keterangan')
    kota_ids = fields.One2many(comodel_name='ref.kota', inverse_name='propinsi_id', string='Nama Kota')
    
class RefKota(models.Model):
    _name = 'ref.kota'
    _description = 'Ref Kota'

    name = fields.Char(string='Nama Kota')
    kode = fields.Char(string='Kode Kota')
    propinsi_id = fields.Many2one(comodel_name='ref.propinsi', string='Nama propinsi')
    singkat = fields.Char(string='Singkatan')
    keterangan = fields.Text(string='Keterangan')
    kecamatan_ids = fields.One2many(comodel_name='ref.kecamatan', inverse_name='kota_id', string='Nama kecamatan')
    
        
class RefKecamatan(models.Model):
    _name = 'ref.kecamatan'
    _description = 'Ref kecamatan'

    name = fields.Char(string='Nama kecamatan')
    kode = fields.Char(string='Kode Kecamatan')
    kota_id = fields.Many2one(comodel_name='ref.kota', string='Nama kota')
    
    keterangan = fields.Text(string='Keterangan')
    desa_ids = fields.One2many(comodel_name='ref.desa', inverse_name='kecamatan_id', string='Nama Desa')    
        
class RefDesa(models.Model):
    _name = 'ref.desa'
    _description = 'Ref Desa'

    name = fields.Char(string='Nama Desa')
    kode = fields.Char(string='Kode Desa')
    kecamatan_id = fields.Many2one(comodel_name='ref.kecamatan', string='Nama kecamatan')
    keterangan = fields.Text(string='Keterangan')
        