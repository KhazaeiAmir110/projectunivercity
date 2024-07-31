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
            is_active BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES user(id)
        );
    """


class HolidaysDateManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS holidaysdate (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            company_id INTEGER NOT NULL,
            FOREIGN KEY(company_id) REFERENCES company(id)
        );
    """


class SansConfigManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS sansconfig (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_time TIME NOT NULL,
            end_time TIME NOT NULL,
            company_id INTEGER NOT NULL UNIQUE,
            duration INTEGER NOT NULL,
            amount INTEGER NOT NULL,
            FOREIGN KEY(company_id) REFERENCES company(id)
        );
    """


class ReservationManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS reservation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT NOT NULL,
            date DATE NOT NULL,
            time TIME NOT NULL,
            company_id INTEGER NOT NULL,
            FOREIGN KEY(company_id) REFERENCES company(id)
        );
    """


class SansHistoryDateManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS sanshistorydate (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_time TIME NOT NULL,
        end_time TIME NOT NULL,
        company_id INTEGER NOT NULL UNIQUE,
        FOREIGN KEY (company_id) REFERENCES company(id) ON DELETE CASCADE
    );
    """


class Company:
    objects = CompanyManager()


class HolidaysDate:
    objects = HolidaysDateManager()


class SansConfig:
    objects = SansConfigManager()


class SansHistoryDate:
    objects = SansHistoryDateManager()


class Reservation:
    objects = ReservationManager()
