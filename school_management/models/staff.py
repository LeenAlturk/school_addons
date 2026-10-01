# -*- coding: utf-8 -*-
from Tools.scripts.dutree import store

from odoo import api, fields, models


class Teacher(models.Model):
    """ This model represents teacher."""
    _name = 'staff'
    _description = 'staff'
    _rec_name = "Full_Name"
    Staff_Number=fields.Char(
        string="Staff Number",
        required=True,
        readonly=True,
        copy=False,
        default="New",
    )
    First_Name=fields.Char(string="First name" , required = True)
    Last_Name=fields.Char(string="Last name",required =True)
    Full_Name = fields.Char(string='Full_name', compute='_compute_name', store=True )
    image=fields.Image()
    Gender=fields.Selection(
        [
            ("female" , "Female "),
            ("male" , "Male")
         ],string="Gender", required = True
    )
    note = fields.Text(string="Note")

    staff_type = fields.Selection ([
            ("administration", "Administration "),
            ("teacher", "Teacher")
        ], string="Staff Type", required=True
    )
    staff_status = fields.Selection([
        ("active" , "Active"),
        ("on Leave", "On Leave"),
        ("resigned", "Resigned")
    ] ,string="Staff Status", required = True)
    hire_Date = fields.Date(string="Hire Date")
    salary = fields.Float(string="Salary")
    date_of_birth=fields.Date(string="Date of Birth" , required = True)
    age = fields.Char(
        compute= "_compute_age" , string="Age" , store = True
    )
    National_ID = fields.Char(
        string="National ID"
    )
    phone =fields.Char(string="Phone")
    Email = fields.Char(string="Email")
    Mobil = fields.Char(string="Mobil")
    department= fields.Many2one(comodel_name="school.department",string="Department")
    @api.model_create_multi
    def create(self, vals):
        """Override the default create method to customize record creation logic."""
        return super().create(vals)

    @api.depends('First_Name','Last_Name')
    def _compute_name (self):
        for record in self:
            record.Full_Name=(
                f"{record.First_Name or ''} {record.Last_Name or ''}"
            ).strip()

    @api.depends("date_of_birth")
    def _compute_age(self):
        today = fields.Date.today()
        for record in self:
            if record.date_of_birth:
                record.age = (
                        today.year
                        - record.date_of_birth.year
                        - (
                                (today.month, today.day)
                                < (
                                    record.date_of_birth.month,
                                    record.date_of_birth.day,
                                )
                        )
                )
            else:
                record.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("Staff_Number", "New") == "New":
                vals["Staff_Number"] = self.env["ir.sequence"].next_by_code(
                    "school.staff"
                ) or "New"
        return super().create(vals_list)


