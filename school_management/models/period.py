# -*- coding: utf-8 -*-
from email.policy import default

from odoo import api, fields, models
class Period(models.Model):
    """ This model represents period."""
    _name = 'school.period'
    _description = 'Period'
    _order = "sequence"
    _rec_name = "name"
    name = fields.Char(string="period Name", required =True)
    start_time = fields.Float(string="Start Time", required =True)
    end_time =fields.Float(string="End Time", required =True)
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default =1
    )
    active = fields.Boolean(
        default=True
    )

