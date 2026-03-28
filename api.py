from fastapi import APIRouter, HTTPException
from schemas import Ticketcreate, TicketOut

api_router = APIRouter(prefix="/api/tickets")


ticket = []
current_ticket_id = 1

@api_router.post("/", response_model=TicketOut)
def create_ticket(ticket_data: Ticketcreate):
    global current_ticket_id

    for sold_ticket in ticket:
        if (sold_ticket.seat_number == ticket_data.seat_number and
            sold_ticket.movie_name == ticket_data.movie_name):
            return HTTPException(status_code=400, detail="Sotilgan bu bilet, umid qilma.")
        
    price = 80000 if ticket_data.is_vip else 40000

    new_ticket = {
        "ticket_id": current_ticket_id,
        "movie_name": ticket_data.movie_name,
        "seat_number": ticket_data.seat_number,
        "customer_name": ticket_data.customer_name,
        "is_vip": ticket_data.is_vip
    }

    ticket.append(new_ticket)
    current_ticket_id += 1

    return new_ticket

@api_router.get("/", response_model=list[TicketOut])
def get_ticket():
    return ticket