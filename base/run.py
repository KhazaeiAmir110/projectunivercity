from apps import app

from apps.company.models import Company

if __name__ == '__main__':
    Company.objects.create_table()
    # res = Company.objects.get(id=1)
    # print(Company.objects.delete(name='amir'))
    # print(Company.objects.create(name='wsfd', description='asdf', address='sdfsdf', slug='sdfsdf', user_id=4))
    print(Company.objects.filter(name='amir'))
    app.run()
