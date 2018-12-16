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

        self._default_sat_per_byte = 0
        self._default_time_lock_delta = 144
        self._default_base_fee_msat = 1000
        self._default_fee_rate = 0.000001

        self._policy1 = None
        self._policy2 = None
        self._policy3 = None

        self._channel_info_update_needed = False

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

    @property
    def default_sat_per_byte(self):
        return self._default_sat_per_byte

    @default_sat_per_byte.setter
    def default_sat_per_byte(self, value):
        self._default_sat_per_byte = value

    @property
    def default_time_lock_delta(self):
        return self._default_time_lock_delta

    @default_time_lock_delta.setter
    def default_time_lock_delta(self, value):
        self._default_time_lock_delta = value

    @property
    def default_base_fee_msat(self):
        return self._default_base_fee_msat

    @default_base_fee_msat.setter
    def default_base_fee_msat(self, value):
        self._default_base_fee_msat = value

    @property
    def default_fee_rate(self):
        return self._default_fee_rate

    @default_fee_rate.setter
    def default_fee_rate(self, value):
        self._default_fee_rate = value

    @property
    def policy1(self):
        return self._policy1

    @policy1.setter
    def policy1(self, value):
        self._policy1 = value

    @property
    def policy2(self):
        return self._policy2

    @policy2.setter
    def policy2(self, value):
        self._policy2 = value

    @property
    def policy3(self):
        return self._policy3

    @policy3.setter
    def policy3(self, value):
        self._policy3 = value

    @property
    def channel_info_update_needed(self):
        return self._channel_info_update_needed

    @channel_info_update_needed.setter
    def channel_info_update_needed(self, value):
        self._channel_info_update_needed = value

    def read_config(self):
        if not os.path.isfile('./config/conductor.conf'):
            raise FileNotFoundError
        config = configparser.ConfigParser()
        config.read('./config/conductor.conf')
        self._admin_macaroon_directory = config['DIRECTORIES']['admin_macaroon']
        self._tls_cert_directory = config['DIRECTORIES']['tls_cert']
        self._lnd_rpc_address = config['ADDRESSES']['lnd_rpc_address']
        self._lnd_rpc_port = config['ADDRESSES']['lnd_rpc_port']

        self._default_sat_per_byte = config['SETTINGS']['default_sat_per_byte']
        self._default_base_fee_msat = config['SETTINGS']['default_base_fee_msat']
        self._default_fee_rate = config['SETTINGS']['default_fee_rate']
        self._default_time_lock_delta = config['SETTINGS']['default_time_lock_delta']

        policy1_perc = config['POLICY']['policy1_perc']
        policy1_base_fee = config['POLICY']['policy1_base_fee']
        policy1_fee_rate = config['POLICY']['policy1_fee_rate']

        self._policy1 = {'perc': policy1_perc, 'base_fee': policy1_base_fee, 'fee_rate': policy1_fee_rate}

        policy2_perc = config['POLICY']['policy2_perc']
        policy2_base_fee = config['POLICY']['policy2_base_fee']
        policy2_fee_rate = config['POLICY']['policy2_fee_rate']

        self._policy2 = {'perc': policy2_perc, 'base_fee': policy2_base_fee, 'fee_rate': policy2_fee_rate}

        policy3_perc = config['POLICY']['policy3_perc']
        policy3_base_fee = config['POLICY']['policy3_base_fee']
        policy3_fee_rate = config['POLICY']['policy3_fee_rate']

        self._policy3 = {'perc': policy3_perc, 'base_fee': policy3_base_fee, 'fee_rate': policy3_fee_rate}

    def write_config(self):
        config = configparser.ConfigParser()
        config['DIRECTORIES'] = {'admin_macaroon': self._admin_macaroon_directory,
                                 'tls_cert': self._tls_cert_directory}

        config['ADDRESSES'] = {'lnd_rpc_address': self._lnd_rpc_address,
                               'lnd_rpc_port': self._lnd_rpc_port}

        config['SETTINGS'] = {'default_sat_per_byte': self._default_sat_per_byte,
                              'default_base_fee_msat': self._default_base_fee_msat,
                              'default_fee_rate': self._default_fee_rate,
                              'default_time_lock_delta': self._default_time_lock_delta}

        config['POLICY'] = {'policy1_perc': self._policy1['perc'],
                            'policy1_base_fee': self._policy1['base_fee'],
                            'policy1_fee_rate': self._policy2['fee_rate'],
                            'policy2_perc': self._policy2['perc'],
                            'policy2_base_fee': self._policy2['base_fee'],
                            'policy2_fee_rate': self._policy2['fee_rate'],
                            'policy3_perc': self._policy3['perc'],
                            'policy3_base_fee': self._policy3['base_fee'],
                            'policy3_fee_rate': self._policy3['fee_rate'],
                            }

        with open('./config/conductor.conf', 'w') as configfile:
            config.write(configfile)
