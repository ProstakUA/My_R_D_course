# Файли
#
# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

from datetime import datetime

LOG_FILE_NAME_TIME = 'exception_log.log'

class MyCustomException(Exception):

    def __init__(self, sys_info_note="Custom exception is occurred"):
        self.sys_info_note = sys_info_note
        with open(LOG_FILE_NAME_TIME, 'a') as buff:
            print(f"{self.__class__.__name__} - {self.sys_info_note} Error at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", file=buff)
        super().__init__(self.sys_info_note)


raise MyCustomException