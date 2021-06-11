# Requires Version 2.1.0, nothing higher or breaks!
# (c) Webair 2019 - Angelo poggi
#Simple script that logs into a Mikrotik and creates a Mark down page so you can copy it to Confluence
from librouteros import connect
from creds import username, password
from json2html import *
import sys
firewall = input('enter firewall\n')
try:
    api = connect(username=username, password=password,
                  host=firewall, port=8728, login_plain=True)
except:
    print('Firewall seems to be offline, Make sure API service is enabled')
    input('Press any key to quit....')
    sys.exit()
list_interface = api(cmd='/interface/print')
nat_rules = api(cmd='/ip/firewall/nat/print')
address_list = api(cmd='/ip/firewall/address-list/print')
firewall_rules = api(cmd='/ip/firewall/filter/print', stats=False)
hostname = api(cmd='/system/identity/print')
system_id = api(cmd='/system/license/print')
ip_addr = api(cmd='/ip/address/print')
ipsec_peer = api(cmd='/ip/ipsec/peer/print')
ipsec_policy = api(cmd='/ip/ipsec/policy/print')
# payload for Peer
ipsec_peer_results = []
for item in ipsec_peer:
    ipsec_peer_results.append({
        'name': item.get('name', ''),
        'address': item.get('address', ''),
        'local-address': item.get('local-address', ''),
        'exchange-mode': item.get('exchange-mode', '')
    })
peer_payload = json2html.convert(json=ipsec_peer_results)
ipsec_policy_results = []
for item in ipsec_policy:
    ipsec_policy_results.append({
        'Peer': item.get('peer', ''),
        'src-address': item.get('src-address', ''),
        'dst-address': item.get('dst-address', ''),
        'sa-src-address': item.get('sa-src-address', ''),
        'sa-dst-address': item.get('sa-dst-address', '')
    })
policy_payload = json2html.convert(json=ipsec_policy_results)
# Payload for hostname
hostname_payload = json2html.convert(json=hostname)
system_id_results = []
for item in system_id:
    system_id_results.append({
        'system-id': item.get('system-id', 'N/A'),
        'software-id': item.get('software-id', 'N/A')
    })
# Payload for System ID's
systemid_payload = json2html.convert(json=system_id_results)
interface_results = []
for item in list_interface:
    interface_results.append({
        'name': item.get('name', 'N/A'),
        'mac-address': item.get('mac-address', 'N/A'),
        'default-name': item.get('default-name', 'N/A')
    })
# payload for Interfaces
interface_payload = json2html.convert(json=interface_results)
nat_results = []
for item in nat_rules:
    nat_results.append({
        'chain': item.get('chain', 'N/A'),
        'action': item.get('action', 'N/A'),
        'src-address': item.get('src-address', 'N/A'),
        'to-address': item.get('to-address', 'N/A'),
        'comment': item.get('comment', 'N/A')
    })
# Payload for NAT rules
nat_payload = json2html.convert(json=nat_results)
result = []
for item in firewall_rules:
    result.append({
        'chain': item.get("chain", "N/A"),
        'protocol': item.get("protocol", "N/A"),
        'src-address': item.get("src-address", "N/A"),
        'dst-address': item.get("dst-address", "N/A"),
        'comment': item.get("comment", "N/A"),
        'action': item.get("action", 'N/A')
    })
firewall_payload = json2html.convert(json=result)
address_list_results = []
for item in address_list:
    address_list_results.append({
        'list': item.get("list", ""),
        'address': item.get("address", "N/A")
    })
address_list_payload = json2html.convert(json=address_list_results)
payloads = [
    hostname_payload,
    systemid_payload,
    interface_payload,
    nat_payload,
    address_list_payload,
    peer_payload,
    policy_payload
]
print(f'Creating File {firewall}.html')
with open(f'{firewall}.html', 'w+') as doc_html:
    for payload in payloads:
        doc_html.write(payload)
        doc_html.write('\n')
print('File Created, please copy & paste into Confluence')
input('Press any key to quit...')
sys.exit()