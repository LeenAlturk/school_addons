# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AcademicYear(models.Model):
    _name = 'academic.year'
    _description = 'AcademicYear'

    name = fields.Char(compute = "_compute_name" ,string='year' , store=True,)
    start_date = fields.Date(string="Start Date" ,required =True)
    end_date=fields.Date(string=" End Date" ,required = True)
    active= fields.Boolean(string = "Active" ,default = True)
    state = fields.Selection([
        ("draft", "Draft"),
        ("active", "Active"),
        ("closed", "Closed"),
    ], default="draft")
    @api.depends("start_date", "end_date")
    def _compute_name(self):
        for record in self:
            if record.start_date and record.end_date:
                record.name = (
                    f"{record.start_date.year}-{record.end_date.year}"
                )
            else:
                record.name = ""
    def button_in_active(self):
        self.write({'state': "active"})

    def  button_in_closed(self):
        self.write({'state': "closed"})