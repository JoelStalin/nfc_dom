from odoo import api, fields, models
from odoo.exceptions import ValidationError

class NcfDom(models.Model):
  _name = 'ncf.dom'
  _description = 'Numero de comprobante Fiscal'
  diario  = fields.Many2one('account.journal', string='Diario')
  type_nfc  = fields.Many2one('account.fiscal.position', string='Fiscal Position',  required=True)
  sufijo   = fields.Char(string='Sufijo', size=3, required=True)
  start_ncf = fields.Integer('star.number', required=True)
  end_ncf = fields.Integer('end.number', required=True)
  experation_date  = fields.Date('expiration.date', required=True)
  sequence_number = fields.Integer('sequence.number', required=True)
#   _sql_constraints = [
#                      ('diario', 
#                       'unique(diario)')
# ]
  
  @api.constrains('experation_date')
  def _validation_date(self):
    for record  in self:
     if record.experation_date < fields.Date.today():
       raise ValidationError("La fecha no puede ser menor que la fecha de hoy.")
  
  @api.constrains('sufijo')
  def _isalpha(self):
     for record  in self:   
      if not record.sufijo[0].isalpha():
        raise ValidationError("El primer carácter no es una letra")
  
       