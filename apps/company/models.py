from apps.core.database import Database
from apps.core.orm import ORMMixin


class CompanyManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS company (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            address TEXT NOT NULL,
            slug TEXT NOT NULL UNIQUE,
            user_id INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(id)
        );
    """


class Company:
    objects = CompanyManager()

# class HolidayDateManager(Database):
#     def _create_instance(cls, *args, **kwargs):
#         super()._create_instance(*args, **kwargs)
#         cls.instance.execute_raw(
#             """
#                 CREATE TABLE IF NOT EXISTS holidaysdate (
#                 id SERIAL PRIMARY KEY,
#                 date DATE NOT NULL,
#                 company_id BIGINT NOT NULL REFERENCES company(id) DEFERRABLE INITIALLY DEFERRED
#             );
#             """
#         )
#
#
# class HolidaysDate:
#     objects = None
#
#     @classmethod
#     def create_company(cls):
#         if cls.objects is None:
#             cls.objects = HolidayDateManager()
