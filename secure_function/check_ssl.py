from typing import Union, Literal
from fastapi import HTTPException
import requests
import ssl
import socket
import certifi

# SSL socket calling
def validate_ssl_certificate(hostname: str) -> bool:
    print(hostname)

    if not hostname:
        return False

    context = ssl.create_default_context(cafile=certifi.where())
    try:
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssock.do_handshake()
                cert = ssock.getpeercert()
                return True
    except (ssl.SSLError, socket.error) as e:
        print(e)
        return False


# Function to check SSL certificate
def check_ssl_certificate(
        base_url: str, 
        hostname: str, 
        scheme: Union[Literal['http', 'https']]
) -> bool :

    if scheme == 'http':
        return False
    if scheme == 'https':
        if not validate_ssl_certificate(hostname):
            return False
    
        try:
            response = requests.get(base_url)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Error checking URL: {str(e)}")


