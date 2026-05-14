import urllib.request
import urllib.error

URL = "https://tools-httpstatus.pickup-services.com/"

class httpReqException(Exception):
    pass

def sendRequest(url: str):
    print(f"\nREQUEST: {url}")
    try:
        response = urllib.request.urlopen(url)
        response_code = response.getcode()
        response_body = response.read().decode("utf-8")

    except urllib.error.HTTPError as e:
        response_code = e.code
        response_body = e.read().decode("utf-8")

        print("ERROR!!!")
        print(f"HTTP STATUS CODE: {response_code}")
        print(f"BODY: {response_body}")

        raise httpReqException(
            f"Request failed with status code {response_code}"
        )
    
    if 100 <= response_code < 400:
        print(f"HTTP STATUS CODE: {response_code}")
        print(f"BODY: {response_body}")
    else:
        print(f"Request not successfull!!!\n. ERROR CODE: {response_code}")
        print(f"BODY: {response_body}")

dummy_requests = [
    f"{URL}/posts/1",
    f"{URL}/posts/2",
    f"{URL}/posts/3",
    f"{URL}/posts/4",
    f"{URL}/posts/5",
]

for url in dummy_requests:
    try:
        sendRequest(url)
    except httpReqException as e:
        print(f"EXCEPTION: {e}")
