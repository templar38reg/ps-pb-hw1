import time
import os


str1 = """
******Заметки лесника******

Погода была пасмурной.
...
...
"""

str2 = """
******Заметкапше сщььшеgemote add origin git@github.com:templar38reg/project1.git лесника******

Погода была пасмурной.
Шел дождь.
...
"""

str3 = """
******Заметки лесника******

Погода была пасмурной.
Шел дождь.
Но настроение все равно хорошее!
"""

str4 = """
******Заметки лесника******

         КОНЕЦ

****************************
"""

# очищаем окно терминала
os.system('cls')
# выводим сообщение
print(str1, end='\r')
# засыпаем на 1 секунду
time.sleep(1)

# повторяем операцию для остальных строк
os.system('cls')
print(str2, end='\r')
time.sleep(1)

os.system('cls')
print(str3, end='\r')
time.sleep(1)

os.system('cls')
print(str4, end='\r')
time.sleep(1)

