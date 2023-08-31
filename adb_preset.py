import socket
import subprocess

adb_directory = '/Users/shengguang/PycharmProjects/TikTok/Sending_msg_bot/adb'

class adb_preset:

    def __init__(self):
        self.adb_directory = adb_directory
    # 获取本地IP
    def local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.254.254.254', 1))            # doesn't even have to be reachable
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    # 配对手机与终端
    def adb_pair(self,adb_directory = adb_directory,port=5555):
        # Inputs
        address = input('Input developer IP address and port as xxx.xxx.xxx:host:')
        # pair
        subprocess.run(['./adb', 'pair', address], cwd=adb_directory)    # if its true, you need to enter the pair code
        print('-----------------------------------------------------------------')
        print('Connected to developer mode','\nStarting to pair')
        print('-----------------------------------------------------------------')
        # Connection
        subprocess.run(['./adb', 'connect', address], cwd=adb_directory)
        # Check
        result = subprocess.run(['./adb', 'devices'], cwd=adb_directory, capture_output=True, text=True)
        # 检查是否成功连接
        if result.stdout:
            print('-----------------------------------------------------------------')
            print(result.stdout,'连接成功')
            return True
        else:
            print('设备连接失败，请检查输入或联系管理员')
            return False

    # 查询adb设备
    def adb_device(self,adb_directory = adb_directory):
        if adb_directory is not None:
            devices_check = subprocess.run(['./adb', 'devices'], cwd=adb_directory, capture_output=True, text=True)
            print('device check:',devices_check.stdout)
            lines = devices_check.stdout.splitlines()
            devices = []
            for line in lines[1:]:
                if '\tdevice' in line:
                    devices.append(line.split('\t')[0])
            return devices
        else:
            raise ValueError('请输入adb文件夹地址')
        return devices_check.stdout

adb = adb_preset()
# adb.adb_pair()
print(adb.adb_device())