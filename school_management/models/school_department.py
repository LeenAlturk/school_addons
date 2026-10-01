# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SchoolDepartment(models.Model):
    """ This model represents school.department."""
    _name = 'school.department'
    _description = 'School Department'
    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    manager=fields.Many2one(comodel_name="staff" ,string="Manger" , domain="[('staff_type', '=', 'administration')]")
    active = fields.Boolean(string="Active", default=True)
    _sql_constraints = [
        ('department_code_unique',
         'unique(code)',
         'Department code must be unique!'),
        ('department_name_unique',
         'unique(name)',
         'Department name must be unique!')
    ]

