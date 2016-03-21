# -*- coding: utf-8 -*-

from openerp import models, fields, api
'''clase curso en el cual se pide el nombre y su descripcion '''
class Course(models.Model):
    _name = 'openacademy.course'
    
    name = fields.Char(string="Titulo", required=True)
    description = fields.Text()
    
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    
class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
  
