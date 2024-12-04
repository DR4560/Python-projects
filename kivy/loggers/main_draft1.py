import logging
import Module2

# filemode changed to overwrite:
# filemode ="w"

def main():
# Entry app main point
    logging.basicConfig(filename="kivy_main_sample.log", level=logging.INFO)
    logging.info("The program started")
    result = Module2.add(5, 6)
    logging.info("The program was build successfully")
    log = logging.getLogger("ex")  # ex is a logger object
    # 5 logging levels are exist:


    logging.debug("Debug message")
    logging.info("Additional info message")
    logging.warning("Warning message")
    logging.error("AN ERROR")
    logging.critical("Critical message")

    try:
        raise RuntimeError
    except RuntimeError:
        log.exception("Error!")

if __name__ == "__main__":
    main()