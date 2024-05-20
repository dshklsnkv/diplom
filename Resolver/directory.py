from typing import Optional, List
from schema import DirectoryType
from Service.directory import DirectoryService
from datetime import datetime

"""Класс функций резолверов для Параметров"""


class DirectoryResolver:
    """"Получить параметры"""

    @staticmethod
    async def getDirectorys(
            idDirectory: Optional[List[int]] = None,
            nameDirectory: Optional[str] = None,
            momentBegin: Optional[datetime] = None,
            momentEnd: Optional[datetime] = None
    ) -> List[DirectoryType]:
        directorys = await DirectoryService.getDirectorys(
            idDirectory=idDirectory,
            nameDirectory=nameDirectory,
            momentBegin=momentBegin,
            momentEnd=momentEnd
        )
        return [DirectoryType(
            id_directory=directory.id_directory,
            name_directory=directory.name_directory,
            moment_begin=directory.moment_begin,
            moment_end=directory.moment_end
        ) for directory in directorys]
