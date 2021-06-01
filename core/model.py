import json
import requests
import socket
import base64


class BankIdModel:
    def __init__(self, ssn=None, amount=None):
        self.ssn = ssn
        self.amount = amount
        self.rootUrl = "https://appapi2.test.bankid.com" # test url
        # self.rootUrl = "https://appapi2.bankid.com" # production url
        self.client = requests.Session()
        self.client.verify = 'appapi.test.bankid.com.pem' # test issuer server cert
        # self.client.verify = 'appapi.bankid.com.pem' # production issuer server cert
        self.client.cert = ('bankid-test.crt.pem', 'bankid-test.key.pem')
        self.client.headers = {'content-type': 'application/json'}
        self.hintcode = ""
        self.status = ""

    def auth(self):
        url = self.rootUrl + "/rp/v5.1/auth"
        ip = socket.gethostbyname(socket.gethostname())

        payload = {
            "personalNumber": "{}".format(self.ssn),
            "endUserIp": "{}".format(ip),
            "requirement": {"allowFingerprint": True},
        }
        self.rpResponse = self.client.post(url, json=payload)
        return self.rpResponse.json()

    def sign(self):
        url = self.rootUrl + "/rp/v5.1/sign"
        ip = socket.gethostbyname(socket.gethostname())

        message = f"Köp hos Testföretag AB på {self.amount} SEK"

        encoded_message = base64.b64encode(message.encode('utf-8'))
        encoded_message = encoded_message.decode('utf-8')  # take away binary
        # print(encoded_message)
        payload = {
            "personalNumber": "{}".format(self.ssn),
            "endUserIp": "{}".format(ip),
            "requirement": {"allowFingerprint": True},
            "userVisibleData": "{}".format(encoded_message)
            # "userVisibleDataFormat": "simpleMarkdownV1"
        }
        self.rpResponse = self.client.post(url, json=payload)

        # print(self.rpResponse.status_code)
        # print(self.rpResponse.json())

        return self.rpResponse.json()

    def collect(self):
        url = self.rootUrl + "/rp/v5.1/collect"
        payload = {
            "orderRef": "{}".format(self.rpResponse.json()['orderRef'])}
        return self.client.post(url, json=payload).json()

    def cancel(self):
        url = self.rootUrl + "/rp/v5.1/cancel"
        payload = {
            "orderRef": "{}".format(self.rpResponse.json()['orderRef'])}
        return self.client.post(url, json=payload).json()


if __name__ == '__main__':
    model = BankIdModel(amount="500.00")
    model.sign()
