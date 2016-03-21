from openerp import fields, models


__author__ = "Sergio Benavides"

class Partner(models.Model):
    _inherit = 'res.partner'

    # insertar nueva columna a res.partner model, por defecto partners no tiene
    # instructors
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session',
        string="Attended Sessions", readonly=True)
