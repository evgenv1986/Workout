class Exercise:
    _title: str
    def __init__(self, title: str):
        self._title = title
    def __eq__(self, other: 'Exercise'):
        return other._title.__eq__(self._title)