from odoo import models,fields,api
from odoo.exceptions import ValidationError
class Choises(models.Model):
    _name = 'school.exam.question.choice'
    _description = 'school.choices'
    _rec_name = 'choice'
    question_id=fields.Many2one(
        comodel_name='school.exam.question'
    )
    choice=fields.Char(string='choice')
    is_correct=fields.Boolean(string='is Correct Ans')

