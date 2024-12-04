import logging
import logging.config
import Module2

def main():
    """Based on https://python-scripts.com/logging-python """
    logging.config.fileConfig('config.ini')
    logger = logging.getLogger("SampleApp")

    logger.setLevel(logging.INFO)  # info level - basic logged message


    logger.info("Program started successfully")

    result = Module2.add(1, 2)
    # Лучше добавлять результат сложения в лог

    logger.info("New commit has been created")





if __name__ == "__main__":
    main()