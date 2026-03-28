from pydantic import BaseModel, Field

class Ticketcreate(BaseModel):
    movie_name: str = Field(max_length=100)
    seat_number: int = Field(ge=1, le=100)
    customer_name: str = Field(max_length=100)
    is_vip: bool = Field(default=False)

class TicketOut(BaseModel):
    ticket_id: int = Field(le=1)
    movie_name: str = Field(max_length=100)
    seat_number: int = Field(ge=1, le=100)
    customer_name: str = Field(max_length=100)
    is_vip: bool = Field(default=False)
    price: float = Field(max_digits=10, decimal_places=2, default=0)



