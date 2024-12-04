import logging
import Module2

def main():
    logger = logging.getLogger("SampleApp")
    logger.setLevel(logging.INFO)  # info level - basic logged message

    # File handler (creating):
    file_handler = logging.FileHandler("app1.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # Исправлено 'lvlname' на 'levelname'
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)  # Add handler to logger object

    logger.info("Program started successfully")

    try:
        result = Module2.add(1, 2)
        logger.info("Result of addition: %s", result)  # Лучше добавлять результат сложения в лог
    except Exception as e:
        logger.error("An error occurred while adding: %s", e)

    logger.info("New commit has been created")

    # msgs logging
    logging.debug("This is a debug message")
    logging.info("Informational message")
    logging.error("An error has happened!")

    try:
        raise RuntimeError
    except RuntimeError:
        logger.exception("Error occurred!")# or caught!



    file_handler.close()

if __name__ == "__main__":
    main()