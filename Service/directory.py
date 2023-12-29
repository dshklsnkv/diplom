from datetime import datetime

from Model.directory import Directory
from Repository.directory import DirectoryRepository
from schema import DirectoryInput, DirectoryType


class DirectoryService:

    @staticmethod
    async def add_directory(directory_data: DirectoryInput):
        directory = Directory()
        directory.id_directory = directory_data.id_directory
        directory.name_directory = directory_data.name_directory
        # parameter.moment_begin = parameter_data.moment_begin
        # parameter.moment_end = parameter_data.moment_end
        directory.moment_begin = directory_data.moment_begin if directory_data.moment_begin else datetime.now()
        directory.moment_end = directory_data.moment_end if directory_data.moment_end else datetime.strptime(
            '9999-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')

        await DirectoryRepository.create(directory)

        return DirectoryType(id_directory=directory.id_directory, name_directory=directory.name_directory,
                             moment_begin=directory.moment_begin, moment_end=directory.moment_end)

    @staticmethod
    async def get_all():
        list_directory = await DirectoryRepository.get_all_directorys()
        return [DirectoryType(id_directory=directory.id_directory, name_directory=directory.name_directory,
                              moment_begin=directory.moment_begin, moment_end=directory.moment_end) for directory in
                list_directory]

    @staticmethod
    async def get_by_id(directory_id: int):
        directory = await DirectoryRepository.get_directory_by_id(directory_id)
        return DirectoryType(id_directory=directory.id_directory, name_directory=directory.name_directory,
                             moment_begin=directory.moment_begin, moment_end=directory.moment_end)

    @staticmethod
    async def delete(directory_id: int):
        await DirectoryRepository.delete(directory_id)
        return f'Successfully deleted data by id {directory_id}'

    @staticmethod
    async def update(directory_id: int, directory_data: DirectoryInput):
        directory = Directory()
        directory.name_directory = directory_data.name_directory
        directory.moment_begin = directory_data.moment_begin
        directory.moment_end = directory_data.moment_end
        await DirectoryRepository.update(directory_id, directory)

        return f'Successfully updated data by id {directory_id}'


