class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x <= 0 or not isinstance(x, int):
            raise NonPositiveError()
        super(PositiveList, self).append(x)
