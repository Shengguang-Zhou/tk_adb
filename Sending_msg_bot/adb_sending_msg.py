import time
from coordinator import *
from adb_preset import *
import numpy as np
import random


# TODO:
#  实现对安卓多端Wi-Fi连接 done -> Android 11+
#  滑动屏幕x、y轴根据逻辑随机
#  抖音用户头像圆圈内随机
#  -------------------------------------
#  实现私信主播并随机调取"打招呼.py"文件的文本生成
#  文本流式输入，间隔时间为随机0.05s到0.2s, uniform distribution
#  修改坐标
#  主播ID私信输入从streamlit前端文件接收



# TODO:
#  Fill opentiktok
#  Fill type_comment
def open_tiktok():
    pass

class TikTok_action:
    coordinator = coordinator()
    def __init__(self):
        pass
    def streaming_print(self,string):
        for i in range(len(string)):
            self.send_string(string[i])
            time.sleep(0.03)

    # 输入文字
    def send_string(self,string):
        string = string.replace('\\', '\\\\')  # Escape backslashes first
        string = string.replace('"', '\\"')    # Escape double quotes
        string = string.replace('!', '\\!')    # Escape exclamation marks
        string = string.replace("'", "\\'")    # Escape single quotes
        string = string.replace(" ", "%s")
        string = string.replace('\n', '%sKEYCODE_ENTER%s')

        cmd = ['./adb', 'shell', 'input', 'text', string]
        subprocess.run(cmd,cwd=adb_directory)
        return string

    def delete(self):
        cmd = ['./adb', 'shell', 'input', 'keyevent', '67']  # 67 is the keycode for KEYCODE_DEL
        subprocess.run(cmd, cwd=adb_directory)

    # 上滑
    def swipe_up(self,x1=random.uniform(coordinator['swipe_up']['lower_x1'],coordinator['swipe_up']['higher_x1']),
                 y1=random.uniform(coordinator['swipe_up']['lower_y1'],coordinator['swipe_up']['higher_y1']),
                 trajectory=random.uniform(coordinator['swipe_up']['lower_trajectory'],coordinator['swipe_up']['higher_trajectory']),
                 theta_x = random.uniform(coordinator['swipe_up']['lower_theta'],coordinator['swipe_up']['higher_theta']),
                 theta_y = random.uniform(coordinator['swipe_up']['lower_theta'],coordinator['swipe_up']['higher_theta']),
                 duration=int(random.uniform(coordinator['swipe_up']['lower_duration'],coordinator['swipe_up']['higher_duration']))):
        final_position = np.array([[x1],[y1]]) +trajectory* np.array([[np.cos(np.deg2rad(theta_x))],     # (x) = x + h * cos theta
                                                                    [np.sin(np.deg2rad(theta_y))]])      # (y) = y + h * sin theta
        x2,y2 = int(final_position[0][0]),int(final_position[1][0])
        cmd = ['./adb','shell', 'input', 'swipe', str(x1), str(y1), str(x2), str(y2),str(duration)]
        subprocess.run(cmd,cwd=adb_directory)

    def swipe_down(self,x1=random.uniform(coordinator['swipe_down']['lower_x1'],coordinator['swipe_down']['higher_x1']),
                   y1=random.uniform(coordinator['swipe_down']['lower_y1'],coordinator['swipe_down']['higher_y1']),
                   trajectory=random.uniform(coordinator['swipe_down']['lower_trajectory'],coordinator['swipe_down']['higher_trajectory']),
                   theta_x = random.uniform(coordinator['swipe_down']['lower_theta'],coordinator['swipe_down']['higher_theta']),
                   theta_y = random.uniform(coordinator['swipe_down']['lower_theta'],coordinator['swipe_down']['higher_theta']),
                   duration=int(random.uniform(coordinator['swipe_down']['lower_duration'],coordinator['swipe_down']['higher_duration']))):
        final_position = np.array([[x1],[y1]]) +trajectory* np.array([[np.cos(np.deg2rad(theta_x))],     # (x) = x + h * cos theta
                                                                      [np.sin(np.deg2rad(theta_y))]])      # (y) = y + h * sin theta
        x2,y2 = int(final_position[0][0]),int(final_position[1][0])
        cmd = ['./adb','shell', 'input', 'swipe', str(x1), str(y1), str(x2), str(y2),str(duration)]
        subprocess.run(cmd,cwd=adb_directory)

    def like(self,x1=random.uniform(coordinator['like']['min_x'],coordinator['like']['max_x']),
                    y1 = random.uniform(coordinator['like']['min_y'],coordinator['like']['max_y']),
                    x_displacement = random.uniform(0,coordinator['like']['x_displacement']),
                    y_displacement = random.uniform(0,coordinator['like']['y_displacement'])):
        x2,y2 = x1+x_displacement, y1+y_displacement
        cmd_1 = ['./adb','shell', 'input', 'tap', str(x1), str(y1)]
        cmd_2 = ['./adb','shell', 'input', 'tap', str(x2), str(y2)]
        subprocess.run(cmd_1,cwd=adb_directory)
        subprocess.run(cmd_2,cwd=adb_directory)

    def comment(self,x=coordinator['comment']['x'],
                y=coordinator['comment']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_comment_tab(self,x= coordinator['click_comment_tab']['x'],
                          y = coordinator['click_comment_tab']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_comment_send(self,x=coordinator['click_comment_send']['x'],
                           y=coordinator['click_comment_send']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def favourite(self,x=random.uniform(coordinator['favourite']['min_x'],coordinator['favourite']['max_x']),
                  y=random.uniform(coordinator['favourite']['min_y'],coordinator['favourite']['max_y'])):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_share(self,x=random.uniform(coordinator['click_share']['min_x'],coordinator['click_share']['max_x']),
                    y=random.uniform(coordinator['click_share']['min_y'],coordinator['click_share']['max_y'])):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def download(self,x=random.uniform(coordinator['download']['min_x'],coordinator['download']['max_x']),
                 y=random.uniform(coordinator['download']['min_y'],coordinator['download']['max_y']),
                 sleepy=random.uniform(0,2)):
        self.click_share()
        time.sleep(sleepy)
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_home(self,x=random.uniform(coordinator['click_home']['min_x'],coordinator['click_home']['max_x']),
                   y=random.uniform(coordinator['click_home']['min_y'],coordinator['click_home']['max_y'])):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_info(self,x=random.uniform(coordinator['click_info']['min_x'],coordinator['click_info']['max_x']),
                   y=random.uniform(coordinator['click_info']['min_y'],coordinator['click_info']['max_y'])):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def follow(self,x=random.uniform(coordinator['follow']['min_x'],coordinator['follow']['max_x']),
               y=random.uniform(coordinator['follow']['min_y'],coordinator['follow']['max_y'])):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def follow_userpage(self,x=coordinator['follow_userpage']['x'],
                        y=coordinator['follow_userpage']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_search(self,x=random.uniform(coordinator['click_search']['min_x'],coordinator['click_search']['max_x']),
               y=random.uniform(coordinator['click_search']['min_y'],coordinator['click_search']['max_y'])):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_confirm_search(self,x=random.uniform(coordinator['click_confirm_search']['min_x'],coordinator['click_confirm_search']['max_x']),
                             y=random.uniform(coordinator['click_confirm_search']['min_y'],coordinator['click_confirm_search']['max_y'])):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_search_box(self,x=coordinator['click_search_box']['x'],
                             y=coordinator['click_search_box']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def search_clear(self,x=coordinator['search_clear']['x'],
                     y=coordinator['search_clear']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_search_user(self,x=coordinator['click_search_user']['x'],
                          y=coordinator['click_search_user']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_usertab(self,x=coordinator['click_usertab']['x'],
                      y=coordinator['click_usertab']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_usertab_firstuser(self,x=coordinator['click_usertab_firstuser']['x'],
                                y=coordinator['click_usertab_firstuser']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_userpage_firstvideo(selfself,x=coordinator['click_userpage_firstvideo']['x'],
                                   y=coordinator['click_userpage_firstvideo']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_message(self,x=coordinator['click_message']['x'],
                     y=coordinator['click_message']['y']):
      cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
      subprocess.run(cmd,cwd=adb_directory)

    def click_message_textbox(self,x1=coordinator['click_message_textbox']['x1'],y1=coordinator['click_message_textbox']['y1']):
        cmd = ['./adb','shell', 'input', 'tap', str(x1), str(y1)]
        subprocess.run(cmd,cwd=adb_directory)

    def click_message_send(self,x=random.uniform(coordinator['click_message_send']['min_x'],coordinator['click_message_send']['max_x']),
                             y=random.uniform(coordinator['click_message_send']['min_y'],coordinator['click_message_send']['max_y'])):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def unfollow(self,x=random.uniform(coordinator['unfollow']['min_x'],coordinator['unfollow']['max_x']),
                 y=random.uniform(coordinator['unfollow']['min_y'],coordinator['unfollow']['max_y'])):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    def back(self):
        # 模拟按下返回键
        cmd = ['./adb', 'shell', 'input', 'keyevent', '4']
        subprocess.run(cmd, cwd=adb_directory)

    def adb_send(self):
        cmd = ['./adb', 'shell', 'input', 'keyevent', '66'] # 66 is send
        subprocess.run(cmd, cwd=adb_directory)





from Comment_Generator import *


send_msg_TikTok_action = TikTok_action()
# for i in range(10):
#     send_msg_TikTok_action.delete()


send_msg_TikTok_action.adb_send()





