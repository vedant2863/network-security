# import sys
# from networksecurity.logging import logger

# class NetworkSecurityException(Exception):
#     def __init__(self,error_message,error_details:sys):
#         super().__init__(error_message)
#         _, _, exc_tb = error_details
#         self.lineno = exc_tb.tb_lineno
#         self.file_name = exc_tb.tb_frame.f_code.co_filename
#         self.error_message = error_message

#     def __str__(self):
#         return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
#         self.file_name, self.lineno, str(self.error_message))


import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        exc_type, exc_value, exc_tb = sys.exc_info()  # Extract traceback details
        if exc_tb:  # Ensure traceback exists before accessing its attributes
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None
        self.error_message = error_message

    def __str__(self):
        return "Error occurred in script [{0}] at line [{1}] with message [{2}]".format(
            self.file_name if self.file_name else "Unknown",
            self.lineno if self.lineno else "Unknown",
            str(self.error_message)
        )
