from flask import Blueprint, render_template, request, redirect, url_for, session

from apps.company.models import Company, SansConfig, SansHistoryDate, HolidaysDate, Reservation
from apps.users.models import User

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


@blueprint.route('/<company_slug>')
def company_detail(company_slug):
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

        # send code to number
        # api = KavenegarAPI(kavenegar.API_KEY)
        # params = {
        #     'receptor': request.POST.get('number'),
        #     'message': f'کد تأیید : {kavenegar.code}\n سیستم رزرواسیون و نوبت دهی براتو'
        # }
        #
        # api.sms_send(params)

        return {'status': 'success'}
    return {'status': 'error', 'message': 'Invalid request'}
