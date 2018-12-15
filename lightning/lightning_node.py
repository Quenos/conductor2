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

import ipaddress
from lightning import lndAL
import re


class Node(object):
    def __init__(self,
                 num_channels=0,
                 total_capacity=0,
                 last_update=0,
                 pub_key='',
                 alias='',
                 addresses='',
                 color=''):
        self.num_channels = num_channels
        self.total_capacity = total_capacity
        self.last_update = last_update
        self.pub_key = pub_key
        self.alias = alias
        if addresses:
            try:
                self.address = "Unknown"
                for x in addresses:
                    self.address = x.addr
                    # test if the uri is IPv4, IPv6 or tor
                    if self.address.split(':')[0][-5:] == 'onion':
                        continue
                    if isinstance(ipaddress.ip_address(self.address.split(':')[0]), ipaddress.IPv4Address):
                        break
            except Exception as ex:
                raise ex
        else:
            self.address = 'private'
        self.color = color

    @staticmethod
    def find_node(pub_key=None, alias=None):
        ret_val = None
        if pub_key:
            try:
                response = lndAL.LndAL.get_node_info(pub_key)
                if response.node:
                    ret_val = Node(response.num_channels,
                                   response.total_capacity,
                                   response.node.last_update,
                                   response.node.pub_key,
                                   response.node.alias,
                                   response.node.addresses,
                                   response.node.color)
            except Exception as ex:
                if ex.__str__()[:12] != "<_Rendezvous":
                    raise ex
        elif alias:
            response = lndAL.LndAL.describe_graph()
            ret_val = []
            for node in response.nodes:
                search_result = re.search(alias, node.alias, re.IGNORECASE)
                if search_result is not None:
                    # the recursion is used because describe graph doesn't return the number of channels
                    # and the total capacity. So once the pub_key is known, the function is now called
                    # with the pub key as search parameter
                    ret_val.append({'pub_key': node.pub_key, 'alias': node.alias})
        return ret_val


class HomeNode(object):

    def __init__(self):
        info = lndAL.LndAL.get_info()
        self.name = info.alias
