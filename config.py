# TODO:
#  Home Done
#  Search
#  SearchPage
#  SearchUser
#  UserPage
#  Message
#  Live
#  Live_UserTab
#  ----------------
#  Inbox
#  Setting_and_Privacy
#  Setting_Switch_Account
#  Setting_Tab


InteractiveComponents = {
    # Home page components
    'Home':[
        # Top Bar
            # For You
        {'Name':'For You',
         'Config':{
             'content-desc':'For You'
         }}
         ,
            # Search
        {'Name':'Search',
         'Config':{
             'resource-id':'com.zhiliaoapp.musically:id/cm3'
         }},
            # Live
        {'Name':'Live',
         'Config':{
             'NAF': 'true',
             'index': '0',
             'text': '',
             'resource-id': '',
             'class': 'android.widget.ImageView',
             'content-desc': ''
        }},
        # Bottom bar
            # Home
        {'Name':'Home',
         'Config':{
             'content-desc':'Home'
         }},
            # Discover
        {'Name':'Discover',
         'Config':{
             'content-desc':'Discover'
         }},
            # Inbox
        {'Name':'Inbox',
         'Config':{
             'resource-id': 'com.zhiliaoapp.musically:id/fie'
         }},
            # Profile
        {'Name':'Profile',
         'Config':{
             'resource-id': 'com.zhiliaoapp.musically:id/fif'
         }},
        # Main Page Components
            # User Page
        {'Name':'User Page',
         'Config':{
             'resource-id':'com.zhiliaoapp.musically:id/d08'
         }},
            # Follow
        {'Name':'Follow',
         'Config':{
             'resource-id':'com.zhiliaoapp.musically:id/l9n'
         }},
            # Like
        {'Name':'Like',
         'Config':{
             'resource-id':'com.zhiliaoapp.musically:id/buh'
         }},
            # Comment
        {'Name':'Comment',
         'Config':{
             'resource-id':'com.zhiliaoapp.musically:id/b9d'
         }},
            # Favourite
        {'Name':'Favourite',
         'Config':{
             'resource-id':'com.zhiliaoapp.musically:id/cmd'
         }},
            # Share
        {'Name':'Share',
         'Config':{
             'resource-id':'com.zhiliaoapp.musically:id/buh'
         }}
    ],

    # User Page Components
    'UserPage_entry':[
        # Follow
        {'Name':'Follow',
         'Config':{
             'resource-id':'com.zhiliaoapp.musically:id/h43'
         }}],
    'UserPage_postfollow':[
        # Message
        {'Name':'Message',
         'Config':{
             'resource-id':'com.zhiliaoapp.musically:id/igs'
         }}],

    # Live Page Components
    'Live':[
        # host Info Logo
        {'Name':'hostInfoLogo',
         'Config':{
            'resource-id': 'com.zhiliaoapp.musically:id/la8'
         }}
    ],

    # Live Page Usertab Components
    'Live_UserTab':[
        # Host User Page
        {'Name':'hostUserPage',
         'Config':{
        'resource-id': 'com.zhiliaoapp.musically:id/a3c'
         }}
    ],

    # Direct Message Page Components
    'Message_entry':[
        # Text box
        {'Name':'DMTextbox',
         'Config':{
             'resource-id': 'com.zhiliaoapp.musically:id/frt'
         }}],
    'Message_input':[
        # confirm send
        {'Name':'DMconfirmSend',
         'Config':{
        'resource-id': 'com.zhiliaoapp.musically:id/igh'
         }}
    ],

    # Search Page Components
    'Search':[
        # Search button
        {'Name':'SearchButton',
         'Config':{
             'text':'Search'
         }},
        # Search Box
        {'Name':'SearchBox',
         'Config':{
             'resource-id': 'com.zhiliaoapp.musically:id/ch2'
         }}
    ],

    # Search Page User Components
    'SearchPage':[
        # Users Tab
        {'Name':'UserTab',
         'Config':{
             'content-desc': 'Users'
         }}],
    'UserTab':[{'Name':'FirstUser',
         'Config':{
             'resource-id': 'com.zhiliaoapp.musically:id/l3c'
         }}
    ],

    # Inbox Components -> later
    'Inbox':[

    ],

    # Setting and Privacy Page Components -> later
    'Setting_and_Privacy':[

    ],

    # Setting Switch Account Page Components -> later
    'Setting_Switch_Account':[

    ],

    # Setting Tab Components -> later
    'Setting_Tab':[

    ]
}



TextComponents = {
    'UserPage':[
        {'Attr':'resource-id',
         'Name':'com.zhiliaoapp.musically:id/l_c',  # userid
         'text':''},
        {'Attr':'resource-id',
         'Name':'com.zhiliaoapp.musically:id/d12',  # followers
         'text':''},
        {'Attr':'resource-id',
         'Name':'com.zhiliaoapp.musically:id/btf',  # likes number
         'text':''}
    ]
}

