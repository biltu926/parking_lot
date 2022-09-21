from datetime import datetime
from app.fee_models import FeeModel
from app.ticket import ParkingTicket
import app.config as cfg


class ParkingReceipt:

    RECEIPT_NUMBER = 0

    def __init__(self) -> None:
        self.receipt_number: int = 0
        self.entry_date_time: str
        self.exit_date_time: str
        self.fees: float

    def __repr__(self) -> str:
        return f'Receipt number: {self.receipt_number}\nEntry date: {self.entry_date_time}\nExit date: {self.exit_date_time}\nFees: {self.fees}'

    def generate(self, ticket: ParkingTicket, fee_model: FeeModel):
        ParkingReceipt.RECEIPT_NUMBER += 1
        self.receipt_number = ParkingReceipt.RECEIPT_NUMBER
        self.entry_date_time = ticket.entry_date_time.strftime(cfg.date_format)
        self.exit_date_time = datetime.now().strftime(cfg.date_format)
        self.fees = fee_model.estimated_fees(ticket)
