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

from datetime import datetime
from scheduler.update_scheduler import UpdateScheduler
from config.config import SystemConfiguration
from lightning import lightning_channel


class AutoPolicy(object):
    def __init__(self):
        sc = SystemConfiguration()
        self.policy1 = sc.policy1
        self.policy2 = sc.policy2
        self.policy3 = sc.policy3

        # register the auto policy update function, run it evey 2 hours if auto_policy flag is True in config
        st = sc.auto_policy
        UpdateScheduler.register('auto_policy',
                                 self.update,
                                 interval=2 * 60 * 60 * 1000,
                                 start=sc.auto_policy,
                                 immediate=sc.auto_policy)

    def update(self):
        print('auto_policy entry: ' + str(datetime.now()))
        sc = SystemConfiguration()
        for c in lightning_channel.Channels.channel_index:
            channel = lightning_channel.Channels.channel_index[c][0]
            if channel.channel_type == "open_channel":
                if channel.remote_balance == 0:
                    balance_ratio = 100000.0
                else:
                    balance_ratio = channel.local_balance / channel.remote_balance
                if balance_ratio >= float(self.policy1['perc']):
                    lightning_channel.Channels.update_channel_policy(
                        channel.channel_point,
                        base_fee_msat=int(self.policy1['base_fee']),
                        fee_rate=float(self.policy1['fee_rate']),
                        time_lock_delta=int(sc.default_time_lock_delta))
                elif balance_ratio >= float(self.policy2['perc']):
                    lightning_channel.Channels.update_channel_policy(
                        channel.channel_point,
                        base_fee_msat=int(self.policy2['base_fee']),
                        fee_rate=float(self.policy2['fee_rate']),
                        time_lock_delta=int(sc.default_time_lock_delta))
                else:
                    lightning_channel.Channels.update_channel_policy(
                        channel.channel_point,
                        base_fee_msat=int(self.policy3['base_fee']),
                        fee_rate=float(self.policy3['fee_rate']),
                        time_lock_delta=int(sc.default_time_lock_delta))
        UpdateScheduler.trigger('channel_info_widget')
        print('auto_policy exit: ' + str(datetime.now()))
