'''
for login more details check the documentation
its basicaaly for any excution is basically happen its hould be able to log all the information the execution and evrything kept in the file 
so we can track even the custom exception comes or any error comes we logged that into the custom files 
'''
import logging
import os
from datetime import datetime

LOG_FILES = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # so the file name is whetever date time is same as file name
Logs_path = os.path.join(os.getcwd(),"Logs",LOG_FILES) # log files created in current working directory
os.makedirs(Logs_path,exist_ok=True) # even there is an file append on it 

LOG_PATH_PATH=os.path.join(Logs_path,LOG_FILES)

logging.basicConfig(
    filename=LOG_PATH_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("logging done")