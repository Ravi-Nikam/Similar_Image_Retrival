'''
for exception handling 
'''
import os
print(os.getcwd())
import sys   # any exception basically gatting the sys library  will have there information
# sys.path.append('D:/similar_image_retrival')
# Add the path of the src directory to the Python path
sys.path.append("../src")
from logger import logging
def error_message_details(error,error_details:sys): # any exception come there i wanna give my custom error msg  # error details already present in sys module 
    _,_,exc_tb=error_details.exc_info() # this basically the execution info , they give you threee information but 3 is important for us
    print(error_details.exc_info())
    file_name = exc_tb.tb_frame.f_code.co_filename # this give a file name of exception comes # for more details visit custom_exception handling in python documentation
    error_message = "error occured in python script name [{0}] line number [{1}] error message [{2}] ".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_details:sys):
        print("===========>",error_message,error_details)
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message   


if __name__=="__main__":
    try:
        a = 1/0
        print(a)
    except Exception as e:
        logging.info("Devide BY zero") 
        raise CustomException(e,sys)

'''
1 ) custom_exception(Exception) in this parameter exception is inherit parent exception 
2 ) whatever error message will come to error_message_details(error_message,error_details=error_details) rror_details=error_details basically track by :sys here  and it call the error_message_details funciotn  
3 ) and return value will be initlize to  self.error_message
4 ) def __str__(self): give error msg in string
5 ) so now when you get any error you have to just give try catch in or call custom_exceptioni function
'''