import logging
class CliniqueLogegr:
    logging.basicConfig(filename='cliniqueErrors.log', level = logging.ERROR)
    loggerError = logging.getLogger(__name__)