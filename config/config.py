# Copyright 2018 <Quenos Blockchain R&D KFT>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the 
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import configparser
import os.path


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SystemConfiguration(object, metaclass=Singleton):

    def __init__(self):
        self._admin_macaroon_directory = ''
        self._tls_cert_directory = ''
        self._lnd_rpc_address = ''
        self._lnd_rpc_port = ''
        pass

    @property
    def admin_macaroon_directory(self):
        return self._admin_macaroon_directory

    @admin_macaroon_directory.setter
    def admin_macaroon_directory(self, value):
        self._admin_macaroon_directory = value

    @property
    def tls_cert_directory(self):
        return self._tls_cert_directory

    @tls_cert_directory.setter
    def tls_cert_directory(self, value):
        self._tls_cert_directory = value

    @property
    def lnd_rpc_address(self):
        return self._lnd_rpc_address

    @lnd_rpc_address.setter
    def lnd_rpc_address(self, value):
        self._lnd_rpc_address = value

    @property
    def lnd_rpc_port(self):
        return self._lnd_rpc_port

    @lnd_rpc_port.setter
    def lnd_rpc_port(self, value):
        self._lnd_rpc_port = value

    def read_config(self):
        if not os.path.isfile('./config/conductor.conf'):
            raise FileNotFoundError
        config = configparser.ConfigParser()
        config.read('./config/conductor.conf')
        self._admin_macaroon_directory = config['DIRECTORIES']['admin_macaroon']
        self._tls_cert_directory = config['DIRECTORIES']['tls_cert']
        self._lnd_rpc_address = config['ADDRESSES']['lnd_rpc_address']
        self._lnd_rpc_port = config['ADDRESSES']['lnd_rpc_port']

    def write_config(self):
        config = configparser.ConfigParser()
        config['DIRECTORIES'] = {'admin_macaroon': self._admin_macaroon_directory,
                                 'tls_cert': self._tls_cert_directory}
        config['ADDRESSES'] = {'lnd_rpc_address': self._lnd_rpc_address,
                               'lnd_rpc_port': self._lnd_rpc_port}
        with open('./config/conductor.conf', 'w') as configfile:
            config.write(configfile)
