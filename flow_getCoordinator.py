from class_getCoordinates import *


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