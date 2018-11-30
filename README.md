# Conductor2
### Lightning routing node dashboard

Project to manage lightning node. It is still in prototype phase. Almost no error handling.
Many bugs are still present. Programm will crash.

The program has not been systematically tested, but only by using it on Ubuntu.

I installed it on Windows 8.1, and it runs, but the UI needs tweaking to better fit. It appears that for some reason the windows are not resizable.

### Functionality
1. Shows graph of all the channels for your node
2. Shows a list of all the pending open or closing channels
3. Shows the information about a channel when clicking on the connected node in the channel graph.
  Channels can be closed, or when inactive you can try to reconnect to the node.
4. For each channel the channel policy can be set. Base fee, fee rate and time lock delay 
5. Shows node information when searching on Node name (case sensitive) or public key of the node. You can open a channel to this node if you wish to do so.

### Installation
In order for gRPC to work follow the following guidelines:
[How to write a Python gRPC client for the Lightning Network Daemon](https://dev.lightning.community/guides/python-grpc/)

Furthermore, install the packages from requirements.txt

I will be very happy with bug reports, feature requests and pull requests.

# Use at your own risk, if used on mainnet Bitcoin (money) can and will be lost.

