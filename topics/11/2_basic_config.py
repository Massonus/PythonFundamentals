# basicConfig (**kwargs)
# метод для налаштування 
# журналу логів

# import logging

# logging.basicConfig(level = logging.DEBUG)
# logging.debug('This will get logged')

###############################
# запи логів в файл
#################################

# import logging

# logging.basicConfig(filename = 'app.log', 
#                     filemode = 'w', 
#                     format = '%(name)s :-: %(levelname)s :-: %(message)s')

# logging.warning('This will get logged to a file')

################################
# формат виводу
# ідентифікатор ID процесу
################################

# import logging

# logging.basicConfig(format = '%(process)d-%(levelname)s-%(message)s')

# logging.warning('This is a Warning')


###################################
# додавання інформації
# про час створення запису
##############################
# import logging

# logging.basicConfig(format = '%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')

###########################
# формат дати можна змінити
# з допомогою атрибута datefmt
#############################
# import logging

# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')

##############################
# логування змінних
# додавання динамічної
# інформації з застосунку
#############################

# import logging

# name = 'User_name999'

# logging.error(f'{name} raised an error')

