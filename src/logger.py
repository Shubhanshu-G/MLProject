import logging

import os

from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")



print("Logging done")

# import csv
# import os
# from datetime import datetime

# # Create Logs folder
# LOG_DIR = "logs"
# os.makedirs(LOG_DIR, exist_ok=True)

# # CSV file
# LOG_FILE = os.path.join(LOG_DIR, "application_log.csv")

# # CSV Header
# HEADER = [
#     "Timestamp",
#     "Level",
#     "Module",
#     "Function",
#     "Line No",
#     "Message"
# ]

# # Create file with header if it doesn't exist
# if not os.path.exists(LOG_FILE):
#     with open(LOG_FILE, "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(HEADER)


# def log(level, module, function, line_no, message):
#     """Write log information into CSV."""

#     with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)

#         writer.writerow([
#             datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             level,
#             module,
#             function,
#             line_no,
#             message
#         ])


# if __name__ == "__main__":

#     log(
#         level="INFO",
#         module=__name__,
#         function="main",
#         line_no=42,
#         message="Logging has started"
#     )

#     print("Logging Done")