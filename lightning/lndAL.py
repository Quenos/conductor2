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
    _macaroon = None
    _stub = None

    class LightningException(Exception):
        '''
        grpc._channel._Rendezvous: <_Rendezvous of RPC that terminated with:
        status = StatusCode.UNAVAILABLE
        details = "Connect Failed"
        debug_error_string = "{"created":"@1542897540.782691997","description":"Failed to create subchannel","file":"src/core/ext/filters/client_channel/client_channel.cc","file_line":2721,"referenced_errors":[{"created":"@1542897540.782674777","description":"Pick Cancelled","file":"src/core/ext/filters/client_channel/lb_policy/pick_first/pick_first.cc","file_line":241,"referenced_errors":[{"created":"@1542897540.782478720","description":"Connect Failed","file":"src/core/ext/filters/client_channel/subchannel.cc","file_line":689,"grpc_status":14,"referenced_errors":[{"created":"@1542897540.782298936","description":"Handshake write failed","file":"src/core/lib/security/transport/security_handshaker.cc","file_line":347,"referenced_errors":[{"created":"@1542897540.782285043","description":"FD Shutdown","file":"src/core/lib/iomgr/lockfree_event.cc","file_line":194,"referenced_errors":[{"created":"@1542897540.782256648","description":"Handshake timed out","file":"src/core/lib/channel/handshaker.cc","file_line":290}]}]}]}]}]}"

        grpc._channel._Rendezvous: <_Rendezvous of RPC that terminated with:
        status = StatusCode.UNIMPLEMENTED
        details = "unknown service lnrpc.Lightning"
        debug_error_string = "{"created":"@1543505526.607347974","description":"Error received from peer","file":"src/core/lib/surface/call.cc","file_line":1017,"grpc_message":"unknown service lnrpc.Lightning","grpc_status":12}"

        grpc._channel._Rendezvous: <_Rendezvous of RPC that terminated with:
        status = StatusCode.UNKNOWN
        details = "peer 0321ad07ca4a3e590830ea835844820ea08b0e8d2e7dbdc32aa98e801ab9fd862e is not online"
        debug_error_string = "{"created":"@1547324967.579864705","description":"Error received from peer","file":"src/core/lib/surface/call.cc","file_line":1017,"grpc_message":"peer 0321ad07ca4a3e590830ea835844820ea08b0e8d2e7dbdc32aa98e801ab9fd862e is not online","grpc_status":2}"

        grpc._channel._Rendezvous: <_Rendezvous of RPC that terminated with:
        status = StatusCode.UNKNOWN
        details = "not enough witness outputs to create funding transaction, need 0.01 BTC only have 0.00004855 BTC  available"
        debug_error_string = "{"created":"@1547325316.221901640","description":"Error received from peer","file":"src/core/lib/surface/call.cc","file_line":1017,"grpc_message":"not enough witness outputs to create funding transaction, need 0.01 BTC only have 0.00004855 BTC  available","grpc_status":2}"

        grpc._channel._Rendezvous: <_Rendezvous of RPC that terminated with:
        status = StatusCode.UNKNOWN
        details = "no policy for outgoing channel 613822157507592192 "
        debug_error_string = "{"created":"@1547327609.724794018","description":"Error received from peer","file":"src/core/lib/surface/call.cc","file_line":1017,"grpc_message":"no policy for outgoing channel 613822157507592192 ","grpc_status":2}"

        '''
        pass

    @staticmethod
    def get_rpc_data():
        system_config = SystemConfiguration()
        LndAL._macaroon = codecs.encode(open(system_config.admin_macaroon_directory + '/admin.macaroon', 'rb').read(),
                                     'hex')
        os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
        cert = open(system_config.tls_cert_directory + '/tls.cert', 'rb').read()
        ssl_creds = grpc.ssl_channel_credentials(cert)
        channel = grpc.secure_channel(system_config.lnd_rpc_address + ':' + system_config.lnd_rpc_port, ssl_creds,
                                      options=[('grpc.max_send_message_length', 8000000),
                                               ('grpc.max_receive_message_length', 8000000)])
        LndAL._stub = lnrpc.LightningStub(channel)

    @staticmethod
    def get_rpc_unlock_data():
        system_config = SystemConfiguration()
        LndAL._macaroon = codecs.encode(open(system_config.admin_macaroon_directory + '/admin.macaroon', 'rb').read(),
                                        'hex')
        os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
        cert = open(system_config.tls_cert_directory + '/tls.cert', 'rb').read()
        ssl_creds = grpc.ssl_channel_credentials(cert)
        channel = grpc.secure_channel(system_config.lnd_rpc_address + ':' + system_config.lnd_rpc_port, ssl_creds)
        LndAL._stub = lnrpc.WalletUnlockerStub(channel)

    @staticmethod
    def describe_graph():
        LndAL.get_rpc_data()
        request = ln.ChannelGraphRequest()
        return LndAL._stub.DescribeGraph(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def channel_balance():
        LndAL.get_rpc_data()
        request = ln.ChannelBalanceRequest()
        return LndAL._stub.ChannelBalance(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def wallet_balance():
        LndAL.get_rpc_data()
        request = ln.WalletBalanceRequest()
        return LndAL._stub.WalletBalance(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def list_channels(active_only=False, inactive_only=False, public_only=False, private_only=False):
        LndAL.get_rpc_data()
        request = ln.ListChannelsRequest(
            active_only=active_only,
            inactive_only=inactive_only,
            public_only=public_only,
            private_only=private_only)
        return LndAL._stub.ListChannels(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def closed_channels(cooperative=False,
                        local_force=False,
                        remote_force=False,
                        breach=False,
                        funding_canceled=False):
        LndAL.get_rpc_data()
        request = ln.ClosedChannelsRequest(cooperative=cooperative,
                                           local_force=local_force,
                                           remote_force=remote_force,
                                           breach=breach,
                                           funding_canceled=funding_canceled)
        return LndAL._stub.ClosedChannels(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def get_transactions():
        LndAL.get_rpc_data()
        request = ln.GetTransactionsRequest()
        return LndAL._stub.GetTransactions(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def get_info():
        LndAL.get_rpc_data()
        request = ln.GetInfoRequest()
        return LndAL._stub.GetInfo(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def forwarding_history(start_time=0, end_time=0, index_offset=0, num_max_events=0):
        LndAL.get_rpc_data()
        request = ln.ForwardingHistoryRequest(
            start_time=start_time,
            end_time=end_time,
            index_offset=index_offset,
            num_max_events=num_max_events)
        return LndAL._stub.ForwardingHistory(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def query_routes(pub_key, fee_limit, amt=0, num_routes=10, final_cltv_delta=0):
        LndAL.get_rpc_data()
        request = ln.QueryRoutesRequest(
            pub_key=pub_key,
            amt=amt,
            num_routes=num_routes,
            fee_limit=fee_limit,
            final_cltv_delta=final_cltv_delta)
        return LndAL._stub.QueryRoutes(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def decode_pay_req(pay_req):
        LndAL.get_rpc_data()
        request = ln.PayReqString(pay_req=pay_req)
        return LndAL._stub.DecodePayReq(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def new_address(type):
        LndAL.get_rpc_data()
        request = ln.NewAddressRequest(type=type)
        return LndAL._stub.NewAddress(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def unlock_wallet(wallet_password, recovery_window=0):
        LndAL.get_rpc_unlock_data()
        request = ln.UnlockWalletRequest(wallet_password=wallet_password, recovery_window=recovery_window)
        return LndAL._stub.UnlockWallet(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def update_channel_policy(chan_point, base_fee_msat, fee_rate, time_lock_delta):
        LndAL.get_rpc_data()
        request = ln.PolicyUpdateRequest(chan_point=chan_point,
                                         base_fee_msat=base_fee_msat,
                                         fee_rate=fee_rate,
                                         time_lock_delta=time_lock_delta)
        return LndAL._stub.UpdateChannelPolicy(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def get_node_info(pub_key):
        LndAL.get_rpc_data()
        request = ln.NodeInfoRequest(pub_key=pub_key)
        return LndAL._stub.GetNodeInfo(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def get_chan_info(chan_id):
        LndAL.get_rpc_data()
        request = ln.ChanInfoRequest(chan_id=chan_id)
        return LndAL._macaroon.GetChanInfo(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def get_fee_report():
        LndAL.get_rpc_data()
        request = ln.FeeReportRequest()
        return LndAL._stub.FeeReport(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def pending_channels():
        LndAL.get_rpc_data()
        request = ln.PendingChannelsRequest()
        return LndAL._stub.PendingChannels(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def connect(addr, perm=False):
        LndAL.get_rpc_data()
        request = ln.ConnectPeerRequest(addr=addr)
        return LndAL._stub.ConnectPeer(request, metadata=[('macaroon', LndAL._macaroon)])

    @staticmethod
    def open_channel(node_pub_key,
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
        LndAL.get_rpc_data()
        request = ln.OpenChannelRequest(node_pubkey=node_pub_key,
                                        node_pubkey_string=node_pub_key_string,
                                        local_funding_amount=local_funding_amount,
                                        push_sat=push_sat,
                                        target_conf=target_conf,
                                        sat_per_byte=sat_per_byte,
                                        private=private,
                                        min_htlc_msat=min_htlc_msat,
                                        remote_csv_delay=remote_csv_delay)

        for r in LndAL._stub.OpenChannel(request, metadata=[('macaroon', LndAL._macaroon)]):
            # TODO: test the below
            response.append(r)
            if r:
                break
        return response

    @staticmethod
    def close_channel(channel_point, force=False, target_conf=0, sat_per_byte=0):
        response = []
        LndAL.get_rpc_data()
        request = ln.CloseChannelRequest(channel_point=channel_point,
                                         force=force,
                                         target_conf=target_conf,
                                         sat_per_byte=sat_per_byte)
        for r in LndAL._stub.CloseChannel(request, metadata=[('macaroon', LndAL._macaroon)]):
            # TODO: test the below
            response.append(r)
            if r:
                break
        return response

    @staticmethod
    def set_fee_limit(fixed=0, percent=0):
        val = {"fixed": fixed, "percent": percent}
        return val
