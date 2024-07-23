from apps import app

from apps.company.models import Company

if __name__ == '__main__':
    Company.objects.create_table()
    res = Company.objects.get(1)
    app.run()
