# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SchoolJobPosition(models.Model):
    """ This model represents school.job.position."""
    _name = 'school.job.position'
    _description = 'SchoolJobPosition'
    name = fields.Char(string="job position")
    department = fields.Many2one(comodel_name="school.department" ,string="Department")


