from datetime import datetime
from Model.directory import Directory
from config import async_db
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlmodel import SQLModel, select
from typing import Optional, List


class DirectoryRepository:

    @staticmethod
    async def getDirectorys(
            idDirectory: Optional[List[int]] = None,
            nameDirectory: Optional[str] = None,
            momentBegin: Optional[datetime] = None,
            momentEnd: Optional[datetime] = None
    ):
        async with async_db() as session:
            query = select(Directory)
            if idDirectory:
                query = query.filter(Directory.id_directory.in_(idDirectory))
            if nameDirectory:
                query = query.filter(Directory.name_directory.like(nameDirectory))
            if momentBegin:
                query = query.filter(Directory.moment_begin.like(momentBegin))
            if momentEnd:
                query = query.filter(Directory.moment_end.like(momentEnd))
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def create(directory_data: Directory):
        async with async_db() as session:
            async with session.begin():
                session.add(directory_data)
            await session.commit()

    @staticmethod
    async def get_directory_by_id(directory_id: int):
        async with async_db() as session:
            stmt = select(Directory).where(Directory.id_directory == directory_id)
            result = await session.execute(stmt)
            directory = result.scalars().first()
            return directory

    @staticmethod
    async def get_all_directorys():
        async with async_db() as session:
            query = select(Directory)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(directory_id: int, directory_data: Directory):
        async with async_db() as session:
            stmt = select(Directory).where(Directory.id_directory == directory_id)
            result = await session.execute(stmt)

            directory = result.scalars().first()
            directory.name_directory = directory_data.name_directory
            directory.moment_begin = directory_data.moment_begin
            directory.moment_end = directory_data.moment_end

            # query = sql_update(Parameter).where(Parameter.id_parameter == parameter_id).values({
            #     "name_parameter": "123",  "id_place_izmer": 11}).execution_options(synchronize_session="fetch")
            query = update(Directory).where(Directory.id_directory == directory_id).values(
                # **parameter.dict()).execution_options(synchronize_session="fetch")
                name_directory=directory.name_directory,
                moment_begin=directory.moment_begin,
                moment_end=directory.moment_end)

            await session.execute(query)
            await session.commit()

    @staticmethod
    async def delete(directory_id: int):
        async with async_db() as session:
            query = delete(Directory).where(Directory.id_directory == directory_id)
            await session.execute(query)
            await session.commit()
