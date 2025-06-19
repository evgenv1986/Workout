class Exercise:
    _title: str
    def __init__(self, title: str):
        self._title = title
    def __eq__(self, other: 'Exercise'):
        return other._title.__eq__(self._title)
    def to_dict(self):
        return {'title': self._title}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'])