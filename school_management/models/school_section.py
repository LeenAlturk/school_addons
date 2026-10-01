from odoo import fields,models,api
from odoo.exceptions import UserError, ValidationError, AccessError, MissingError

class Section (models.Model):
    _name = 'school.section'
    _description = 'school.section'
    _rec_name = ''
    name = fields.Char(string='section' , required=True)
    section_teacher = fields.Many2one(comodel_name="staff",domain="[('staff_type','=','teacher')]")
    capacity = fields.Integer(string="Capacity", required=True)
    class_id = fields.Many2one(comodel_name='school.class', ondelete="cascade")



