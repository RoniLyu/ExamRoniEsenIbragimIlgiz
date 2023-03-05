from flask_wtf import FlaskForm
import wtforms as wf

from . import app
from .models import Position


def get_categories():
    with app.app_context():
        return [(position.id, position.name) for position in Position.query.all()]


class PositionForm(FlaskForm):
    name = wf.StringField('Name', validators=[wf.validators.DataRequired()])
    department = wf.StringField('Department')
    wage = wf.IntegerField('Wage', validators=[wf.validators.DataRequired()])

    def validate_wage(self, wage):
        if wage.data < 0:
            raise wf.ValidationError('Wage must be positive')


class EmployeeForm(FlaskForm):
    name = wf.StringField('Name', validators=[wf.validators.DataRequired()])
    inn = wf.StringField('INN', validators=[wf.validators.DataRequired()])
    position_id = wf.SelectField('Position', choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position_id.choices = get_categories()


class UserForm(FlaskForm):
    username = wf.StringField('Username', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Password', validators=[wf.validators.DataRequired()])
