# 5 рівнів серйозності,
# які вказують важливість 
# події
# на кожному рівні є
# свій метод, який можна
# використовувати для логування
# подій на відповідному рівні 
# серйозності 

import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')