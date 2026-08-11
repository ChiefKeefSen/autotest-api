import logging

import httpx_client
from tools.http.logger import get_logger

logger = logging.getLogger('AUTOTEST')  #создаем логгер
logger.setLevel(logging.DEBUG) #ставим нижний уровень логгера, он будет записывать все что выше
#DEBUG → INFO → WARNING → ERROR → CRITICAL

#handler = logging.FileHandler() это 2 вида handler, 1 пишет в файл другой в консоль
handler = logging.StreamHandler() #создание хэндлера
handler.setLevel(logging.DEBUG) #создание уровня хэндлера, он тоже пропускает все что выше

#                         время логирования имя логера     уровень       сообщение
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
handler.setFormatter(formatter) #привязка форматтера к хэндлеру
logger.addHandler(handler) # привязка хэндлера к логгеру
#этапы настройки логгера вот такие (от меньшего к большему)
#formatter - handler - logger
#вот такие
#logger - handler - formatter (настройки handler)


logger.debug("Это сообщение уровня DEBUG")
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
logger.error("Это сообщение уровня ERROR")
logger.critical("Это сообщение уровня CRITICAL")


def make_api_request():
    logger.info("Make API Request") #надо логировать до функции
    client = ...#ну и логирование не должно быть избыточным, надо аккуратно
    client.get(...)

#FATAL = CRITICAL = 50
#ERROR = 40
#WARN = WARNING = 30
#INFO = 20
#DEBUG = 10
#NOTSET = 0


#logger можно случайно дублировать и если мы напишем так ->
#logger = get_logger("INPUT")
#logger = get_logger("INPUT")
#logger = get_logger("INPUT")
#logger = get_logger("INPUT")
#logger.info("Make API request") # <- то у нас каждое это сообщение по 4 раза выйдет
#logger.info("Got 200 response") #поэтому надо следить за тем сколько логгеров

#кстати в аллюр отчете будет файлик log и туда все логируется