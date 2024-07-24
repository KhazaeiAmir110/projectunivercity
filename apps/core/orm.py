class ORMMixin:
    def get(self, *args, **kwargs):
        keys = [key for key in kwargs]
        if len(keys) == 0:
            return None
        elif len(keys) > 1:
            return ValueError("ERROR : User More than one")
        else:
            with self:
                results = self.execute_raw(
                    f"""
                        SELECT * FROM {self.__class__.__name__.split('Manager')[0].lower()} where
                         {keys[0]} = '{kwargs[keys[0]]}';
                    """
                )
                if len(results) == 0:
                    return None
                return results[0]

    def update(self):
        pass

    def delete(self, *args, **kwargs):
        global key_, value_
        geting = self.get(*args, **kwargs)

        if type(geting) is tuple:
            for key, value in kwargs.items():
                key_ = key
                value_ = value
            with self:
                self.execute_raw(
                    f"""
                                    DELETE FROM {self.__class__.__name__.split('Manager')[0].lower()} WHERE
                                     {key_}='{value_}';
                                """
                )
                return True
        else:
            raise ValueError("ERROR :Not delete")

    def create(self, *args, **kwargs):
        keys = []
        values = []
        for key, value in kwargs.items():
            keys.append(key)
            values.append(value)

        with self:
            self.execute_raw(
                f"""
                    INSERT INTO {self.__class__.__name__.split('Manager')[0].lower()}
                     ({', '.join(keys)})
                     VALUES ({str(', '.join(list(map(str, values))))})
                     
                """
            )
            return True
