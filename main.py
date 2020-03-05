from netmiko import ConnectHandler
import re

# ips_file = open("list_ip", 'r')  ## open a file from root if it all backbone or mobilebackhoul
# ips_file.seek(0)  ## put the first read on the begining
# iplist = ips_file.read().splitlines()  ## splite the ip's in a list
# ips_file.close()

def Write_file(data, name):
    filz = open("/auto/DIMAH_Conn_Multi_Vendor/nodes_config/"+name, 'w')
    filz.write(data)
    filz.close()

def getbackup():
    ipz = input("Enter node IP: ")
    cumulus = {
        'device_type': 'linux',
        'ip': ipz,
        'username': 'root',
        'password': 'root',
    }
    nokia = {
        'device_type': 'alcatel_sros',
        'ip': ipz,
        'username': 'admin',
        'password': 'admin',
    }
    cisco = {
        'device_type': 'cisco_ios',
        'ip': ipz,
        'username': 'dema',
        'password': 'dema',
    }
    nokia_IPs = ['10.255.255.1', '10.255.255.2', '10.255.255.3', '10.255.255.4', '10.255.255.5', '10.255.255.6', '10.255.255.7', '10.255.255.8']  # the list of  Nokia nodes in the network
    cumulus_IPs = ['10.233.233.1', '10.233.233.2', '10.233.233.3', '10.233.233.4', '10.233.233.5', '10.244.244.244.1',
                   '10.244.244.2', '10.244.244.3', '10.244.244.4',
                   '10.244.244.5']  # the list of cumulus nodes in the network
    cisco_IPs = ['10.254.254.11', '10.254.254.12', '10.254.254.13', '10.254.254.14', '10.254.254.15', '10.254.254.16']
    try:
        if ipz in nokia_IPs:
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

        elif ipz in cumulus_IPs:
            connect = ConnectHandler(**cumulus)
            # get device name
            # deviceinfo = connect.send_command('show chassis | match Name post-lines 13')
            # devicename = re.search(r"(.+Name) +(:) (.+)", deviceinfo, re.I).group(3)
            # output_dict[devicename] = devicename
            # out_q.put(output_dict)
            #
            # # get the backupFile name
            # filename = connect.send_command('show bof | match primary-config')
            # backup = re.search(r"(.+primary-config) +(.+)", filename, re.I).group(2)
            #
            # # send backup config to FTP with ip and device name
            # connect.send_command(('file copy ') + (backup) + (' ftp://ALU:lucent@10.22.33.2/dema/') + (ipz) + ('_') + (devicename))
            connect.disconnect()

        elif ipz in cisco_IPs:
            connect = ConnectHandler(**cisco)
            # get device name
            data = connect.send_command('sho running-config | include hostname')
            devicename = re.search(r"(hostname) +(.+)", data, re.I).group(2)
            print(devicename)

            # # get the backupFile name
            # filename = connect.send_command('show bof | match primary-config')
            # backup = re.search(r"(.+primary-config) +(.+)", filename, re.I).group(2)

            # send backup config to FTP with ip and device name
            # connect.send_command(
            #     ('copy system:running-config tftp://10.10.99.3/') + (ipz) + ('_') + (devicename))
            # print("Cisco backup sent!")

            config = connect.send_command('sho running-config')
            Write_file(config, devicename)
            connect.disconnect()
        else:
            print("the {} is not within your network".format(ipz))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    getbackup()
