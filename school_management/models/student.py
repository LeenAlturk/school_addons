from odoo import api, fields, models
class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student"
    _rec_name = "full_name"
    _order = "student_number"

    student_number = fields.Char(
        string="Student Number",
        required=True,
        readonly=True,
        copy=False,
        default="New",
    )

    first_name = fields.Char(
        string="First Name",
        required=True,
    )

    last_name = fields.Char(
        string="Last Name",
        required=True,
    )

    full_name = fields.Char(
        string="Full Name",
        compute="_compute_full_name",
        store=True,
    )

    image = fields.Image()

    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
    ], string="Gender")

    date_of_birth = fields.Date(string="Date of Birth")

    age = fields.Integer(
        string="Age",
        compute="_compute_age",
        store=True,
    )

    phone = fields.Char(string="Phone")

    email = fields.Char(string="Email")

    address = fields.Text(string="Address")

    parent_name = fields.Char(string="Parent Name")

    parent_phone = fields.Char(string="Parent Phone")

    color_eyes = fields.Char(string ="Color eyes" , required =True)
    habbit = fields.Selection(
        [
            ("football" , " football"),
            ("painting", "Painting")
        ]
    )
    emergency_contact = fields.Char(string="Emergency Contact")

    admission_date = fields.Date(
        string="Admission Date",
        default=fields.Date.today,
    )

    status = fields.Selection([
        ("active", "Active"),
        ("graduated", "Graduated"),
        ("suspended", "Suspended"),
    ], default="active")

    notes = fields.Text(string="Notes")

    active = fields.Boolean(default=True)

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for record in self:
            record.full_name = (
                f"{record.first_name or ''} {record.last_name or ''}"
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
            if vals.get("student_number", "New") == "New":
                vals["student_number"] = self.env["ir.sequence"].next_by_code(
                    "school.student"
                ) or "New"
        return super().create(vals_list)