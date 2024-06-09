
# функція рівня модуля logging.getLogger(name)
# створює об'єкти класу Logger
# (користувацький logger з ім'ям example_logger,
# але на відміну від кореневого логера,
# користувацький logger не можна 
# налаштувати з допомогою basicConfig(). 
# його налаштовують з 
# допомогою Handlers і Formatters
################################################# 
 
# import logging

# logger = logging.getLogger('example_logger')
# logger.warning('This is a warning')




#######################
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')