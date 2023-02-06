# -*- coding: utf-8 -*-

"""CRUD implementations for prices."""


from typing import Optional

from sqlalchemy.sql import Selectable, ClauseElement

from app.crud.base import CRUDBase
from app.models import Price, Port, Customer
from app.schemas import price as schema


class CRUDPrice(CRUDBase[Price, schema.PriceCreate, schema.PriceUpdate]):
    """CRUD class for price with added with relation work on queries."""

    def _with_relations_query(self, where_clause: Optional[ClauseElement] = None) -> Selectable:
        port_alias = Port.alias()
        query = self.model.query.join(Port).join(port_alias).join(Customer).select()
        if where_clause:
            query = query.where(where_clause)
        return query.gino.load(orig_code=Port, dest_code=port_alias, customer=Customer).query


price = CRUDPrice(Price)
