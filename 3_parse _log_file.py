import logging
import re
import os

logging.basicConfig(level = logging.DEBUG, filename='logging.log')
logging.debug("A Debug Logging Message")
logging.info("A Info Logging Message")
logging.warning("A Warning Logging Message-1")
logging.error("An Error Logging Message-1")
logging.critical("A Critical Logging Message")
logging.warning("A Warning Logging Message-2")
logging.error("An Error Logging Message-2")


fileName = "logging.log"
if os.path.isfile(fileName):
    with open(fileName, "r") as reader:
        data = reader.readlines()
    if (data):
        with open("error_Warning.log", "w") as writer:
            for x in data:
                print(x)
                x1 = re.findall("^WARNING:", x) or re.findall("^ERROR:", x)
                if x1:
                    writer.write(x)
