import logging


def create_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        filename='program.log', 
        format='%(asctime)s, %(levelname)s, %(message)s, %(name)s, %(funcName)s',
        encoding='utf-8'
    )

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    return logger
