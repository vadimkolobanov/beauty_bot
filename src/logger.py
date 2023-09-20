import logging


def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(f"file_logs/{name}.log", mode='a')

    formatter = logging.Formatter("%(name)s %(asctime)s %(threadName)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info('\n\n\n\n')
    logger.info(f"Successfully created logger for {name}...")
    return logger