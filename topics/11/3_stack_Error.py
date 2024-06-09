#######################################
#логування стеку виконання застосунку
#######################################

# import logging

# first_number = 25
# second_number = 0

# try:
#     result = first_number / second_number

# except Exception as e:
#     logging.error("Exception occurred", exc_info = True)
  
#################################

import logging

first_number = 25
second_number = 0

try:
  result = first_number / second_number

except Exception as e:
    # logging.error("Exception occurred", exc_info=True)
    
    logging.basicConfig(filename = 'app.log', 
                        filemode = 'w', 
                        format = '%(name)s - %(levelname)s - %(message)s')
    
    logging.error("Exception occurred", exc_info = True)

# ##################################
#logging.exception() ==
#logging.error (exc_info = True)
#
###################################
# import logging

# first_number = 25
# second_number = 0
# try:
#     result = first_number / second_number

# except Exception as e:
#   logging.exception("Exception occurred")