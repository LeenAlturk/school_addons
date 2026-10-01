from  odoo import models,api,fields
from  odoo.exceptions import UserError, ValidationError, AccessError, MissingError
class ExamQuestion(models.Model):
    _name ='school.exam.question'
    _description ='exam question'
    exam_id=fields.Many2one(
        comodel_name='school.exam'
    )
    question_num=fields.Integer(
        string="Question No"
        , required=True
    )
    question=fields.Text(string="Question",required=True)
    answer_type=fields.Selection(
        [
            ('Text_ans','Text answer'),
            ('multiple_Select','Multiple Select'),
            ('choices','Choices'),
            ('true_false_ans','True/False')
        ]
    )
    mark_question=fields.Float(string='Mark',required=True)
    choices_ids= fields.One2many(
      comodel_name='school.exam.question.choice',
      inverse_name='question_id',
        string="choices",

    )
    @api.constrains('question_num')
    def check_question_num_dup(self):
        for rec in self:
            conflict = self.search([
                ('question_num' ,'=', rec.question_num),
                ('id', '!=' , rec.id)
            ])

            if conflict:
                raise  ValidationError('Question Num Should Be Unique')
            if rec.question_num < 0 :
                raise  ValidationError("question Number Should be positive")


