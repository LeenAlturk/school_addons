from odoo import models,fields,api
from odoo.exceptions import ValidationError
class ExamResult(models.Model):
    _name = 'school.exam.results'
    _description = 'school_exam_results'
    exam_id=fields.Many2one(
        comodel_name="school.exam",
        string="Exam"
    )
    class_id = fields.Many2one(
        "school.class",
        related="exam_id.class_id",
        store=True,
    )
    student_enroll = fields.Many2one(
        comodel_name="enrollment",
        string="Student",
        domain="[('status','=','active')]", required=True
    )
    total_mark=fields.Float(string='Total Mark')
    note=fields.Text(string='Note')
    section=fields.Many2one(comodel_name='school.section',string='Section')

    @api.constrains('student_enroll','class_id')
    def check_student_dup(self):
        for rec in self:
            conflict = self.search([
                ('student_enroll' ,'=', rec.student_enroll.id),
                ('class_id' , '=' , rec.class_id),
                ('id', '!=', rec.id),
            ]
            )

            if conflict:
                raise ValidationError('student should be Unique')

