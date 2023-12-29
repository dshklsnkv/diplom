from datetime import datetime
from Model.directory import Directory
from config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete


class DirectoryRepository:

    @staticmethod
    async def create(directory_data: Directory):
        async with db as session:
            async with session.begin():
                session.add(directory_data)
            await db.commit_rollback()

    @staticmethod
    async def get_directory_by_id(directory_id: int):
        async with db as session:
            stmt = select(Directory).where(Directory.id_directory == directory_id)
            result = await session.execute(stmt)
            directory = result.scalars().first()
            return directory

    @staticmethod
    async def get_all_directorys():
        async with db as session:
            query = select(Directory)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(directory_id: int, directory_data: Directory):
        async with db as session:
            stmt = select(Directory).where(Directory.id_directory == directory_id)
            result = await session.execute(stmt)

            directory = result.scalars().first()
            directory.name_directory = directory_data.name_directory
            directory.moment_begin = directory_data.moment_begin
            directory.moment_end = directory_data.moment_end

            # query = sql_update(Parameter).where(Parameter.id_parameter == parameter_id).values({
            #     "name_parameter": "123",  "id_place_izmer": 11}).execution_options(synchronize_session="fetch")
            query = sql_update(Directory).where(Directory.id_directory == directory_id).values(
                # **parameter.dict()).execution_options(synchronize_session="fetch")
                name_directory=directory.name_directory,
                moment_begin=directory.moment_begin,
                moment_end=directory.moment_end).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(directory_id: int):
        async with db as session:
            query = sql_delete(Directory).where(Directory.id_directory == directory_id)
            await session.execute(query)
            await db.commit_rollback()