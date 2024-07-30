from typing import Union
from secure_function import parse_url, check_ssl, check_fake_db, decision_tree, check_web_risk

def is_link_secue(link: str) -> Union[str, None]:

    # Parse Link
    parse_result = parse_url.parse_url(link)
    base_url = parse_result['base_url']
    hostname = parse_result['hostname']
    scheme = parse_result['scheme']

    print(parse_result)
    print(base_url)
    print(hostname)

    # Check DB
    in_fake_db = check_fake_db.check_fake_url_db(hostname)
    print('------------------------')
    print('check db')
    if in_fake_db:
        return '100%'
        # return 'Fake or Phishing URL by database'

    # Check SSL
    ssl_url = check_ssl.check_ssl_certificate(base_url, hostname, scheme)
    print('------------------------')
    print('check ssl')
    if not ssl_url:
        return '100%'
        # return 'SSL certificate is not valid'

    # Check Google
    

    # Check Decision tree
    pass_dct = decision_tree.classify_url_content(base_url)
    print('------------------------')
    print('check dct')
    if not pass_dct:
        return '80%'
        # return 'Inapproprite content such as gambling'

    return None





# def check_google_safe_browsing(url):
#     return 'lee'


# def check_ssl_certificate(url):
#     return 'lee' 


# def check_fake_url_list(url):
#     return 'lee' 


# def check_url_content(url):
#     return 'lee'


# def check_url_safety(url):

#     # Check Google
#     check_google_safe_browsing()

#     # Check SSL
#     check_ssl_certificate()

#     # Check FAKE DB
#     check_fake_url_list()
    
#     # Check Butiful, Decision tree
#     check_url_content(url)