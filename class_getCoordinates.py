import time
import xml.etree.ElementTree as ET
import re
import os

# TODO: Text extract:
#  userid, nickname, followerNumber, Likes, Bio

class getCoordinates:
    target_path = '/Users/shengguang/PycharmProjects/TikTok/Sending_msg_bot/xml_tmp'
    xml_path = '/Users/shengguang/PycharmProjects/TikTok/Sending_msg_bot/xml_tmp/window_dump.xml'

    def __init__(self):
        pass

    # Save current screen to XML file, not called directly
    def save_ui(self,target_path):
        # adb shell uiautomator dump --compressed
        # cmd = ['./adb','shell', 'uiautomator', 'dump', '--compressed']
        cmd = ['./adb','shell', 'uiautomator', 'dump']
        subprocess.run(cmd, cwd=adb_directory)
        xml_path = target_path+'/window_dump.xml'
        # adb pull /sdcard/window_dump.xml /path/to/your/directory/
        cmd = ['./adb','pull','/sdcard/window_dump.xml',target_path]
        subprocess.run(cmd, cwd=adb_directory)
        return xml_path

    # Get text element coordinate
    def root_page(self, xml_path=None):
        if xml_path is None:
            xml_path = self.save_ui(target_path='/Users/shengguang/PycharmProjects/TikTok/Sending_msg_bot/xml_tmp/')
        # 解析XML -> fix later for variable
        tree = ET.parse(xml_path)
        root = tree.getroot()
        # for node_element in root.findall('.//node'):
        #     print(node_element.attrib)
        return root

    def position(self,root,component):
        # 待查找的元素
        result_element = None
        # 遍历查找node元素
        for node_element in root.findall('.//node'):
            if all(node_element.attrib.get(key) == value for key,value in component.items()):  # when we pass items, pass config list by a for loop
                result_element = node_element
                break
        # 如果找不到元素，直接返回空
        if result_element is None:
            print('抱歉！找不到元素！')
            return None
        # 解析数据
        coord = re.compile(r"\d+").findall(result_element.attrib['bounds'])
        # 中心点坐标
        position_center = int((int(coord[0]) + int(coord[2])) / 2), int((int(coord[1]) + int(coord[3])) / 2)
        return position_center

    # delete file, call after you get position
    def delete_file(self,xml_path):
    # Delete the XML file
        try:
            os.remove(xml_path)
            print(f"File {xml_path} deleted successfully!")
        except OSError as e:
            print(f"Error deleting file {xml_path}. Reason: {e.strerror}")

    def find_coordinates(self,df,page): # Pass the page you want to find here, which is the config file key, df is config
        co = {}
        xml = self.root_page()
        for component in df[page]:
            xy = self.position(root = xml, component = component['Config'])
            co[component['Name']] = {'x':xy[0],
                                     'y':xy[1]}
        self.delete_file(self.xml_path)
        return co


    def save_coordinates(self,df_name,coordinates,deviceName, ):
        device_fileName = f'/Users/shengguang/PycharmProjects/TikTok/Sending_msg_bot/device_info/{deviceName}.py'
        with open(device_fileName,'a') as file:
            output = '{} = {}'.format(df_name,coordinates)
            file.write(output+'\n')




######################################################################################################################################################
######################################################################################################################################################



from config import InteractiveComponents
from adb_sending_msg import *
def deviceCoordinate(components):
    # init (todo -> get device name -> replace all deviceName)
    coord = getCoordinates()
    action = TikTok_action()

    # get home coordinates
    co_home = coord.find_coordinates(df = components,page ='Home')
    coord.save_coordinates(df_name='Home',coordinates= co_home,deviceName='test')
    time.sleep(2)

    # click live
    action.adb_tap(x = co_home['Live']['x'],y = co_home['Live']['y'])
    time.sleep(2)

    # get live coordinates
    co_live = coord.find_coordinates(df = components,page ='Live')
    coord.save_coordinates(df_name='Live',coordinates= co_live,deviceName='test')
    time.sleep(2)

    # click live_hostlogo
    action.adb_tap(x = co_live['hostInfoLogo']['x'],y = co_live['hostInfoLogo']['y'])
    time.sleep(2)

    # get live_usertab coordinates
    co_liveUserTab = coord.find_coordinates(df = components,page ='Live_UserTab')
    coord.save_coordinates(df_name='Live_UserTab',coordinates= co_liveUserTab,deviceName='test')
    time.sleep(2)

    # back*2
    action.back()
    time.sleep(2)
    action.back()
    time.sleep(2)

    # click Search
    action.adb_tap(x = co_home['Search']['x'],y = co_home['Search']['y'])
    time.sleep(2)

    # get search coordinates
    co_Search = coord.find_coordinates(df = components,page ='Search')
    coord.save_coordinates(df_name='Search',coordinates= co_Search,deviceName='test')
    time.sleep(2)

    # input something
    action.send_string('theRock')
    time.sleep(1)
    # click search
    action.adb_tap(x = co_Search['SearchButton']['x'],y = co_Search['SearchButton']['y'])
    time.sleep(2)

    # get search_user coordinate for usertab
    co_SearchPage = coord.find_coordinates(df = components,page ='SearchPage')
    coord.save_coordinates(df_name='SearchPage',coordinates= co_SearchPage,deviceName='test')
    time.sleep(2)

    # click usertab
    action.adb_tap(x = co_SearchPage['UserTab']['x'],y=co_SearchPage['UserTab']['y'])
    time.sleep(2)

    # get firstuser coordinate for usertab
    co_UserTab = coord.find_coordinates(df = components,page ='UserTab')
    coord.save_coordinates(df_name='UserTab',coordinates= co_UserTab,deviceName='test')

    # click firstuser
    action.adb_tap(x = co_UserTab['FirstUser']['x'],y=co_UserTab['FirstUser']['y'])
    time.sleep(2)

    # get userpage coordinates
    co_UserPage_entry = coord.find_coordinates(df = components,page ='UserPage_entry')
    coord.save_coordinates(df_name='UserPage_entry',coordinates= co_UserPage_entry,deviceName='test')

    # click follow
    action.adb_tap(x = co_UserPage_entry['Follow']['x'],y=co_UserPage_entry['Follow']['y'])
    time.sleep(2)

    # get message coordinates
    co_UserPage_postfollow = coord.find_coordinates(df = components,page ='UserPage_postfollow')
    coord.save_coordinates(df_name='UserPage_postfollow',coordinates= co_UserPage_postfollow,deviceName='test')

    # click message
    action.adb_tap(x = co_UserPage_postfollow['Message']['x'],y=co_UserPage_postfollow['Message']['y'])
    time.sleep(2)

    # get message textbox coordinates
    co_Message_entry = coord.find_coordinates(df = components,page ='Message_entry')
    coord.save_coordinates(df_name='Message_entry',coordinates= co_Message_entry,deviceName='test')

    # click textbox
    action.adb_tap(x = co_Message_entry['DMTextbox']['x'],y=co_Message_entry['DMTextbox']['y'])
    time.sleep(2)

    # get message send coordinate
    co_Message_input = coord.find_coordinates(df = components,page ='Message_input')
    coord.save_coordinates(df_name='Message_input',coordinates= co_Message_input,deviceName='test')

    # back to homepage (6 times)
    for i in range(6):
        action.back()
        time.sleep(1)
    print('Finish collecting coordinates info')


deviceCoordinate(components=InteractiveComponents)