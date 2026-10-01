# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.addons.test_convert.tests.test_env import record


class SchoolTimeTableLine(models.Model):
    """ This model represents school.time.table.line."""
    _name = 'school.time.table.line'
    _description = 'SchoolTimeTableLine'
    _rec_name = "display_name"
    display_name = fields.Char(compute="_compute_display_name")
    day_session = fields.Selection([
        ("sat","saterday"),
        ("sunday", "Sunday"),
        ("monday", "Monday"),
        ("tuesday", "Tuesday "),
        ("wednesday", "Wednesday "),
        ("thursday", "Thursday "),
        ("friday", "Friday "),
    ],string="day", required = True)
    period = fields.Many2one(comodel_name="school.period" , string="Period")
    teacher = fields.Many2one(comodel_name="staff", domain="[('staff_type','=','teacher')]")
    subject= fields.Many2one(comodel_name="school.subject",string="Subject")
    time_table_id = fields.Many2one(
        comodel_name="school.time.table",
        string="Timetable",
    )

    @api.depends('day_session', 'period')
    def _compute_display_name(self):
       for rec in self:
         if rec.period and rec.day_session:
             day = dict(rec._fields['day_session'].selection).get(rec.day_session)
             period =rec.period.name if rec.period else ''
             rec.display_name = f"{day} - {period}"