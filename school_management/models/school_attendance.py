# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SchoolAttendance(models.Model):
    """ This model represents school.attendance."""
    _name = 'school.attendance'
    _description = 'SchoolAttendance'
    date = fields.Date(string="attendance Date", required = True )
    timetable_id = fields.Many2one(comodel_name="school.time.table", string="Time table" , required = True)
    timetable_line = fields.Many2one(
        comodel_name="school.time.table.line",
        string="Period",
        domain="[('time_table_id', '=', timetable_id)]",
    )
    attendance_line_ids = fields.One2many('school.attendance.line', 'attendance_header', string='Attendance')

