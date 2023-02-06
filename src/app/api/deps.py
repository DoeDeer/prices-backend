# -*- coding: utf-8 -*-

"""Api's dependencies declarations and implementations."""

from fastapi import HTTPException

from app.models import Customer
from app.crud import customer as crud


async def get_customer_by_title(customer: str) -> Customer:
    """Return Customer model instances by provided customer title from query string.

    Raises:
        HTTPException: If customer with such title didn't found.

    """
    db_customer = await crud.get_multi(where_clause=Customer.title == customer)
    if len(db_customer) != 1:
        raise HTTPException(status_code=400, detail="No such customer")
    return db_customer[0]
