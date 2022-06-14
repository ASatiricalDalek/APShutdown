import switch_connect
from getpass import getpass

pw = getpass()

ees_mdf = {
    "switch_ip" : "10.136.200.100",
    "pw" : pw
}

ees_idf1 = {
    "switch_ip" : "10.136.200.110",
    "pw" : pw
}

pes_mdf = {
    "switch_ip" : "10.136.200.200",
    "pw" : pw
}

kes_mdf = {
    "switch_ip" : "10.136.200.150",
    "pw" : pw
}

kes_idf1 = {
    "switch_ip" : "10.136.200.160",
    "pw" : pw
}

## Disable ##

# con = switch_connect.connect_to_switch(ees_mdf["switch_ip"], ees_mdf["pw"])
# ports = switch_connect.get_ports("WiFi_AP", con)
# print(ports)
# switch_connect.disable_ports(con,ports)

# con = switch_connect.connect_to_switch(ees_idf1["switch_ip"], ees_idf1["pw"])
# ports = switch_connect.get_ports("WiFi_AP", con)
# print(ports)
# switch_connect.disable_ports(con,ports)

# con = switch_connect.connect_to_switch(pes_mdf["switch_ip"], pes_mdf["pw"])
# ports = switch_connect.get_ports("WiFi_AP", con)
# print(ports)
# switch_connect.disable_ports(con,ports)

# con = switch_connect.connect_to_switch(pes_idf1["switch_ip"], pes_idf1["pw"])
# ports = switch_connect.get_ports("WiFi_AP", con)
# print(ports)
# switch_connect.disable_ports(con,ports)

# con = switch_connect.connect_to_switch(kes_mdf["switch_ip"], kes_mdf["pw"])
# ports = switch_connect.get_ports("WiFi_AP", con)
# print(ports)
# switch_connect.disable_ports(con,ports)

# con = switch_connect.connect_to_switch(kes_idf1["switch_ip"], kes_idf1["pw"])
# ports = switch_connect.get_ports("WiFi_AP", con)
# print(ports)
# switch_connect.disable_ports(con,ports)

# con = switch_connect.connect_to_switch(ees_mdf["switch_ip"], ees_mdf["pw"])
# ports = switch_connect.get_ports("WiFi_AP", con)
# print(ports)
# switch_connect.disable_ports(con,ports)

## Enable ##

con = switch_connect.connect_to_switch(ees_idf1["switch_ip"], ees_idf1["pw"])
ports = switch_connect.get_ports("WiFi_AP", con)
print(ports)
switch_connect.enable_ports(con,ports)

con = switch_connect.connect_to_switch(pes_mdf["switch_ip"], pes_mdf["pw"])
ports = switch_connect.get_ports("WiFi_AP", con)
print(ports)
switch_connect.enable_ports(con,ports)

con = switch_connect.connect_to_switch(pes_idf1["switch_ip"], pes_idf1["pw"])
ports = switch_connect.get_ports("WiFi_AP", con)
print(ports)
switch_connect.enable_ports(con,ports)

con = switch_connect.connect_to_switch(kes_mdf["switch_ip"], kes_mdf["pw"])
ports = switch_connect.get_ports("WiFi_AP", con)
print(ports)
switch_connect.enable_ports(con,ports)

con = switch_connect.connect_to_switch(kes_idf1["switch_ip"], kes_idf1["pw"])
ports = switch_connect.get_ports("WiFi_AP", con)
print(ports)
switch_connect.enable_ports(con,ports)