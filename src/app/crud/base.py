# -*- coding: utf-8 -*-

"""Implementations of base operations."""

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union, AsyncIterator

from pydantic import BaseModel
from sqlalchemy.sql import Select, ClauseElement

from app.db import db, BaseDBModel

ModelType = TypeVar("ModelType", bound=BaseDBModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """CRUD object with default methods to Create, Read, Update, Delete (CRUD).

    Args:
        model: A GINO model class

    """

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def _with_relations_query(self, where_clause: Optional[ClauseElement] = None) -> Select:
        """Return SELECT query wih joined and loaded relations.

        Args:
            where_clause (SQLAlchemy.sql.ClauseElement): WHERE conditions value.

        """
        return self._query(where_clause)

    def _query(self, where_clause: Optional[ClauseElement] = None) -> Select:
        """Return SELECT query without any related tables.

        Args:
            where_clause (SQLAlchemy.sql.ClauseElement): WHERE conditions value.

        """
        q = self.model.query
        if where_clause is not None:
            q = q.where(where_clause)
        return q

    async def get(self, id_: Any, with_relations: bool = True) -> Optional[ModelType]:
        """Return first founded raw object by given slug.

        Args:
            id_ (any): slug for search perform for,
            with_relations (bool): does return object should load related objects.

        Returns:
            model object instance. Return None if no result founded by provided slug.

        """
        if with_relations:
            return await self._with_relations_query().gino.first()  # noqa: Gino tricks
        return await self.model.get(id_)

    async def get_multi(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        with_relations: bool = True,
        where_clause: Optional[ClauseElement] = None
    ) -> List[ModelType]:
        """Return pages raws of model instances filtered by where_clause if provided.

        Args:
            skip (int): amount of raws to skip,
            limit (int): response raws maximum count,
            with_relations (bool): does return raws should load related objects,
           where_clause (SQLAlchemy.sql.ClauseElement): WHERE conditions value.

        Returns:
            model object instances in list paged by 'skip' and 'limit' args. Returns empty list if no raws founded.

        """
        query = self._with_relations_query(where_clause) if with_relations else self._query(where_clause)
        return await query.offset(skip).limit(limit).gino.all()  # noqa: gino tricks

    async def iterate_multi(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        with_relations: bool = True,
        where_clause: Optional[ClauseElement] = None
    ) -> AsyncIterator:
        """Returns same as "get_multi" method, except of replacing list to async iterable object."""
        query = self._with_relations_query(where_clause) if with_relations else self._query(where_clause)
        query = query.offset(skip).limit(limit)
        async with db.transaction():
            async for result in db.iterate(query):
                yield result

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        """Create model instance and save it into database.

        Args:
            obj_in (pydantic.BaseModel): instance creating validation schema.

        Returns:
            created db model instance.

        """
        return await self.model.create(**obj_in.dict(exclude_unset=True))

    @staticmethod
    async def update(db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        """Update in database instance fields values.

        Args:
            db_obj (gino.Model): instance of db model,
            obj_in (pydantic.BaseModel): instance updating validation schema.

        Returns:
            db model instance wth updated values.

        """
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        await db_obj.update(*update_data).apply()
        return db_obj

    async def remove(self, id_: int) -> ModelType:
        """Delete model instance related raw from database.

        Args:
            id_ (any): slug for search perform for,

        Returns:
            deleted db model instance (app's memory).

        """
        obj = await self.model.get(id_)
        await obj.delete()
        return obj
