from datetime import datetime

from Model.directoryvalue import DirectoryValue
from Repository.directoryvalue import DirectoryValueRepository
from schema import DirectoryValueInput, DirectoryValueType
from typing import Optional, List


class DirectoryValueService:

    @staticmethod
    async def getDirectoryValues(
            idDirectoryValue: Optional[List[int]] = None,
            idDirectory: Optional[List[int]] = None,
            longName: Optional[str] = None,
            shortName: Optional[str] = None,
            momentBegin: Optional[datetime] = None,
            momentEnd: Optional[datetime] = None
    ):
        return await DirectoryValueRepository.getDirectoryValues(
            idDirectoryValue,
            idDirectory,
            longName,
            shortName,
            momentBegin,
            momentEnd
        )

    @staticmethod
    async def add_directoryvalue(directoryvalue_data: DirectoryValueInput):
        directoryvalue = DirectoryValue()
        directoryvalue.id_directoryvalue = directoryvalue_data.id_directoryvalue
        directoryvalue.id_directory = directoryvalue_data.id_directory
        directoryvalue.long_name = directoryvalue_data.long_name
        directoryvalue.short_name = directoryvalue_data.short_name
        # parameter.moment_begin = parameter_data.moment_begin
        # parameter.moment_end = parameter_data.moment_end
        directoryvalue.moment_begin = directoryvalue_data.moment_begin if directoryvalue_data.moment_begin else datetime.now()
        directoryvalue.moment_end = directoryvalue_data.moment_end if directoryvalue_data.moment_end else datetime.strptime(
            '9999-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')

        await DirectoryValueRepository.create(directoryvalue)

        return DirectoryValueType(id_directoryvalue=directoryvalue.id_directoryvalue,
                                  id_directory=directoryvalue.id_directory,
                                  long_name=directoryvalue.long_name,
                                  short_name=directoryvalue.short_name, moment_begin=directoryvalue.moment_begin,
                                  moment_end=directoryvalue.moment_end)

    @staticmethod
    async def get_all():
        list_directoryvalue = await DirectoryValueRepository.get_all_directoryvalues()
        return [
            DirectoryValueType(id_directoryvalue=directoryvalue.id_directoryvalue,
                               id_directory=directoryvalue.id_directory,
                               long_name=directoryvalue.long_name, short_name=directoryvalue.short_name,
                               moment_begin=directoryvalue.moment_begin, moment_end=directoryvalue.moment_end)
            for directoryvalue in
            list_directoryvalue]

    @staticmethod
    async def get_by_id(directoryvalue_id: int):
        directoryvalue = await DirectoryValueRepository.get_directoryvalue_by_id(directoryvalue_id)
        return DirectoryValueType(id_directoryvalue=directoryvalue.id_directoryvalue,
                                  id_directory=directoryvalue.id_directory,
                                  long_name=directoryvalue.long_name,
                                  short_name=directoryvalue.short_name, moment_begin=directoryvalue.moment_begin,
                                  moment_end=directoryvalue.moment_end)

    @staticmethod
    async def delete(directoryvalue_id: int):
        await DirectoryValueRepository.delete(directoryvalue_id)
        return f'Successfully deleted data by id {directoryvalue_id}'

    @staticmethod
    async def update(directoryvalue_id: int, directoryvalue_data: DirectoryValueInput):
        directoryvalue = DirectoryValue()
        directoryvalue.id_directory = directoryvalue_data.id_directory
        directoryvalue.long_name = directoryvalue_data.long_name
        directoryvalue.short_name = directoryvalue_data.short_name
        directoryvalue.moment_begin = directoryvalue_data.moment_begin
        directoryvalue.moment_end = directoryvalue_data.moment_end
        await DirectoryValueRepository.update(directoryvalue_id, directoryvalue)

        return f'Successfully updated data by id {directoryvalue_id}'
