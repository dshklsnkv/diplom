from typing import Optional, List
from schema import DirectoryValueType
from Service.directoryvalue import DirectoryValueService
from datetime import datetime

"""Класс функций резолверов для Параметров"""


class DirectoryValueResolver:
    """"Получить параметры"""

    @staticmethod
    async def getDirectoryValues(
            idDirectoryValue: Optional[List[int]] = None,
            idDirectory: Optional[List[int]] = None,
            longName: Optional[str] = None,
            shortName: Optional[str] = None,
            momentBegin: Optional[datetime] = None,
            momentEnd: Optional[datetime] = None
    ) -> List[DirectoryValueType]:
        directoryvalues = await DirectoryValueService.getDirectoryValues(
            idDirectoryValue=idDirectoryValue,
            idDirectory=idDirectory,
            longName=longName,
            shortName=shortName,
            momentBegin=momentBegin,
            momentEnd=momentEnd
        )
        return [DirectoryValueType(
            id_directoryvalue=directoryvalue.id_directoryvalue,
            id_directory=directoryvalue.id_directory,
            long_name=directoryvalue.long_name, short_name=directoryvalue.short_name,
            moment_begin=directoryvalue.moment_begin, moment_end=directoryvalue.moment_end
        ) for directoryvalue in directoryvalues]
