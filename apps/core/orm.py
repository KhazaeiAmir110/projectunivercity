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
                return results[0]

    def update(self):
        pass

    def delete(self):
        pass

    def create(self):
        pass
