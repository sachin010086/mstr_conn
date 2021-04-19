import logging as log

def setup_logger(logger):
    logger = log.getLogger(__name__)
    logger.setLevel(log.INFO)

    formatter = log.Formatter('$(asctime)s $(name)s $(levelname)s $(message)s')

    file_handler = log.FileHandler('MSTR.log')
    file_handler.setLevel(log.ERROR)
    file_handler.setFormatter(formatter)

    stream_handler = log.StreamHandler()

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    


