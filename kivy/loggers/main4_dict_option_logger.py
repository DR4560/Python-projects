import logging
import logging.config
import Module2

def main():
    """Based on https://python-scripts.com/logging-python """
    dictLogConfig = {
        "version":1,
        "handlers":{
            "fileHandler":{
                "class": "logging.FileHandler",
                "formatter": "myFormatter",
                "filename": "config2.log"
            }
        },
        "loggers": {
            "SampleApp":{
                "handlers": ["fileHandler"],
                "level": "INFO",
            }
        },
        "formatters": {
            "myFormatter": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }

    logging.config.dictConfig(dictLogConfig)

    logger = logging.getLogger("SampleApp")
    logger.info("Program started successfully")
    result = Module2.add(1, 2)
    logger.info("New commit has been created")



if __name__ == "__main__":
    main()