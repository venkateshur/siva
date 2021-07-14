from paramiko import SSHClient
from scp import SCPClient

def unix_transfer(path, host, port, user_name, password, input_file, output_file):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(user_name + ":" + password + "@" + host + ":" + port + ":" + path)

    with SCPClient(ssh.get_transport()) as scp:
        scp.put(input_file, output_file)


