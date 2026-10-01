
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Exam(models.Model):
    _name = 'school.exam'
    _description = 'school_exam'
    _rec_name = 'name'
    name = fields.Char(string="Exam Name",required =True)
    exam_type=fields.Selection([
        ('midterm','Midterm'),
        ('quiz','Quiz'),
        ('final_ex','final exam')
    ],default='quiz',required =True)
    acadimic_year_id=fields.Many2one(
        comodel_name='academic.year',
        string='Academic Year'
    )
    class_id = fields.Many2one(
        comodel_name='school.class',
        string='School Class'
    )
    subject = fields.Many2one(
        comodel_name='school.subject',
        string='School Subject'
    )
    exam_date=fields.Date(string="Exam Date")
    max_mark=fields.Float(string='Max Mark')
    question_ids=fields.One2many(
        comodel_name="school.exam.question",
        inverse_name='exam_id'
    )
    results_ids=fields.One2many(
        comodel_name='school.exam.results',
        inverse_name='exam_id',
        string='Results'
    )

    @api.constrains('max_mark','results_ids')
    def check_mark(self):
            for rec in self:
               for result in rec.results_ids:
                    if result.total_mark > rec.max_mark or result.total_mark < 0:
                        raise ValidationError("student Mark should be less than Max Mark and Positive")



    @api.constrains('max_mark','question_ids')
    def check_sum_question_mark(self):
            for rec in self:
                mark_sum = 0.0
                for mark in rec.question_ids:
                    mark_sum += mark.mark_question
                    if mark_sum > rec.max_mark:
                        raise ValidationError('max mark of question should be less or equal Max Mark')






