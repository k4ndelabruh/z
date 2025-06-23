from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import db
from app.models.freight_request import FreightRequest
from app.forms.request_forms import FreightRequestForm
from datetime import datetime

request = Blueprint('request', __name__)

@request.route('/requests', methods=['GET'])
@login_required
def view_requests():
    user_requests = FreightRequest.query.filter_by(user_id=current_user.id).order_by(FreightRequest.date_created.desc()).all()
    return render_template('requests.html', title='Мои заявки - Грузовозофф', requests=user_requests)

@request.route('/requests/new', methods=['GET', 'POST'])
@login_required
def new_request():
    form = FreightRequestForm()
    
    if form.validate_on_submit():
        # Combine date and time fields into one datetime object
        transport_datetime = datetime.combine(form.transport_date.data, form.transport_time.data)
        
        freight_request = FreightRequest(
            transport_date=transport_datetime,
            weight=form.weight.data,
            dimensions=form.dimensions.data,
            cargo_type=form.cargo_type.data,
            pickup_address=form.pickup_address.data,
            delivery_address=form.delivery_address.data,
            user_id=current_user.id
        )
        
        db.session.add(freight_request)
        db.session.commit()
        
        flash('Заявка успешно создана!', 'success')
        return redirect(url_for('request.view_requests'))
    
    return render_template('create_request.html', title='Новая заявка - Грузовозофф', form=form, legend='Новая заявка') 