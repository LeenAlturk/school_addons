# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SchoolSubject(models.Model):
    """ This model represents school.subject."""
    _name = 'school.subject'
    _description = 'School Subject'
    name= fields.Char(string="name",required=True)
    code = fields.Char(string="Code" ,required=True)
    description = fields.Text(string="Description")
    credit_hours=fields.Float(string="Credit Hours" ,required=True)


