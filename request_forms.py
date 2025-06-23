from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, TextAreaField, SelectField
from wtforms.fields import DateField, TimeField
from wtforms.validators import DataRequired, NumberRange
from datetime import datetime, time

class FreightRequestForm(FlaskForm):
    transport_date = DateField('Дата перевозки', 
                            validators=[DataRequired()], 
                            default=datetime.now().date())
    
    transport_time = TimeField('Время перевозки', 
                           validators=[DataRequired()],
                           default=time(9, 0))
    
    weight = FloatField('Вес груза (кг)', 
                      validators=[DataRequired(), 
                                NumberRange(min=0.1, message='Вес должен быть положительным')])
    
    dimensions = StringField('Габариты (ДxШxВ в см)', validators=[DataRequired()])
    
    cargo_type = SelectField('Тип груза',
                           validators=[DataRequired()],
                           choices=[
                               ('Мебель', 'Мебель'),
                               ('Строительные материалы', 'Строительные материалы'),
                               ('Техника', 'Техника'),
                               ('Продукты питания', 'Продукты питания'),
                               ('Документы', 'Документы'),
                               ('Другое', 'Другое')
                           ])
    
    pickup_address = TextAreaField('Адрес отправления', validators=[DataRequired()])
    
    delivery_address = TextAreaField('Адрес получения', validators=[DataRequired()])
    
    submit = SubmitField('Отправить заявку') 