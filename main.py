from datetime import date
from typing import Optional
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

from bookings.router import router as router_bookings
from users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


class SHotel(BaseModel):
    address: str
    name: str
    start: int


class SHotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            stars: Optional[int] = Query(None, ge=1, le=5),
            has_spa: Optional[bool] = None

    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


# @app.get('/hotels', response_model=list[SHotel]) Валиадация данных на отправку
@app.get('/hotels')
def get_hotels(
        search_args: SHotelsSearchArgs = Depends()
) -> list[SHotel]:  # то же что и response_model на 15 строчке
    hotels = [
        {
            'address': 'Уральская 150 кв 101',
            'name': 'Super Hotel',
            'start': 5
        }
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
def add_booking(booking: SBooking):
    ...