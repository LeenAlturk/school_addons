{
    "name": "School Management",
    "version": "18.0.1.0.0",
    "summary": "School Management System",
    "description": """
        School Management System
        ========================
        Manage:
        - Students
        - Teachers
        - Classes
        - Subjects
        - Attendance
        - Exams
        - Grades
        - Fees
    """,
    "author": "Leen Al Turk",
    "website": "",
    "category": "Education",
    "license": "LGPL-3",
    "depends": [
        "base",
    ],
    'data': [
    'security/ir.model.access.csv',
    'data/student_sequence.xml',
    'data/staff_sequence.xml',
    'views/student_views.xml',
	'views/staff.xml',
	'views/department.xml',
	'views/job_position_view.xml',
	'views/subject_view.xml',
	'views/academic_year_view.xml',
	'views/class_view.xml',
	'views/school_enrollment.xml',
	'views/school_period.xml',
	'views/time_table.xml',
	'views/school_atttendance.xml',
	'views/school_exam.xml',
		'views/school_exam_results.xml',
],
    "demo": [
    ],
    "installable": True,
    "application": True,
}