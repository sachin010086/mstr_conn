import requests, urllib3
from mstr_api.config.log_mod import setup_logger
import logging as log


from mstr_api.config.config import cfg, setup_logger

logger = log.getLogger(__name__)
setup_logger(logger)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_mstr_sesson():
    """
        This method is used to log-in and create session in MSTR
        url: this is the url link of MSTR server
        usr: this is the user of the MSTR account
        password: this is the password of the MSTR account
        return : it returns the token and cookies
    """    

    payload = {
        "username": cfg.MSTR.USER
        "password": cfg.MSTR.PASSWORD
        "loginMode": 1,
    }

    r = requests.post(cfg.MSTR.URL + 'auth/login', json = payload, verify = False)
    responseHeaders = r.headers
    responseCookies = r.cookies
    log.info(r.status_code)
    if 200 <= r.status_code < 300:
        return responseHeaders['X-MSTR-AuthToken'], responseCookies
    else:
        logger.error(f"MSTR login has failed {r}")
        raise Exception(f"MSTR session has failed {r}")

def close_MSTR_session(token: str, cookies: str):
    """
        This method is used to close the MSTR session
        url: this is the url link of MSTR server
        param token: Once RestAPI credential are valited, this is issue to the client
        param cookies: JSESSIONID is set by the JSP application server/IIS to track the user over te course of the its session
        return: this return if the session is valid or not
    """

    headers = {
        'content-Type': 'application/json',
        'Accept' : 'application/json',
        'X-MSTR-AuthToken': token
    }

    r = requests.post(cfg.MSTR.URL + 'auth/logout', header = headers , cookies = cookies, verify = False)
    if r.status_code == 204:
        return True
    else:
        logger.error(f"close session has failed {r}")
        raise Exception(f"close session has failed {r}")

def create_report_instance(token: str, project_id: str, report_id : str, offset=None, limit = 1000, body = None):
    """
        This method is used to create the instance to get the result of the report
        url: this is the url of the MSTR intelligent server
        param token: Once RestAPI credential are valited, this is issue to the client
        param cookies: JSESSIONID is set by the JSP application server/IIS to track the user over te course of the its session
        param project_id: Unique Id of the MSTR specific project
        param report_id: Unique Id of the MSTR specific report
        param offset: Starting point within the collection of returned results 
        param limit: max item retun from the single request
        param body: json structure as per MSTR             
        return: json if status code between 200 to 300
    """

    headers = {
        'content-Type': 'application/json',
        'Accept' : 'application/json',
        'X-MSTR-AuthToken': token,
        'X-MSTR-ProjectID': project_id        
    }

    param = {
        'offset': offset,
        'limit': limit
    }

    r = requests.post(cfg.MSTR.URL + report_id + '/instances/', 
    headers = headers,
    cookies = cookies, 
    params = params,
    json = body,
    verify = False)

    if 200 <= r.status_code = < 300:
        return r.json()

    else:
        logger.error(f"create report instance has failed {r}")
        raise Exception(f"create report instance has failed {r}")

def get_report_prompt(token: str, cookies: str, project_id : str, report_id :str, instance_id: str):
    """
        This method is used to get the report prompt for the specfic report
        url: this is the url of the MSTR intelligent server
        param token: Once RestAPI credential are valited, this is issue to the client
        param cookies: JSESSIONID is set by the JSP application server/IIS to track the user over te course of the its session
        param project_id: Unique Id of the MSTR specific project
        param report_id: Unique Id of the MSTR specific report
        param instance_id: instance ID of the MSTR report 
        return: json if status code between 200 to 300
    """
    headers = {
        'content-Type': 'application/json',
        'Accept' : 'application/json',
        'X-MSTR-AuthToken': token,
        'X-MSTR-ProjectID': project_id        
    }

    r = requests.get(cfg.MSTR.URL + '/reports/' + report_id + '/instance/' +instance_id + '/prompts',
    headers = headers,
    cookies = cookies,
    verify = False)

    if 200 <= r.status_code < 300:
        return r.json() 
    else:
        logger.error(f"Get report prompt has failed {r}")
        raise Exception(f"Get report prompt has failed {r}")

def answer_report_prompt(token: str, cookies: str, project_id : str, report_id :str, instance_id: str):
    """
        This method is used to provide reponse as per report prompt
        url: this is the url of the MSTR intelligent server
        param token: Once RestAPI credential are valited, this is issue to the client
        param cookies: JSESSIONID is set by the JSP application server/IIS to track the user over te course of the its session
        param project_id: Unique Id of the MSTR specific project
        param report_id: Unique Id of the MSTR specific report
        param instance_id: instance ID of the MSTR report 
        return: json if status code between 200 to 300
    """
    headers = {
        'content-Type': 'application/json',
        'Accept' : 'application/json',
        'X-MSTR-AuthToken': token,
        'X-MSTR-ProjectID': project_id        
    }    

    r = requests.put(cfg.MSTR.URL + '/reports/' + '/instance/' + instance_id + '/prompts/answers', 
    headers = headers,
    cookies = cookies,
    json = body,
    verify = False)

    if 200 <= r.status_code < 300:
        return True
    else:
        logger.error(f"Answer report has return {r}")
        raise Exception(f"Answer report has return {r}")

def get_report_instance(token: str, cookies: str, project_id : str, report_id :str, instance_id: str
                        offset = None, limit = 1000):
    """
        This method is used to provide reponse as per report prompt
        url: this is the url of the MSTR intelligent server
        param token: Once RestAPI credential are valited, this is issue to the client
        param cookies: JSESSIONID is set by the JSP application server/IIS to track the user over te course of the its session
        param project_id: Unique Id of the MSTR specific project
        param report_id: Unique Id of the MSTR specific report
        param instance_id: instance ID of the MSTR report 
        param offset: starting point within the collection of return result
        param limit: max item return from the single request
        return: json if status code between 200 to 300
    """
    headers = {
        'content-Type': 'application/json',
        'Accept' : 'application/json',
        'X-MSTR-AuthToken': token,
        'X-MSTR-ProjectID': project_id        
    }    

    params = {
        'offset': offset,
        'limit': limit
    }

    r = requests.put(cfg.MSTR.URL + '/reports/' + '/instance/' + instance_id, 
    headers = headers,
    cookies = cookies,
    params = params,
    json = body,
    verify = False)

    if 200 <= r.status_code < 300:
        return r.json()
    else:
        logger.error(f'Get report instance return an error {r}')
        raise Exception(f'Get report instance return an error {r}')
