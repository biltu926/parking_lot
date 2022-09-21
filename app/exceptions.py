
class Base(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class ParkingFull(Base):
    def __init__(self, *args) -> None:
        super().__init__(*args)

