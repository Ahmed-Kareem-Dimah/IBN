from netmiko import ConnectHandler
import re

# ips_file = open("list_ip", 'r')  ## open a file from root if it all backbone or mobilebackhoul
# ips_file.seek(0)  ## put the first read on the begining
# iplist = ips_file.read().splitlines()  ## splite the ip's in a list
# ips_file.close()

def Write_file(data, name):
    filz = open("/auto/IBN/nodes_config/"+name, 'w')
    filz.write(data)
    filz.close()

def getbackup():
    ipz = ['10.255.255.1', '10.255.255.3', '10.255.255.4', '10.255.255.5', '10.255.255.6', '10.255.255.7',
           '10.255.255.8', '10.253.253.21', '10.253.253.22', '10.254.254.11', '10.254.254.12', '10.254.254.13',
           '10.254.254.14', '10.254.254.15', '10.254.254.16']
    print(ipz)
    new_ip = input("Is this new IP ?: ")
    if new_ip not in ipz:  # to confirm if the new IP has been entered or not or already exist
        a = new_ip.split('.')
        if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (
                int(a[0]) != 169 or int(a[1]) != 254) and (
                0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
            ipz.append(new_ip)
            print(ipz)
        else:
            print("The New ip {} is in wrong format".format(new_ip))

    else:
        print("this IP {} already in the list !".format(new_ip))
        pass

    for ip in ipz:
        a = ip.split('.')
        if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (
                int(a[0]) != 169 or int(a[1]) != 254) and (
                0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
            print('\n')
            #print("IP's formula is good :%s" % ip)

            cumulus = {
                'device_type': 'linux',
                'ip': ip,
                'username': 'root',
                'password': 'root',
            }
            nokia = {
                'device_type': 'alcatel_sros',
                'ip': ip,
                'username': 'admin',
                'password': 'admin',
            }
            cisco = {
                'device_type': 'cisco_ios',
                'ip': ip,
                'username': 'dema',
                'password': 'dema',
            }
            nokia_IPs = ['10.255.255.1', '10.255.255.2', '10.255.255.3', '10.255.255.4', '10.255.255.5', '10.255.255.6',
                         '10.255.255.7', '10.255.255.8']  # the list of  Nokia nodes in the network
            cumulus_IPs = ['10.253.253.21', '10.253.253.22', '10.253.253.23', '10.253.253.24', '10.253.253.25',
                           '10.253.253.26', '10.253.253.27', '10.253.253.28', '10.253.253.29', '10.253.253.30',
                           '10.253.253.31', '10.253.253.32', '10.253.253.33', '10.253.253.34', '10.253.253.35',
                           '10.253.253.36']  # the list of cumulus nodes in the network
            cisco_IPs = ['10.254.254.11', '10.254.254.12', '10.254.254.13', '10.254.254.14', '10.254.254.15',
                         '10.254.254.16']  # the list of Cisco nodes in the network
            try:
                if ip in nokia_IPs:
                    connect = ConnectHandler(**nokia)
                    # get device name
                    deviceinfo = connect.send_command('show chassis | match Name post-lines 13')
                    devicename = re.search(r"(Name) +(:) (.+)", deviceinfo, re.I).group(3)
                    print(devicename)

                    # get the backupFile name
                    # filename = connect.send_command('show bof | match primary-config')
                    # backup = re.search(r"(primary-config) +(.+)", filename, re.I).group(2)

                    # get the backupFile name
                    config = connect.send_command('admin display')

                    # send backup config to FTP with ip and device name
                    # connect.send_command(
                    #     ('file copy ') + (backup) + (' tftp://10.10.99.3/') + (ipz) + ('_') + (devicename) + ' force')
                    # print("Nokia Backup sent !!")
                    Write_file(config, devicename)
                    connect.disconnect()

                elif ip in cumulus_IPs:
                    connect = ConnectHandler(**cumulus)
                    # get device name
                    deviceinfo = connect.send_command('net sho hostname')
                    #
                    # # get the backupFile name
                    config = connect.send_command('net sho configuration commands')
                    Write_file(config, deviceinfo)
                    connect.disconnect()

                elif ip in cisco_IPs:
                    connect = ConnectHandler(**cisco)
                    # get device name
                    data = connect.send_command('sho running-config | include hostname')
                    devicename = re.search(r"(hostname) +(.+)", data, re.I).group(2)
                    print(devicename)

                    # send backup config to FTP with ip and device name
                    # connect.send_command(
                    #     ('copy system:running-config tftp://10.10.99.3/') + (ipz) + ('_') + (devicename))
                    # print("Cisco backup sent!")

                    config = connect.send_command('sho running-config')
                    Write_file(config, devicename)
                    connect.disconnect()
                else:
                    print("the {} is not within your network".format(ip))
            except Exception as e:
                print(e)

        else:
            print("This is wrong IP: %s" % ip)
            break
    #ipz = input("Enter node IP: ")


if __name__ == "__main__":
    getbackup()
