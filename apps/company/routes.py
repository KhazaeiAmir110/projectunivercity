import json
import requests
from flask import Blueprint, render_template, request, redirect, url_for, session
from suds.client import Client

from kavenegar import KavenegarAPI

from apps.company.models import Company, SansConfig, SansHistoryDate, HolidaysDate, Reservation
from apps.users.models import User
from base import secret

blueprint = Blueprint('company', __name__)


@blueprint.route('/', methods=("GET", "POST"))
def home():
    if request.method == "POST":
        company_slug = request.form.get('company_slug')
        if company_slug:
            return redirect(url_for('company.company_detail', company_slug=company_slug))

    return render_template('company/page1.html',
                           companies=Company.objects.filter(is_active=1),
                           join_table=Company.objects.inner_join(join_table=User,
                                                                 join_condition='company.user_id=user.id'))


@blueprint.route('/<company_slug>', methods=("GET", "POST"))
def company_detail(company_slug):
    if request.method == "POST":
        request_code = request.form.get('code')
        if int(request_code) == secret.code:
            return redirect(url_for('company.payment', company_slug=company_slug))
        else:
            return render_template('pages/error.html',
                                   message="The code you entered is incorrect",
                                   company_slug=company_slug)

    company = Company.objects.get(slug=company_slug)
    return render_template('company/page2.html',
                           company=company,
                           holidays=HolidaysDate.objects.filter(company_id=company[0]),
                           join_company_sansconfig=
                           Company.objects.inner_join(join_table=SansConfig,
                                                      join_condition='company.id=sansconfig.company_id'),
                           sansconfig=SansConfig.objects.get(company_id=company[0]),
                           sansholidaydatetime=SansHistoryDate.objects.get(company_id=company[0]),
                           reservations=Reservation.objects.filter(company_id=company[0]),
                           )


@blueprint.route('/baraato/send', methods=['POST'])
def send_code():
    if request.method == 'POST':
        # save information user in session
        session['name'] = request.form.get('name'),
        session['family'] = request.form.get('family'),
        session['number'] = request.form.get('number'),
        session['email'] = request.form.get('email'),
        session['time'] = request.form.get('time'),
        session['date'] = request.form.get('date'),
        session['amount'] = request.form.get('amount')

        # send code to number
        # api = KavenegarAPI(secret.API_KEY)
        # params = {
        #     'receptor': request.form.get('number'),
        #     'message': f'کد تأیید : {secret.code}\n سیستم رزرواسیون و نوبت دهی براتو'
        # }
        #
        # api.sms_send(params)
        print(secret.code)

        return {'status': 'success'}
    return {'status': 'error', 'message': 'Invalid request'}


@blueprint.route('/<company_slug>/payment', methods=('GET', 'POST'))
def payment(company_slug):
    if request.method == 'POST':
        client = Client(secret.ZARINPAL_WEBSERVICE)
        if session['amount']:
            result = client.service.PaymentRequest(
                secret.MERCHANT, session['amount'], secret.description, secret.email, secret.phone,
                url_for('company.verify', _external=True)
            )
        else:
            return render_template('pages/error.html',
                                   message='Error')

        if result.Status == 100:
            return redirect(f'{secret.ZP_API_STARTPAY}{result.Authority}')
        else:
            return 'ERROR'

    # Display information to the user
    company = Company.objects.get(slug=company_slug),
    join_company_sansconfig = Company.objects.inner_join(join_table=SansConfig,
                                                         join_condition='company.id=sansconfig.company_id')

    for i in join_company_sansconfig:
        if i[0] == company[0][0]:
            result = i
    return render_template(
        'company/page4.html',
        company=company,
        result=result
    )


# zarinpal => verify
@blueprint.route('/payment/verify/', methods=['GET', 'POST'])
def verify():
    client = Client(secret.ZARINPAL_WEBSERVICE)
    if request.args.get('Status') == 'OK':
        result = client.service.PaymentVerification(secret.MERCHANT,
                                                    request.args['Authority'],
                                                    secret.amount)
        if result.Status == 100:
            return render_template('company/page5.html')
        else:
            return render_template('pages/error.html',
                                   message='Transaction failed. Status: ' + str(result.Status))
    else:
        return render_template('pages/error.html',
                               message='Transaction failed or canceled by user')
