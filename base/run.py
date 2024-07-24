from apps import app

from apps.company.models import Company

if __name__ == '__main__':
    Company.objects.create_table()
    # res = Company.objects.get(id=1)
    # print(Company.objects.delete(name='amir'))
    Company.objects.insert(name='wsfd', description='asdf', address='sdfsfdf', slug='amirrsdfsfd', user_id=4)
    # print(Company.objects.filter(name='amir'))
    app.run()
