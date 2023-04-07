'''
for exception handling 
'''
import sys   # any exception basically gatting the sys library  will have there information
def error_message_details(error,error_details:sys): # any exception come there i wanna give my custom error msg  # error details already present in sys module 
    _,_,exc_tb=error_details.exc_info() # this basically the execution info , they give you threee information but 3 is important for us
    file_name = exc_tb.tb_frame.f_code.co_filename # this give a file name of exception comes # for more details visit custom_exception handling in python documentation
    error_message = "error occured in python script name [{0}] line number [{1}] error message [{2}] ".format()
    file_name,exc_tb.tb_lineno,str(error)
    return error_message

class custom_exception(Exception):
    def __init__(self, error_message,error_details:sys):
        super.__init__(error_message)

