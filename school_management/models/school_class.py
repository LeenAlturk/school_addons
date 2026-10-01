# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SchoolClass(models.Model):
    """ This model represents school.class."""
    _name = 'school.class'
    _description = 'School Class'
    name= fields.Char(string="Class Name" , compute ="_compute_name"
)
    grade = fields.Selection([
        ('kg1', 'KG 1'),
        ('kg2', 'KG 2'),
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ], string="Grade", required=True)
    section_ids = fields.One2many(comodel_name='school.section' ,inverse_name="class_id" , required = True)
    academic_year=fields.Many2one(comodel_name="academic.year", string="Academic year" , required = True)
    teacher_id= fields.Many2one(comodel_name="staff",string="Supervisor", required = True , domain="[('staff_type','=','teacher')]")

    @api.depends("grade")
    def _compute_name(self):
        for record in self:
            if record.grade:
                record.name = (
                    f"Grade {record.grade}"
                )
            else:
                record.name = ""

    _sql_constraints = [
        (
            "unique_class",
            "unique(grade, section, academic_year)",
            "This class already exists for the selected academic year!"
        )
    ]