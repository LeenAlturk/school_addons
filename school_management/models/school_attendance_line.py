# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class SchoolAttendanceLine(models.Model):
    """ This model represents school.attendance.line."""
    _name = 'school.attendance.line'
    _description = 'SchoolAttendanceLine'

    attendance_header = fields.Many2one(comodel_name="school.attendance",ondelete="cascade",)
    class_id = fields.Many2one(
        "school.class",
        related="attendance_header.timetable_id.class_time_table",
        store=True,
    )
    student_enroll = fields.Many2one(
        comodel_name="enrollment",
        string="Student",
        domain="[('status','=','active'), ('class_id','=',class_id)]",required = True
    )
    att_status = fields.Selection(
        [
            ("present", "Present"),
            ("absent", "Absent"),
            ("late", "Late"),
            ("excused", "Excused"),
        ], string="Attendance Status", required=True, default="present" )
    note = fields.Text(string="Note")

    @api.constrains('student_enroll' , 'attendance_header')
    def _check_double_att(self):
        for rec in self:
            conflict = self.search([
                ('student_enroll', '=', rec.student_enroll.id),
                ('attendance_header', '=', rec.attendance_header.id),
                ('id', '!=', rec.id),
            ])

            if conflict:
                raise ValidationError('The Student Already Added')

