# -*- coding: utf-8 -*-

from openerp import models, fields, api
'''clase curso en el cual se pide el nombre y su descripcion '''
class Course(models.Model):
    _name = 'openacademy.course'
    
    name = fields.Char(string="Titulo", required=True)
    description = fields.Text()
    
    
class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
  
