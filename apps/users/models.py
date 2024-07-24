from apps.core.database import Database
from apps.core.orm import ORMMixin


class UserManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL,
            is_superuser BOOLEAN NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            is_active BOOLEAN NOT NULL,
            date_joined TIMESTAMP NOT NULL,
            username TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            otp TEXT
        );
    """

class User:
    objects = UserManager()