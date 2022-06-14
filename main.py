import switch_connect
from getpass import getpass

pw = getpass()

ees_mdf = {
    "switch_ip" : "10.136.200.100",
    "pw" : pw
}

con = switch_connect.connect_to_switch(ees_mdf["switch_ip"], ees_mdf["pw"])
ports = switch_connect.get_ports("WiFi_AP", con)
print(ports)
# switch_connect.disable_ports(con,ports)