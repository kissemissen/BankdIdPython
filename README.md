# BankdId Client and UI for Python3.x
A small repository that offers a client implementation for Swedish BankId with both auth and sign. TO BE USED WITH PYTHON3.

The repositoy is structured with app.py being the text based user interface, model.py containing the Client which connects to the BankdId services and the certificates and keys which are used to authenticate the rest api calls to the BankId server.

<b>To run the app:</b><br />
N.B! Using a virtual environment is recommended to isolate the plugins. This step is not necessary and the requirements.txt can be used to install the dependencies directly on the Python installation.
1. Clone the repository into a folder of your choice <br />
2. Create a virtual env (not required, you can read more on how to create a venv at https://docs.python.org/3/library/venv.html) <br />
3. Run pip install -r requirements.txt <br />
4. Run python app.py <br />

Please note that full error handling is not implemented. As an example, the app will crash if the user i.e. tries to select collect before an auth or sign has been initialized.

<b>app.py</b><br />
The auth and sign functions require a Swedish Social Security Number (SSN, personnummer) to be entered. The sign option also takes an amount to be signed. <br />
To create an SSN, please follow the instructions given at the BankId developer homepage: https://www.bankid.com/utvecklare/rp-info. <br />

<b>License information</b><br />
This distribution is released with the conditions of the MIT License.

All trademarks referenced herein are property of their respective holders.

<h3>Happy coding!</h3>
