import logging as log

from config.log_mod import setup_logger

logger = log.getLogger('mstr_report')
setup_logger(logger)

def get_report(duns_number: str, report_id: str):
    '''
    This mstr method call for external MSTR API to fetch report for give duns_number
    :param duns_number: duns number of the insured party
    :report_id: unique MSTR report id
    :return return the result of the chose report in json format
    '''
    # this is used to generate session for MSTR
    token, cookies = get_MSTR_session()

    