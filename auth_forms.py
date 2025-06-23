from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from app.models.user import User

class RegistrationForm(FlaskForm):
    username = StringField('Логин', 
                           validators=[DataRequired(), 
                                      Length(min=6, message='Логин должен содержать минимум 6 символов')])
    
    fullname = StringField('ФИО', validators=[DataRequired()])
    
    phone = StringField('Телефон', 
                       validators=[DataRequired(),
                                  Regexp(r'^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$', 
                                       message='Введите номер в формате +7(XXX)-XXX-XX-XX')])
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Пароль', 
                            validators=[DataRequired(), 
                                       Length(min=6, message='Пароль должен содержать минимум 6 символов')])
    
    confirm_password = PasswordField('Подтверждение пароля', 
                                    validators=[DataRequired(), EqualTo('password', message='Пароли должны совпадать')])
    
    submit = SubmitField('Зарегистрироваться')
    
    # Custom validators
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Этот логин уже занят. Пожалуйста, выберите другой.')
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Этот email уже зарегистрирован.')


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти') 