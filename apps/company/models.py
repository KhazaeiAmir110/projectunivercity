from apps.core.database import Database


class CompanyManager(Database):
    def _create_instance(cls, *args, **kwargs):
        super()._create_instance(*args, **kwargs)
        cls.instance.execute_raw(
            """
            CREATE TABLE IF NOT EXISTS company (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                address VARCHAR(200) NOT NULL,
                slug VARCHAR(100) NOT NULL UNIQUE,
                user_id BIGINT NOT NULL REFERENCES user(id) DEFERRABLE INITIALLY DEFERRED
            );
            """
        )


class Company:
    objects = None

    @classmethod
    def create_company(cls):
        if cls.objects is None:
            cls.objects = CompanyManager()
