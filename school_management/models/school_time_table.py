# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SchoolTimeTable(models.Model):
    """ This model represents school.time.table."""
    _name = 'school.time.table'
    _description = 'SchoolTimeTable'
    _rec_name = 'table_name'
    table_name = fields.Char(compute ="_compute_table_name" ,string = "Table Name" ,store = True)
    academic_year_id = fields.Many2one(
        "academic.year",
        compute="_compute_academic_year",
        store=True,
    )
    class_time_table = fields.Many2one(comodel_name="school.class", string="Class")
    section_class_section =fields.Many2one(string="section",comodel_name="school.section",domain="[('class_id', '=', class_time_table)]")
    time_table_line_id = fields.One2many(inverse_name="time_table_id" , comodel_name="school.time.table.line")
    active = fields.Boolean(default=True)

    @api.depends("class_time_table")
    def _compute_academic_year(self):
        for rec in self:
            rec.academic_year_id = rec.class_time_table.academic_year

    @api.depends("class_time_table", "academic_year_id")
    def _compute_table_name(self):
        for record in self:
            if record.class_time_table and record.academic_year_id:
                record.table_name = (
                    f"{record.class_time_table.display_name} - "
                    f"{record.section_class_section.display_name}-"
                    f"{record.academic_year_id.display_name}"
                )
            else:
                record.table_name = ""
