from apps.users.models import User
from apps.company.models import (
    Company, HolidaysDate, SansConfig, Reservation)

User.objects.create_table()
Company.objects.create_table()
HolidaysDate.objects.create_table()
SansConfig.objects.create_table()
Reservation.objects.create_table()