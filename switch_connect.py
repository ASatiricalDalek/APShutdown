from netmiko import ConnectHandler

def connect_to_switch(switch_ip, switch_pw):
    next_switch = {
        'device_type': 'cisco_ios',
        'host': switch_ip,
        'username': 'OSLAN\\amcnamarac',
        'password': switch_pw
    }
    net_connect = ConnectHandler(**next_switch)
    return net_connect


def get_ports(desc, connection):
    # List of all the eventual ports to be returned
    ports = []
    # Command run on the switch to get all the interfaces needed
    output = connection.send_command('show interface description | incl ' + desc)
    # There will be multiple Gs in the return string so keep track of where the last one was
    last_index = 0
    # Keep track of the current index to accurately update the last index when we find a G
    current_index = 0
    for letter in output:
        # If the letter is G and the next letter is an i this is most likely an interface
        if letter == 'G' and output[(output.index(letter,last_index) + 1)] == "i":
            # Mark this index as a "G" so we don't keep writing the same interface to the list (index function returns the first found instance of the string)
            last_index = current_index
            interface = output[current_index]
            increment = 1
            loop_control = True
            # Loop through the string starting at the G until hitting the empty space. Write the full interface to a variable and finally to the list
            while loop_control:
                next_letter = current_index + increment 
                if output[next_letter] == " ":
                    ports.append(interface)
                    loop_control = False
                    break
                else:
                    interface += output[next_letter]
                    increment += 1
        current_index += 1
    return ports

def disable_ports(connection, ports):
    for port in ports:
        connection.send_config_set(['interface ' +port, 'shutdown'])
        connection.disconnect()

    
        