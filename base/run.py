from apps import app

from apps.company.models import Company

app.run()

Company.create_company()
