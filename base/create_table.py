from apps.company.models import (
    Company, HolidaysDate, SansConfig, Reservation)
from apps.users.models import User

Company.objects.create_table()
HolidaysDate.objects.create_table()
SansConfig.objects.create_table()
Reservation.objects.create_table()
User.objects.create_table()

