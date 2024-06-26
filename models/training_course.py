from odoo import models, fields, api

class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'tabel Training Course'
    _sql_constraints = [("name_unique", "unique(name)", "Error message")]

    name = fields.Char(string='Nama Kursus' )
    keterangan = fields.Text(string='keterangan' )
    user_id = fields.Many2one(comodel_name='res.users', string='Penanggung Jawab' )
    session_line = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Sessions' )
   

   
class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Session'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Sesi Training', required=True)
    course_id = fields.Many2one(comodel_name='training.course', string='Course Name', required=True, ondelete='cascade', tracking=True)
    start_date = fields.Date(string='Start Date', required=True , tracking=True)
    duration = fields.Float(string='Duration', required=True , tracking=True)
    seats = fields.Integer(string='Peserta', required=True, default=1 , tracking=True)
    instruktur_id = fields.Many2one(comodel_name='instruktur', string='Instruktur' , tracking=True)
    
    alamat = fields.Char(string='Alamat',related='instruktur_id.street' , tracking=True)
    no_hp = fields.Char(string='Handpone',related='instruktur_id.mobile' , tracking=True)
    email = fields.Char(string='Email',related='instruktur_id.email' , tracking=True)
    jenis_kel = fields.Selection(string='Jenis Kelamin',related='instruktur_id.jenis_kel' , tracking=True)
    peserta_ids = fields.Many2many(comodel_name='peserta', string='Peserta' , tracking=True)
    jml_peserta = fields.Char(compute='_compute_jml_peserta',string='Jumlah peserta' , tracking=True)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('progres', 'Sedang Berlangsung'),('done', 'Selesai'),],default= 'draft' , tracking=True)

    
    

    @api.depends('peserta_ids')
    def _compute_jml_peserta(self):
        for rec in self:
            rec.jml_peserta = len(rec.peserta_ids)
    
    def action_confirm(self):
        self.state = 'progres'
    def action_done(self):
        self.state = 'done'
    def action_draft(self):
        self.state = 'draft'        
        
        




    
    
    

    
    
    