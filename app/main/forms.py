from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError, validators
from ..models import User, Department



class IssueForm(Form):
    '''This class creates an IssueForm
    object.
    '''

    name = StringField('Issue',
                       [validators.Required(message='Please enter the issue.')]
                       )
    description = TextAreaField('Issue Description',
                                [validators.required(
                                    message='Please describe your issue.')])
    priority = SelectField('Priority', choices=[
                    ('high', 'High'), ('medium', 'Medium'), ('low', 'Low')])

    department = SelectField('Department', choices=[
                    ('operations', 'Operations'), ('finance', 'Finance'), ('success', 'Success')])


    submit = SubmitField('Report Issue')

    # def __init__(self, *args, **kwargs):
    #     super(IssueForm, self).__init__(*args, **kwargs)
    #     self.department.choices = [
    #         (dept.id, dept.name) for dept in Department.query.all()]
