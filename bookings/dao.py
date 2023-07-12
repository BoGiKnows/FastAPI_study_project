from sqlalchemy import select

from bookings.models import Bookings
from DAO.base import BaseDAO
from database import async_session_maker


class BookingDAO(BaseDAO):
    model = Bookings
