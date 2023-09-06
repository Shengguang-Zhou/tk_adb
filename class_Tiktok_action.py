import time
from coordinator import *
from adb_preset import *
import numpy as np
import random
from device_info.test import *


def open_tiktok():
    pass

class TikTok_action:
    coordinator = coordinator()
    def __init__(self):
        pass


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

    # 删除文字
    def delete(self):
        cmd = ['./adb', 'shell', 'input', 'keyevent', '67']  # 67 is the keycode for KEYCODE_DEL
        subprocess.run(cmd, cwd=adb_directory)

    # 上滑
    # todo -> get screen coordinate then fix this
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

    # 下滑
    # todo -> get screen coordinate then fix this
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

    # 点赞
    def like(self,x = Home['Like']['x'],y = Home['Like']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 评论
    def comment(self,x = Home['Comment']['x'],y = Home['Comment']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # todo -> need coordinate
    # 点击评论框
    def click_comment_tab(self,x= coordinator['click_comment_tab']['x'],
                          y = coordinator['click_comment_tab']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # todo -> need coordinate
    # 点击发送评论
    def click_comment_send(self,x=coordinator['click_comment_send']['x'],
                           y=coordinator['click_comment_send']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 收藏
    def favourite(self,x = Home['Favourite']['x'],y = Home['Favourite']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 点击分享
    def click_share(self,x = Home['Share']['x'],y = Home['Share']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # todo -> 采集坐标
    def download(self,x=random.uniform(coordinator['download']['min_x'],coordinator['download']['max_x']),
                 y=random.uniform(coordinator['download']['min_y'],coordinator['download']['max_y']),
                 sleepy=random.uniform(0,2)):
        self.click_share()
        time.sleep(sleepy)
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 点击home
    def click_home(self,x = Home['Home']['x'],y = Home['Home']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 查看主页
    def click_info(self, x = Home['User Page']['x'],y = Home['User Page']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 关注
    def follow(self,x = Home['Follow']['x'],y = Home['Follow']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 用户页关注
    def follow_userpage(self,x = UserPage_entry['Follow']['x'],y = UserPage_entry['Follow']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 点击搜索
    def click_search(self,x = Home['Search']['x'],y = Home['Search']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 点击确认搜索
    def click_confirm_search(self,x = Search['SearchButton']['x'],y = Search['SearchButton']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 点击搜索框
    def click_search_box(self,x = Search['SearchBox']['x'],y = Search['SearchBox']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # todo: 采集坐标
    # 清搜搜索
    def search_clear(self,x=coordinator['search_clear']['x'],
                     y=coordinator['search_clear']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # todo: 这是啥
    def click_search_user(self,x=coordinator['click_search_user']['x'],
                          y=coordinator['click_search_user']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 搜索页usertab
    def click_usertab(self,x = SearchPage['UserTab']['x'],y = SearchPage['UserTab']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 点击第一个usertab里的第一个用户
    def click_usertab_firstuser(self,x = UserTab['FirstUser']['x'],y = UserTab['FirstUser']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # todo -> 采集坐标
    def click_userpage_firstvideo(selfself,x=coordinator['click_userpage_firstvideo']['x'],
                                  y=coordinator['click_userpage_firstvideo']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # TODO： GETSTART坐标
    def click_getstart(self,x=coordinator['click_getstart']['x'],
                       y=coordinator['click_getstart']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    # 用户页点击发送消息
    def click_message(self,x=UserPage_postfollow['Message']['x'],y=UserPage_postfollow['Message']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)

    #点击消息输入框
    def click_message_textbox(self,x=Message_entry['DMTextbox']['x'],y=Message_entry['DMTextbox']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)
    #点击消息发送
    def click_message_send(self,x=Message_input['DMconfirmSend']['x'],y=Message_input['DMconfirmSend']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)
    # TODO -> 采集坐标 + 改变收集坐标流程
    def unfollow(self,x=random.uniform(coordinator['unfollow']['min_x'],coordinator['unfollow']['max_x']),
                 y=random.uniform(coordinator['unfollow']['min_y'],coordinator['unfollow']['max_y'])):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)
    # 回退
    def back(self):
        # 模拟按下返回键
        cmd = ['./adb', 'shell', 'input', 'keyevent', '4']
        subprocess.run(cmd, cwd=adb_directory)
    # 发送
    def adb_send(self):
        cmd = ['./adb', 'shell', 'input', 'keyevent', '66'] # 66 is send
        subprocess.run(cmd, cwd=adb_directory)
    # TODO：根据屏幕大小改变坐标
    def like_live(self):
        x = random.uniform(130,870)
        y = random.uniform(710,1200)
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd, cwd=adb_directory)
    # 进入Live
    def click_live(self,x = Home['Live']['x'],y = Home['Live']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd, cwd=adb_directory)
    # live点击主播logo
    def click_host_live(self,x=Live['hostInfoLogo']['x'],y = Live['hostInfoLogo']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd, cwd=adb_directory)
    # 点击主播logo跳出后的tab
    def click_host_live_tab(self,x=Live_UserTab['hostUserPage']['x'],y = Live_UserTab['hostUserPage']['y']):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd, cwd=adb_directory)

    def adb_tap(self,x,y):
        cmd = ['./adb','shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(cmd,cwd=adb_directory)




