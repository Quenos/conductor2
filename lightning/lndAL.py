import codecs
import grpc
import os
from lightning import rpc_pb2_grpc as lnrpc, rpc_pb2 as ln


class LndAL:

    def __init__(self):
        pass

    @classmethod
    def get_rpc_data(cls):
        cls.macaroon = codecs.encode(open('/home/coen/data/admin.macaroon', 'rb').read(), 'hex')
        os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
        cert = open('/home/coen/data/tls.cert', 'rb').read()
        ssl_creds = grpc.ssl_channel_credentials(cert)
        channel = grpc.secure_channel('192.168.0.110:10009', ssl_creds)
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

    @staticmethod
    def set_fee_limit(fixed=0, percent=0):
        val = {"fixed": fixed, "percent": percent}
        return val


#print(LndAL.list_channels(inactive_only=True))
#print(LndAL.unlock_wallet(str.encode('MarocPepperCaravanConcreteReason')))
#print(LndAL.forwarding_history(end_time=1541060251))
#3CctbZXkxQ1oxp8v9KWNGBmJNZxArwKwbA
#print(LndAL.query_routes('0232e20e7b68b9b673fb25f48322b151a93186bffe4550045040673797ceca43cf',amt=510000, fee_limit=LndAL.set_fee_limit(5,1)))
#print(LndAL.closed_channels())
