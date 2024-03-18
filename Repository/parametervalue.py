from datetime import datetime
from Model.parametervalue import ParameterValue
from config import async_db
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlmodel import SQLModel, select
from typing import List, Optional


class ParameterValueRepository:

    @staticmethod
    async def getParameterValues(
            idParameterDataSourse: Optional[List[int]] = None,
            momentChange: Optional[datetime] = None,
            value: Optional[List[int]] = None
    ):
        async with async_db() as session:
            query = select(ParameterValue)
            if idParameterDataSourse:
                query = query.filter(ParameterValue.id_parameterdatasourse.in_(idParameterDataSourse))
            if momentChange:
                query = query.filter(ParameterValue.moment_change.like(momentChange))
            if value:
                query = query.filter(ParameterValue.value.in_(value))
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def create(parametervalue_data: ParameterValue):
        async with async_db() as session:
            async with session.begin():
                session.add(parametervalue_data)
            await session.commit()

    @staticmethod
    async def get_parametervalue_by_id(parametervalue_id: int):
        async with async_db() as session:
            stmt = select(ParameterValue).where(
                ParameterValue.id_parameterdatasourse == parametervalue_id)
            result = await session.execute(stmt)
            parametervalue = result.scalars().first()
            return parametervalue

    @staticmethod
    async def get_all_parametervalues():
        async with async_db() as session:
            query = select(ParameterValue)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(parametervalue_id: int, parametervalue_data: ParameterValue):
        async with async_db() as session:
            stmt = select(ParameterValue).where(
                ParameterValue.id_parameterdatasourse == parametervalue_id)
            result = await session.execute(stmt)

            parametervalue = result.scalars().first()
            parametervalue.moment_change = parametervalue_data.moment_change
            parametervalue.value = parametervalue_data.value

            # query = sql_update(Parameter).where(Parameter.id_parameter == parameter_id).values({
            #     "name_parameter": "123",  "id_place_izmer": 11}).execution_options(synchronize_session="fetch")
            query = update(ParameterValue).where(
                ParameterValue.id_parameterdatasourse == parametervalue_id).values(
                # **parameter.dict()).execution_options(synchronize_session="fetch")
                moment_change=parametervalue.moment_change,
                value=parametervalue_data.value)

            await session.execute(query)
            await session.commit()

    @staticmethod
    async def delete(parametervalue_id: int):
        async with async_db() as session:
            query = delete(ParameterValue).where(
                ParameterValue.id_parameterdatasourse == parametervalue_id)
            await session.execute(query)
            await session.commit()
