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

import codecs
import grpc
import os
from lightning import rpc_pb2_grpc as lnrpc, rpc_pb2 as ln
from config.config import SystemConfiguration


class LndAL(object):

    class LightningException(Exception):
        pass

    def __init__(self):
        pass

    @classmethod
    def get_rpc_data(cls):
        system_config = SystemConfiguration()
        cls.macaroon = codecs.encode(open(system_config.admin_macaroon_directory + '/admin.macaroon', 'rb').read(),
                                     'hex')
        os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
        cert = open(system_config.tls_cert_directory + '/tls.cert', 'rb').read()
        ssl_creds = grpc.ssl_channel_credentials(cert)
        channel = grpc.secure_channel(system_config.lnd_rpc_address + ':' + system_config.lnd_rpc_port, ssl_creds)
        cls.stub = lnrpc.LightningStub(channel)

    @classmethod
    def get_rpc_unlock_data(cls):
        cls.macaroon = codecs.encode(open('/home/coen/data/admin.macaroon', 'rb').read(), 'hex')
        os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
        cert = open('/home/coen/data/tls.cert', 'rb').read()
        ssl_creds = grpc.ssl_channel_credentials(cert)
        channel = grpc.secure_channel('192.168.0.110:10009', ssl_creds)
        cls.stub = lnrpc.WalletUnlockerStub(channel)

    @classmethod
    def describe_graph(cls):
        cls.get_rpc_data()
        request = ln.ChannelGraphRequest()
        return cls.stub.DescribeGraph(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def channel_balance(cls):
        cls.get_rpc_data()
        request = ln.ChannelBalanceRequest()
        return cls.stub.ChannelBalance(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def wallet_balance(cls):
        cls.get_rpc_data()
        request = ln.WalletBalanceRequest()
        return cls.stub.WalletBalance(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def list_channels(cls, active_only=False, inactive_only=False, public_only=False, private_only=False):
        cls.get_rpc_data()
        request = ln.ListChannelsRequest(
            active_only=active_only,
            inactive_only=inactive_only,
            public_only=public_only,
            private_only=private_only)
        return cls.stub.ListChannels(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def closed_channels(cls,
                        cooperative=False,
                        local_force=False,
                        remote_force=False,
                        breach=False,
                        funding_canceled=False):
        cls.get_rpc_data()
        request = ln.ClosedChannelsRequest(cooperative=cooperative,
                                           local_force=local_force,
                                           remote_force=remote_force,
                                           breach=breach,
                                           funding_canceled=funding_canceled)
        return cls.stub.ClosedChannels(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def get_transactions(cls):
        cls.get_rpc_data()
        request = ln.GetTransactionsRequest()
        return cls.stub.GetTransactions(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def get_info(cls):
        cls.get_rpc_data()
        request = ln.GetInfoRequest()
        return cls.stub.GetInfo(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def forwarding_history(cls, start_time=0, end_time=0, index_offset=0, num_max_events=0):
        cls.get_rpc_data()
        request = ln.ForwardingHistoryRequest(
            start_time=start_time,
            end_time=end_time,
            index_offset=index_offset,
            num_max_events=num_max_events)
        return cls.stub.ForwardingHistory(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def query_routes(cls, pub_key, fee_limit, amt=0, num_routes=10, final_cltv_delta=0 ):
        cls.get_rpc_data()
        request = ln.QueryRoutesRequest(
            pub_key=pub_key,
            amt=amt,
            num_routes=num_routes,
            fee_limit=fee_limit,
            final_cltv_delta=final_cltv_delta)
        return cls.stub.QueryRoutes(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def decode_pay_req(cls, pay_req):
        cls.get_rpc_data()
        request = ln.PayReqString(pay_req=pay_req)
        return cls.stub.DecodePayReq(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def new_address(cls, type):
        cls.get_rpc_data()
        request = ln.NewAddressRequest(type=type)
        return cls.stub.NewAddress(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def unlock_wallet(cls, wallet_password, recovery_window=0):
        cls.get_rpc_unlock_data()
        request = ln.UnlockWalletRequest(wallet_password=wallet_password, recovery_window=recovery_window)
        return cls.stub.UnlockWallet(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def update_channel_policy(cls, chan_point, base_fee_msat, fee_rate, time_lock_delta ):
        cls.get_rpc_data()
        request = ln.PolicyUpdateRequest(chan_point=chan_point,
                                         base_fee_msat=base_fee_msat,
                                         fee_rate=fee_rate,
                                         time_lock_delta=time_lock_delta)
        return cls.stub.UpdateChannelPolicy(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def get_node_info(cls, pub_key):
        cls.get_rpc_data()
        request = ln.NodeInfoRequest(pub_key=pub_key)
        return cls.stub.GetNodeInfo(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def get_chan_info(cls, chan_id):
        cls.get_rpc_data()
        request = ln.ChanInfoRequest(chan_id=chan_id)
        return cls.stub.GetChanInfo(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def get_fee_report(cls):
        cls.get_rpc_data()
        request = ln.FeeReportRequest()
        return cls.stub.FeeReport(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def pending_channels(cls):
        cls.get_rpc_data()
        request = ln.PendingChannelsRequest()
        return cls.stub.PendingChannels(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def connect(cls, addr, perm=False):
        cls.get_rpc_data()
        request = ln.ConnectPeerRequest(addr=addr)
        return cls.stub.ConnectPeer(request, metadata=[('macaroon', cls.macaroon)])

    @classmethod
    def open_channel(cls,
                     node_pub_key,
                     node_pub_key_string,
                     local_funding_amount,
                     push_sat=0,
                     target_conf=0,
                     sat_per_byte=0,
                     private=False,
                     min_htlc_msat=0,
                     remote_csv_delay=0,
                     min_confs=1,
                     spend_unconfirmed=False):
        response = []
        cls.get_rpc_data()
        request = ln.OpenChannelRequest(node_pubkey=node_pub_key,
                                        node_pubkey_string=node_pub_key_string,
                                        local_funding_amount=local_funding_amount,
                                        push_sat=push_sat,
                                        target_conf=target_conf,
                                        sat_per_byte=sat_per_byte,
                                        private=private,
                                        min_htlc_msat=min_htlc_msat,
                                        remote_csv_delay=remote_csv_delay)

        for r in cls.stub.OpenChannel(request, metadata=[('macaroon', cls.macaroon)]):
            # TODO: test the below
            response.append(r)
            if r:
                break
        return response

    @classmethod
    def close_channel(cls, channel_point, force=False, target_conf=0, sat_per_byte=0):
        response = []
        cls.get_rpc_data()
        request = ln.CloseChannelRequest(channel_point=channel_point,
                                         force=force,
                                         target_conf=target_conf,
                                         sat_per_byte=sat_per_byte)
        for r in cls.stub.CloseChannel(request, metadata=[('macaroon', cls.macaroon)]):
            # TODO: test the below
            response.append(r)
            if r:
                break
        return response

    @staticmethod
    def set_fee_limit(fixed=0, percent=0):
        val = {"fixed": fixed, "percent": percent}
        return val


if __name__ == "__main__":
    sc = SystemConfiguration()
    sc.admin_macaroon_directory = '/home/coen/data'
    sc.tls_cert_directory = '/home/coen/data'
    sc.lnd_rpc_address = '192.168.0.110'
    sc.lnd_rpc_port = '10009'
    r = LndAL.pending_channels()
    print(r)
