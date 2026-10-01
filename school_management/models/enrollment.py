# -*- coding: utf-8 -*-
from email.policy import default

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError, AccessError, MissingError


class Enrollment(models.Model):
    """ This model represents enrollment."""
    _name = 'enrollment'
    _description = 'Enrollment'
    _rec_name = 'student_id'
    student_id=fields.Many2one(comodel_name="school.student",string="Student Name")
    class_id=fields.Many2one(comodel_name="school.class",string="Class")
    section_class_section =fields.Many2one(string="section",comodel_name="school.section",domain="[('class_id', '=', class_id)]")
    academic_year_id = fields.Many2one(
        "academic.year",
    )
    enrollment_date =fields.Date(default = fields.Date.today, string="enrollment Date")
    status=fields.Selection([
        ("active","Active"),
        ("graduate", "Graduate"),
        ("cancelled", "Cancelled")
    ],  string="status",default="active")

    @api.onchange("class_id")
    def _onchange_class_id(self):
        if self.class_id:
            self.academic_year_id = self.class_id.academic_year


    _sql_constraints = [
        (
            "unique_enrollment",
            "unique(student_id,class_id,acadimic_year_id)",
            "This Student already Registered!"
        )
    ]
    @api.constrains('class_id','status')
    def _check_class_availability(self):
        for record in self:
            if record.class_id: #check if class id is existing
                enroll = self.search_count([ # search and count  number of records
                    ("class_id","=",record.class_id.id), # that have same class _id
                    ("status","=","active"), # and status = active
                    ("id", "!=", record.id),   # exclude this record
                ])
                if enroll >= record.section_class_section.capacity: #compare number with  capacity
                    raise ValidationError('This class is Full') #rais validation error if  enroll >= capacity

