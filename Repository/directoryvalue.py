from datetime import datetime
from Model.directoryvalue import DirectoryValue
from config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete


class DirectoryValueRepository:

    @staticmethod
    async def create(directoryvalue_data: DirectoryValue):
        async with db as session:
            async with session.begin():
                session.add(directoryvalue_data)
            await db.commit_rollback()

    @staticmethod
    async def get_directoryvalue_by_id(directoryvalue_id: int):
        async with db as session:
            stmt = select(DirectoryValue).where(DirectoryValue.id_directoryvalue == directoryvalue_id)
            result = await session.execute(stmt)
            directoryvalue = result.scalars().first()
            return directoryvalue

    @staticmethod
    async def get_all_directoryvalues():
        async with db as session:
            query = select(DirectoryValue)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(directoryvalue_id: int, directoryvalue_data: DirectoryValue):
        async with db as session:
            stmt = select(DirectoryValue).where(DirectoryValue.id_directoryvalue == directoryvalue_id)
            result = await session.execute(stmt)

            directoryvalue = result.scalars().first()
            directoryvalue.id_directory = directoryvalue_data.id_directory
            directoryvalue.long_name = directoryvalue_data.long_name
            directoryvalue.short_name = directoryvalue_data.short_name
            directoryvalue.moment_begin = directoryvalue_data.moment_begin
            directoryvalue.moment_end = directoryvalue_data.moment_end

            # query = sql_update(Parameter).where(Parameter.id_parameter == parameter_id).values({
            #     "name_parameter": "123",  "id_place_izmer": 11}).execution_options(synchronize_session="fetch")
            query = sql_update(DirectoryValue).where(DirectoryValue.id_directoryvalue == directoryvalue_id).values(
                # **parameter.dict()).execution_options(synchronize_session="fetch")

                id_directoryvalue=directoryvalue.id_directoryvalue,
                long_name=directoryvalue.long_name,
                short_name=directoryvalue.short_name,
                moment_begin=directoryvalue.moment_begin,
                moment_end=directoryvalue.moment_end).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(directoryvalue_id: int):
        async with db as session:
            query = sql_delete(DirectoryValue).where(DirectoryValue.id_directoryvalue == directoryvalue_id)
            await session.execute(query)
            await db.commit_rollback()
