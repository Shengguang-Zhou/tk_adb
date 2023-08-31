import time
from datetime import datetime
import pandas as pd
from adb_sending_msg import *
from Comment_Generator import *
import streamlit as st


def sleep_time(type):
    if type == 'short':
        sleepy_time = random.uniform(0.1,1.0)
    if type == 'medium':
        sleepy_time = random.uniform(1.0,2.0)
    if type == 'long':
        sleepy_time = random.uniform(2.0,3.0)
    if type == 'extra':
        sleepy_time = random.uniform(3,5)
    if type == 'extreme':
        sleepy_time = random.uniform(7,10)
    return time.sleep(sleepy_time)


# send message with known userid
def send_private_msg(users:list,name):
    placeholder = st.empty()
    info = pd.DataFrame(columns=['发送时间', '用户', '发送消息'])
    send_msg_TikTok_action = TikTok_action()

    # only need for the first
    send_msg_TikTok_action.click_home()     # reset to home page just in case
    sleep_time('medium')
    send_msg_TikTok_action.click_search()
    sleep_time('medium')
    for user in users:
        # 输入
        send_msg_TikTok_action.send_string(string=str(user))
        sleep_time('medium') # short
        # 确认搜索
        send_msg_TikTok_action.adb_send()
        time.sleep(0.5)
        send_msg_TikTok_action.adb_send()
        sleep_time('extra')
        # 前往user栏
        send_msg_TikTok_action.click_usertab()
        sleep_time('extreme')
        # 点击第一个用户
        send_msg_TikTok_action.click_usertab_firstuser()
        sleep_time('long')
        # follow
        send_msg_TikTok_action.follow_userpage()
        sleep_time('extra')
        # 进入对话页面
        send_msg_TikTok_action.click_message()
        sleep_time('extra')
        # 点击对话框
        send_msg_TikTok_action.click_message_textbox()
        sleep_time('medium')
        # 输入信息
        message_generated = random_text(name) # input used
        send_msg_TikTok_action.send_string(message_generated)
        sleep_time('extra')
        # 确认发送
        send_msg_TikTok_action.click_message_send()
        sent_time = datetime.today()
        sleep_time('medium')
        # 退出到user info page
        send_msg_TikTok_action.back()   # 第一次会退出对话框
        sleep_time('medium')
        send_msg_TikTok_action.back()
        sleep_time('medium')
        # 回到搜索页
        send_msg_TikTok_action.back()
        sleep_time('medium')
        # 清空搜索页
        send_msg_TikTok_action.click_search_box()   # 第一次会进入对话框
        sleep_time('extra')
        for i in range(len(user)):
            send_msg_TikTok_action.delete()
        sleep_time('medium')
        # Writing to datatable
        new_row = {'发送时间': sent_time, '用户': user, '发送消息': message_generated}
        info = info.append(new_row, ignore_index=True)
        placeholder.table(info)
    placeholder.empty()
    return info

def send_comment_known_id(users:list):
    info = pd.DataFrame(columns=['发送时间', '用户', '发送消息'])
    send_msg_TikTok_action = TikTok_action()
    placeholder = st.empty()

    # only need for the first
    send_msg_TikTok_action.click_home()     # reset to home page just in case
    sleep_time('extra')
    send_msg_TikTok_action.click_search()
    sleep_time('short')
    for user in users:
        # 输入
        send_msg_TikTok_action.send_string(string=str(user))
        sleep_time('extra') # short
        # 确认搜索
        send_msg_TikTok_action.adb_send()
        time.sleep(1)
        send_msg_TikTok_action.adb_send()
        sleep_time('extra')
        # 前往user栏
        send_msg_TikTok_action.click_usertab()
        sleep_time('extra')
        # 点击第一个用户
        send_msg_TikTok_action.click_usertab_firstuser()
        sleep_time('extreme')
        # 点击第一个视频
        send_msg_TikTok_action.click_userpage_firstvideo()
        sleep_time('extra')
        # 点击评论
        send_msg_TikTok_action.click_comment_tab()
        sleep_time('medium')
        # 输入信息
        comment_to_send = comment_generator()
        send_msg_TikTok_action.send_string(string=comment_to_send)
        sleep_time('extra')
        # 点击发送
        send_msg_TikTok_action.click_comment_send()
        sent_time = datetime.today()
        sleep_time('extra')
        # 退出评论区
        send_msg_TikTok_action.back()   # 第一次back退出评论区
        sleep_time('extra')
        # 点击返回 - 用户页
        send_msg_TikTok_action.back()
        sleep_time('extra')
        # 点击返回 - 搜索页
        send_msg_TikTok_action.back()
        sleep_time('extra')
        # 点击搜索栏
        sleep_time('extra')
        # 清空搜索
        for i in range(len(user)):
            send_msg_TikTok_action.delete()
            time.sleep(1)
        sleep_time('extra')
        # 记录数据
        new_row = {'发送时间': sent_time, '用户': user, '发送消息': comment_to_send}
        info = info.append(new_row, ignore_index=True)
        placeholder.table(info)
    placeholder.empty()
    return info


