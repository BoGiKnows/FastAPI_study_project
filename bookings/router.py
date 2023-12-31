from fastapi import APIRouter


from .dao import BookingDAO
from .schemas import SBooking

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование'],
)


@router.get('')
async def get_bookings() -> list[SBooking]:
    return await BookingDAO.find_all()

