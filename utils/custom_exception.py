import sys

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception = None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"

    def __str__(self):
        return self.error_message
    
    import sys
import inspect


# class CustomException(Exception):
#     def __init__(self, message: str, error_detail: Exception = None):
#         self.error_message = self.get_detailed_error_message(message, error_detail)
#         super().__init__(self.error_message)

#     @staticmethod
#     def get_detailed_error_message(message, error_detail):
#         # Get the caller's frame (where CustomException was instantiated)
#         frame = inspect.currentframe().f_back
#         file_name = frame.f_code.co_filename
#         line_number = frame.f_lineno
#         error_str = str(error_detail) if error_detail else "None"
#         return f"{message} | Error: {error_str} | File: {file_name} | Line: {line_number}"

#     def __str__(self):
#         return self.error_message