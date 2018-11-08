from lightning import lightning_channel
from PyQt5 import QtCore, QtWidgets, QtGui


class ChannelInfoWidget(QtWidgets.QWidget):
    def __init__(self, channel_id=0):
        super().__init__()

        self.channel_name_label = QtWidgets.QLabel(self)
        self.channel_name_label.setGeometry(QtCore.QRect(200, 0, 700, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.channel_name_label.setFont(font)
        self.channel_name_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.channel_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.channel_name_label.setObjectName("channel_name_label")

        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 80, 610, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(50, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.active_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.active_label.setObjectName("active_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.active_label)

        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.channel_id_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.channel_id_label.setObjectName("channel_id_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel_id_label)

        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.capacity_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.capacity_label.setObjectName("capacity_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.capacity_label)

        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.local_balance_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.local_balance_label.setObjectName("local_balance_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.local_balance_label)

        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.remote_balance_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.remote_balance_label.setObjectName("remote_balance_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.remote_balance_label)

        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)

        self.commit_fee_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.commit_fee_label.setObjectName("commit_fee_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.commit_fee_label)

        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_16)

        self.commit_weight_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.commit_weight_label.setObjectName("commit_weight_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.commit_weight_label)

        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_17)

        self.fee_per_kw_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.fee_per_kw_label.setObjectName("fee_per_kw_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.fee_per_kw_label)

        self.formLayoutWidget_2 = QtWidgets.QWidget(self)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(610, 80, 621, 431))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(50, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)

        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)

        self.unsettled_balance_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.unsettled_balance_label.setObjectName("unsettled_balance_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.unsettled_balance_label)

        self.tot_sat_sent_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.tot_sat_sent_label.setObjectName("tot_sat_sent_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tot_sat_sent_label)

        self.tot_sat_received_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.tot_sat_received_label.setObjectName("tot_sat_received_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tot_sat_received_label)

        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_20)

        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_21)

        self.num_updates_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.num_updates_label.setObjectName("num_updates_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.num_updates_label)

        self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_29.setObjectName("label_29")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_29)

        self.pending_htlcs_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.pending_htlcs_label.setObjectName("pending_htlcs_label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pending_htlcs_label)

        self.label_31 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_31)

        self.csv_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.csv_label.setObjectName("csv_label")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.csv_label)

        self.label_33 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_33.setObjectName("label_33")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_33)

        self.private_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.private_label.setObjectName("private_label")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.private_label)

        self.formLayoutWidget_3 = QtWidgets.QWidget(self)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 471, 1251, 150))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(50, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.label_42 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_42.setObjectName("label_4")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_42)

        self.channel_point_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9.5)
        self.channel_point_label.setFont(font)
        self.channel_point_label.setObjectName("channel_point_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.channel_point_label)

        self.remote_pubkey_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9.5)
        self.remote_pubkey_label.setFont(font)
        self.remote_pubkey_label.setObjectName("remote_pubkey_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.remote_pubkey_label)

        self.uri_label = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9.5)
        self.uri_label.setFont(font)
        self.uri_label.setObjectName("remote_pubkey_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uri_label)

        self.channel_name_label.setText("TextLabel")
        self.label.setText("Active:")
        self.active_label.setText("TextLabel")
        self.label_2.setText("Remote pubkey:")
        self.remote_pubkey_label.setText("TextLabel")
        self.label_3.setText("Channel point:")
        self.channel_point_label.setText("TextLabel")
        self.label_4.setText("Channel id:")
        self.channel_id_label.setText("TextLabel")
        self.label_5.setText("Capacity:")
        self.capacity_label.setText("TextLabel")
        self.label_6.setText("Local balance:")
        self.local_balance_label.setText("TextLabel")
        self.label_7.setText("Remote balance:")
        self.remote_balance_label.setText("TextLabel")
        self.label_15.setText("Commit fee:")
        self.commit_fee_label.setText("TextLabel")
        self.label_16.setText("Commit weight:")
        self.commit_weight_label.setText("TextLabel")
        self.label_17.setText("Fee per kw:")
        self.fee_per_kw_label.setText("TextLabel")
        self.label_18.setText("Unsettled balance:")
        self.label_19.setText("Total satoshis sent:")
        self.unsettled_balance_label.setText("TextLabel")
        self.tot_sat_sent_label.setText("TextLabel")
        self.tot_sat_received_label.setText("TextLabel")
        self.label_20.setText("Total satoshis received:")
        self.label_21.setText("Number of updates:")
        self.num_updates_label.setText("TextLabel")
        self.label_29.setText("Pending htlcs")
        self.pending_htlcs_label.setText("TextLabel")
        self.label_31.setText("CSV delay")
        self.csv_label.setText("TextLabel")
        self.label_33.setText("Private")
        self.private_label.setText("TextLabel")
        self.label_42.setText("Uri:")
        self.uri_label.setText("TextLabel")

        if channel_id != 0:
            self.update_info(channel_id)
        # don't show the object yet, because it is forward created
        # in order for the channel list to access this object
        # to update info

    def update_info(self, channel_id):
        channel = lightning_channel.Channels.channel_index[channel_id][0]
        self.channel_name_label.setText(channel.remote_node_alias)
        self.active_label.setText(str(channel.channel_state))
        self.remote_pubkey_label.setText(channel.remote_pubkey)
        self.channel_point_label.setText(channel.channel_point.get("funding_txid_str")+':'+str(channel.channel_point.get("output_index")))
        self.channel_id_label.setText(str(channel.chan_id))
        self.capacity_label.setText(str(channel.capacity))
        self.local_balance_label.setText(str(channel.local_balance))
        self.remote_balance_label.setText(str(channel.remote_balance))
        self.commit_fee_label.setText(str(channel.commit_fee))
        self.commit_weight_label.setText(str(channel.commit_weight))
        self.fee_per_kw_label.setText(str(channel.fee_per_kw))
        self.unsettled_balance_label.setText(str(channel.unsettled_balance))
        self.tot_sat_sent_label.setText(str(channel.total_satoshis_sent))
        self.tot_sat_received_label.setText(str(channel.total_satoshis_received))
        self.num_updates_label.setText(str(channel.num_updates))
        # TODO: add pending htlcs link
        if not channel.pending_htlcs:
            self.pending_htlcs_label.setText("No pending HTLC")
        self.csv_label.setText(str(channel.csv_delay))
        self.private_label.setText(str(channel.private))
        self.uri_label.setText(channel.remote_uri)