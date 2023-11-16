import sys
import logging

def error_message_detail(error_detail):
    exc_type, exc_value, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error type [{2}] error message[{3}]".format(
        file_name, exc_tb.tb_lineno, exc_type.__name__, str(exc_value)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_detail):
        super().__init__("Custom exception occurred")
        self.error_message = error_message_detail(error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        logging.error("Divide by zero")
        raise CustomException(sys.exc_info())



        
        