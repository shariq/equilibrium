import httplib
import json
import decimal

class BTERConnection:
    domain = 'data.bter.com'
    def __init__(self, timeout=30):
        self.conn = httplib.HTTPSConnection(self.domain, timeout=timeout)

    def close(self):
        self.conn.close()

    def makeRequest(self, url, method='POST', extra_headers=None, params=''):
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        if extra_headers is not None:
            headers.update(extra_headers)

        self.conn.request(method, url, params, headers)
        response = self.conn.getresponse().read()

        return response

    def makeJSONRequest(self, url, method='POST', extra_headers=None, params=""):
        response = json.loads(self.makeRequest(url, method, extra_headers, params))
        return response

def parseJSONResponse(response):
    def parse_decimal(var):
        return decimal.Decimal(var)

    try:
        r = json.loads(response, parse_float=parse_decimal, parse_int=parse_decimal)
    except Exception as e:
        msg = "Error while attempting to parse JSON response: %s\nResponse:\n%r" % (e, response)
        raise Exception(msg)

    return r
