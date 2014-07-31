#Mar/19/2014 -- David
#added verify_link(logfile, link) function 
# added close browser to fail case browser and comment write log to W:\\; added close browser to install extention function
# changed Google Login to login from link.

#04/14/2014 -- David added close tab function to pass and fail functions
#04/15/2014 -- Kathy: added load browser for Fail and Pass function, to avoid when browser is not open and the image won't be displayed.
#04/29/2014 -- David: changed images for get protection value; change image in close tab function
#05/09/2014 -- Kathy: changed verfy_link function,for some link which are substring of the verify string, will be passed.
                #changed load_browser_with_url,if _PF_link is not correct, load it again.
                #change take screenshot for log before loading failed link
#05/22/2014 -- Kathty: 
                #1.moved _last_modify right after import section for convenience version checking, added space between functions 
                #2.added locate_facebook_section(logfile) in facebookLogin function after detecting facebook already logged in
                #3.cleaned up Facebook login function
#05/23/2014 -- Michael:
                #fixed InstallExtension
                #changed locate FB section and Facebook LogIn
                #changed Twitter login
                #changed locate LinkedIn and Linkedin login 
                #removed extra dot in images
                #changed images names
#05/28/2014-- Michael:
                #Changed locate google section and google log in
                #Changed Twitter locate section
                #Fixed LinkedIn log in
#05/28/2014 -- Kathy:
                # _reset_url = "https://www.stage.privacyfix.com/start/reset" won't work
                #use: _reset_url = "https://stage.privacyfix.com/start/reset" inst

#6/20/2014 -- Kathy: 
                #change last modify using time function to get current date
                #change write_img_log to use relative path
#6/25/2014 -- Kathy:                
                #changed google login image to "settings"
                #added screenshot for Google loging function
#6/26/2014 -- Kathy:    
                #modify facebook login: add locate facebook section
                #change facebook locate logic, use "facebook track you on" as end search
                #change linkedIn login function, fix reset missing images
                
from __future__ import with_statement
import ConfigParser
import logging
import shutil
from sikuli import *
import os, re
from datetime import datetime
import time
from random import randint

#_last_modifed=str(time.strftime("%Y-%m-%d"))
_last_modifed = "2014-06-25 11:13PM by Kathy"
#this PF_common is for firefox
_scriptName = "PF_common_FF.sikuli"


############## Below is Ron's code, please don't touch #################

_saveLogToRW = False
_useAutoUser = False


_log_root = "W:\\Logs\\"

if len(sys.argv) > 1 and sys.argv[1] == "logrw":
    _useAutoUser = True
    _saveLogToRW = True

print "_saveLogToRW: ", _saveLogToRW

if len(sys.argv) > 1 and sys.argv[1] == "autoUser":
    _useAutoUser = True

print "_useAutoUser: ", _useAutoUser
############## Above is Ron's code, please don't touch #################


#_email="eletina1919@gmail.com"
_email="lyemele@gmail.com"
_password="qawsed1234"



############## Below is Ron's code, please don't touch #################

if _useAutoUser:
    # when a Driver launches the TC's always use mzhang account.  
    _email = "mzhang0170@gmail.com"
    _password = "zhang0170"

############## Above Ron's code, please don't touch #################

_passed_link = "dl.dropboxusercontent.com/u/40284694/passed.png"
_failed_link ="dl.dropboxusercontent.com/u/40284694/failed.png"

#_install_link = "stage.privacyfix.com/start/install"
_install_link = "privacyfix.com/start/install"
#_PF_link="stage.privacyfix.com/start/"
_PF_link="privacyfix.com/start"

_reset_url = _PF_link + "/reset"

_firefox_appx86 = "C:\\Program Files (x86)\\Mozilla Firefox\Firefox.exe"
_firefox_app = "C:\\Program Files\\Mozilla Firefox\Firefox.exe"


if os.path.isfile(_firefox_appx86):
    #check for x86 path (x64 bit) 
    _firefox_app =_firefox_appx86
    
ff_icon =( "fficon.png")

_PF_logo="avgLogo.png"
_PF_logo1=("PFTab.png")
_PF_Target=("target.png")
_Top_left_reg = Region(2,103,446,401)
_Top_right_reg =Region(905,44,518,207)

Page_not_ready="pageNotReady.png"
LinkedInloginbutton = "lkLoginButton.png"
linkedin_section_img = "lkLogedIn.png"
LinkedIn_top_icon = Pattern("1403774588454.png").similar(0.90)

#linkedIn_profile=(Pattern("1401281272285.png").similar(0.96))
#LinkedIn_Image=(Pattern("LinkedLogedIn.png").similar(0.90))
#LinkedIn_LogIn=(Pattern("linkedLogIn.png").similar(0.90))
PF_icon = (Pattern("iconGrey.png").similar(0.80))
PF_icon_orange=Pattern("iconOrange.png").similar(0.91)

_rootDir = os.path.dirname(sys.argv[0].replace("/", "\\"))
# can't get dynamicially since this will return the calling script (the Tescase Script)
#_scriptName = os.path.basename(os.path.splitext(sys.argv[0])[0]) + ".sikuli"

print "_scriptName: ", _scriptName

if ".sikuli" in os.path.basename(_rootDir):
    # Running in command line returns the path including the sikuli script, different from IDE
    _rootDir = os.path.dirname(_rootDir)
_rootDir = _rootDir + "\\"
#_rootDir = "W:\\scripts\\web_app\\chrome\\"
#_scriptName = 
_thisScript = _rootDir + _scriptName

_commonDashDir = _thisScript + "\\config_dash\\"
_dirMap = {"dir":_commonDashDir}
_config_file= _commonDashDir + "config.txt" 

_config=ConfigParser.ConfigParser(_dirMap)
_config.read(_config_file)

#_test_suite_log="W:\\Privacy-fix\\test_suite_log.html"
_test_suite_log="C:\\test_suite_log.html"


#############Firefox specific functions###############################
def load_browser_with_url(link,logfile):
    a=App("Firefox")
    reg1=Region(1000,0,440,200)

    reg1.highlight(1)
    if not reg1.exists(ff_icon): 
        App.open(_firefox_app)
        #wait_find(ff_icon)
        sleep(3)        
    switchApp("Firefox")
    a.focus()
    sleep(3)  
    reg1.find(ff_icon).highlight(1)
    if not reg1.exists(ff_icon): 
        raise Exception("Firefox is not open!")
        
    if reg1.exists("1390908075391.png"):reg1.click("1390908075391.png")  
    sleep(1)
    type("l", KeyModifier.CTRL)
    wait (2)
    type(link)
    sleep(2)
    type(Key.ENTER)
    sleep(2)
    write_log(logfile,"Browser loaded" )
   # if link==_PF_link and not exists("1399577787529.png"):#added 5/9/2014
   #     #write_log_with_screenshot(logfile,"PF_link page is not loaded, try again!")       
   #     type("l", Key.CTRL)
   #     wait (2)
   #     type(link)
   #     sleep(2)
   #     type(Key.ENTER)
 #       sleep(2)        
  #  mouseMove(Location(1000,120))
#
#############Firefox specific functions###############################
def get_img_value(logfile,image):
    sleep(2)
    type(Key.F12)
    sleep(3)
    if exists("1399365445269.png"):
        wait_click("1399365462169.png")
    wait_click("1399365479164.png")
    wait_click("1388481681375-1.png")
    sleep(3)
       
    if exists(image):
        write_log_with_screenshot(logfile, "protection level image found!")
        click(image)
        sleep(2)
        type(Key.RIGHT)       
        sleep(2)
        write_log_with_screenshot(logfile, "Screen after click on right key")
        type(Key.DOWN)        
        sleep(1)
        type(Key.ENTER)
        sleep(1)
        type("c", KEY_CTRL)
        print "CTRL_C pressed!"
        sleep(2)        
        #App.open("%windir%\system32\notepad.exe")
        type("v", Key.CTRL)
        sleep(1)
        data=Env.getClipboard()
        print "txt: " + str(data)      
        value1=int(data.replace('%',''))        
        type(Key.F12)        
        print value1        
        return value1
    else:
        msg="Not able to get protection value!"   
        write_log_with_screenshot(logfile, msg)      
        raise Exception(msg)

#############Firefox specific functions###############################
def get_protection_value(logfile):
    
    search_txt1=("1399365553117.png")
                
       
    switchApp("Firefox")
    sleep(2)                
    #search_str2="num_private_settings\n"s
    #search_str1="fb_protection_percent\n"
    print "search img: " +str(search_txt1)
    percent_value = get_img_value(logfile,search_txt1)
    #list2 = get_img_value(search_txt2,search_str2)
    #print percent_value
    write_log(logfile,"Protection value is:" + str(percent_value))
    screen_shot=capture(0,0,1350,850)
    write_screenshot_log(logfile,screen_shot)    
    return percent_value

#############Firefox specific functions###############################
def ClearBrowsingData(logfile):
    a=App("Firefox")
    if not exists(ff_icon): 
        App.open(_firefox_app)
        wait_find(ff_icon)
        mouseMove(Location(1000,120))
    switchApp("Firefox")
    a.focus()
    sleep(2)
    type("s", Key.ALT)
    sleep(1)                
    click("1391300359244.png")
    sleep(1)                
    type("e")
    sleep(2)
    type(Key.ENTER)
    write_log(logfile,"\n<p>Browsing Data was cleared/p>\n")

#############Firefox specific functions###############################
def RemoveExt(logfile):
    load_browser_with_url("about:blank",logfile)
    PF_icon = (Pattern("1389954724256.png").similar(0.80))
                
    write_log_with_screenshot(logfile, "FF is opened!")
    
    if not exists(PF_icon):
        write_log_with_screenshot(logfile, "PF is not installed or removed!")
        return
    Extensions = ("extensions.png")
    Delete = ("deleteData.png")
    Remove = ("removeHistory.png")
    sleep(3)
    if exists(PF_icon):
        type("a", KeyModifier.CTRL + KeyModifier.SHIFT )
        sleep(5)
        click(Pattern(Extensions).similar(0.90))
        
       
        sleep(2)
        doubleClick(Delete)
        click(Remove)
        
        write_log(logfile,"\n<p>Extension was remowed</p>\n")
        type("w", Key.CTRL)  #--- close tab because ctrl_l on this page is different.
    else:
        write_log(logfile, "PF already removed!")
        return
    write_log(logfile, "<p>extension removed successfully</p>\n")

#############Firefox specific functions###############################
def InstallExtension(logfile):
    Get_AVG_PF = ("1389956575753.png")
    Allow = ("1389956735269.png")
    install= ("1389956873839.png")
    Arrow= ("1389957193540.png")
    Skip= ("1389957226628.png")
    PF_icon = (Pattern("1400840767646.png").similar(0.90))
    PF_icon_green =(Pattern("1400242292843.png").similar(0.78))
    reg2=Region(0,5,467,303)
    pfTab=("1400745489468.png")
    
    if reg2.exists(pfTab):        
        click (pfTab)
        print "PF is already installed!"
        write_log_with_screenshot(logfile, "PF is already installed!")
        return
    
    if not exists(ff_icon or PF_icon_green): App.open(_firefox_app)                
    verify(logfile,ff_icon)
    sleep(4)     
    load_browser_with_url("about:blank",logfile)   
    sleep(3)            
    if exists(Pattern(PF_icon).similar(0.90) or PF_icon_green):
        find(PF_icon).highlight(1)
        print "PF is already installed!"
        write_log_with_screenshot(logfile, "PF is already installed!")
        return
    load_browser_with_url(_install_link,logfile)
    verify(logfile,Get_AVG_PF)
    click(Get_AVG_PF)
    wait(2)
    click(Allow)

    verify(logfile,install)
    click(install)
    wait(5)
    i=0
    while (i < 3):
        if exists(Arrow):click(Arrow)
        wait(2)
        i+=1  
        print "i is:" + str(i)
    #if exists(Arrow):find().highlight(1);click(Skip) 
    ClearBrowsingData(logfile)              #avoid install link autofill for _PF_link
    sleep(2)
    type("w", KeyModifier.CTRL + KeyModifier.SHIFT )   
    sleep(2)            
    load_browser_with_url(_PF_link,logfile)
    write_log(logfile, "<p>extension installed successfully</p>\n")

################Common functions for all browsers##################################
def locate_linkedIn_section(logfile):
    LinkedInloginbutton = "lkLoginButton.png"
    linkedin_section_img="lkLogedIn.png"
    if _Top_right_reg.exists(LinkedIn_top_icon): 
        locate_item_page_by_page(logfile, linkedin_section_img)
        locate_item_line_by_line(logfile,"1403774743991.png")
        write_log_with_screenshot(logfile, "Facebook logged in, and facebook section located!")
    else:
        locate_item_page_by_page(logfile, LinkedInloginbutton)
        write_log_with_screenshot(logfile, "Facebook is not logged in, and facebook section located!")
    
def locate_linkedIn_section01(logfile):
    linkedInBoard=(Pattern("linkedBoard.png").similar(0.90))
    
    mouseMove(Location(1000,120))    
    i=0
    while not exists(linkedInBoard) and not exists(LinkedIn_LogIn)and i<8 :
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        mouseMove(Location(1000,110))        
        i+=1
        
    write_log(logfile, "locating linkedIn section") 
    if (not exists (LinkedIn_LogIn)):
        
        return 0

    else: 
        return 1


    mouseMove(Location(1000,120))
     
#find google section image, and use down key to find Tracking section image
#This is to make sure the whole google section is completely showing on screen
#find google section image, and use down key to find Tracking section image
#This is to make sure the whole google section is completely showing on screen
def locate_google_section(logfile):
 #   load_browser_with_url(_PF_link)
    GoogleLogo=("1401268453465.png")
    googlBoard=(Pattern("1401268735790.png").similar(0.91))
    notLoggedIn=("1401268681923.png")
    i=0
    mouseMove(Location(1000,120))
    sleep(2)

    #load_browser_with_url(_PF_link,logfile)
    type(Key.HOME)
    sleep(1)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    
    #while (not exists(googlBoard)  and i<6):
    #    type(Key.DOWN)
    #    mouseMove(Location(1000,110))        
    #    i+=1
    #    sleep(3)
    write_log(logfile, "locating google section") 
    if (not exists (notLoggedIn)):
        #type(Key.HOME)
        return 1

    else: 
      
        return 0


    
def locate_tracking_section(logfile):    #locate both tracking and websites section together
                

    tracking_section_img="personalData.png"
                 
    if not exists(tracking_section_img):
        type(Key.HOME)
        if not exists(_PF_logo):
            load_browser_with_url(_PF_link,logfile)
            wait_find(_PF_logo)
            waitVanish(Page_not_ready)
            sleep(2)
                
    mouseMove(Location(1000,200))
    
def locate_facebook_section(logfile):
    fb_logged_in=("FBLimage-1.png")
    #fb_board=("shareprivacyfix.png")
    fb_tracks_you_on = ("1403767947919.png")
    
    fb_logInbutton=(Pattern("fbLoginButton.png").similar(0.90))    
    if _Top_right_reg.exists("1403768600238.png"): 
        locate_item_page_by_page(logfile, fb_logged_in)
        locate_item_line_by_line(logfile,fb_tracks_you_on)
        write_log_with_screenshot(logfile, "Facebook logged in, and facebook section located!")
    else:
        locate_item_page_by_page(logfile, fb_logInbutton)
        write_log_with_screenshot(logfile, "Facebook is not logged in, and facebook section located!")

def locate_twitter_section(logfile):
    twitterLogin=(Pattern("twitterLogIn.png").similar(0.90))
    twitterLogo=(Pattern("twitterLogedIn.png").similar(0.91))
    i=0
    while (not exists(twitterLogin) and  not exists( twitterLogo) and i<2):
        type(Key.PAGE_DOWN)
        mouseMove(Location(1000,110))        
        i+=1
        sleep(3)
    write_log(logfile, "locating twitter section") 
    if (not exists (twitterLogin)):
        type(Key.HOME)
        return 0

    else: 
      
        return 1


#Login to google account
def GoogleLogin(logfile):
    start_time=datetime.now()
    write_log(logfile, "detecting browser...")
    if not exists(_PF_logo):
        load_browser_with_url(_PF_link,logfile)
        sleep(2)
           
        wait_find(_PF_logo)
        write_log_with_screenshot(logfile, _PF_link + "link entered!")                
        waitVanish(Page_not_ready)
        sleep(5)      
                
    write_log(logfile, "total time detecting browser is: " + str(datetime.now()-start_time)) 

    
    locate_google_section(logfile)
    google_login=("1401272615407.png")
   
    if exists(google_login):
        #load_browser_with_url("https://accounts.google.com")
        #click(google_login)
        google_account_link="https://accounts.google.com/Login?continue=https://history.google.com/history/settings%3Fhl%3Den&hl=en"
        load_browser_with_url(google_account_link,logfile)
        wait_find("singIn.png")
        sleep(2)
        if exists("emailgl.png"):
            type(_email)
            sleep(1)
            type(Key.TAB)
        type(_password)
        write_log_with_screenshot(logfile, "after enter password")
        sleep(1)
        type(Key.ENTER)
        sleep(2)
        verify(logfile,"1403436914889.png")
        write_log(logfile, "logged into Google successfully\n")
        write_log(logfile, "Total time for Google login is: " + str(datetime.now()-start_time))  
        load_browser_with_url(_PF_link,logfile)
        wait_find(_PF_logo)
        sleep(5)
        locate_google_section(logfile)
        write_log_with_screenshot(logfile,"logged into Google successfully\n")
        mouseMove(Location(1000,120))
           
    else: 
        write_log_with_screenshot(logfile, "Already logged into Google!\n")
        print "Already logged into Google!\n"        
        write_log(logfile, "Total time for Google login is: " + str(datetime.now()-start_time)) 
        mouseMove(Location(1000,110))
        
#Logging to Facebook
def FacebookLogin(logfile):
    
    start_time=datetime.now()

    Fb_logedIn=(Pattern("fbicon.png").similar(0.90))
    _Top_right_reg.highlight(1)
    type(Key.HOME)
    if not _Top_right_reg.exists(_PF_logo):
        write_log(logfile, "total time detecting PF logo not exist time is: " + str(datetime.now()-start_time))  
        load_browser_with_url(_PF_link,logfile)
        sleep(2)             
        write_log(logfile, "total time loading browser is: " + str(datetime.now()-start_time))        
        sleep(1)            
        if (wait_find(_PF_logo1)==0): wait_find(_PF_logo1)
        if not _Top_right_reg.exists(_PF_Target):wait_find(_PF_Target)
        write_log_with_screenshot(logfile, _PF_link + " link entered!")                
        _Top_left_reg.waitVanish(Page_not_ready)
        sleep(2)                
                
    write_log(logfile, "total time detecting browser is: " + str(datetime.now()-start_time))  
                          
    write_log_with_screenshot(logfile,"Loaded PF page")                                
    logged = _config.get('Facebook_Login', "logged")
    loginbutton = _config.get('Facebook_Login', "loginbutton")
    fb_logged_in_icon=_config.get('Facebook_Login', "fb_logged_in_icon")
    #locate_facefook_section(logfile)
    #if in Facebook section, and login button is not there, then it's logged in.
    #y=verify_continue(logfile,fb_logged_in_icon)
    #print "in PF_common_FF, y is:" +str(y)
    type(Key.HOME)
    if _Top_right_reg.exists (Fb_logedIn):
        find(Fb_logedIn).highlight(1)

        write_log_with_screenshot(logfile, "Facebook is already logged in!")  
        write_log(logfile, "total time detect logged in is: " + str(datetime.now()-start_time))
        locate_facebook_section(logfile)
        return
    #locate_facefook_section(logfile)
    #write_log(logfile, "total time detect logged in FB icon is: " + str(datetime.now()-start_time))                                
    #if login button shown in facebook section, then login to facebook section
    #fb_logo = _config.get('Facebook_Login', "FB_logo")
 #   cert_warning = _config.get('Facebook_Login', "cert_warning")
    #proceed = _config.get('Facebook_Login', "proceed")
    

    locate_item_page_by_page(logfile,loginbutton)
    click(Pattern(loginbutton).similar(0.90).targetOffset(224,0))
    
    sleep(2)
    reg_FBtab=Region(0,0,1440,200)                
    wait_find_reg(reg_FBtab,"facebook_tab_logo.png")
    ok_reg=Region(548,449,469,350)               
    okey_button=("ok1.png")
    ok_button=("ok2.png")
                    
    if exists(okey_button):
        click(okey_button)
        sleep(3)        
        if exists(okey_button):
            click(okey_button)
            sleep(3)         
        verify(logfile,fb_logged_in_icon)  
    write_log(logfile, "total time detect ok button is: " + str(datetime.now()-start_time)) 

    verify(logfile,"fbPageLogo.png")
    login_reg=Region(377,170,454,399)
    login_reg.highlight(1)                
    #print "loggin region is: " +login_reg.X()+" "+login_reg.Y() 
    username1=Pattern("1390307763657.png").similar(0.87)
    username2=Pattern("1389809891723.png").similar(0.90)
    username3=(Pattern("1390183106564.png").similar(0.90))
          
    if login_reg.exists(username1) or login_reg.exists(username2) or login_reg.exists(username3):
        sleep(1)
        type(_email)
        sleep(1)
        write_log_with_screenshot(logfile,"email entered")
        type(Key.TAB)
        sleep(1)
    write_log(logfile, "total time detect FB login username is: " + str(datetime.now()-start_time))                 
    type(_password)
    write_log_with_screenshot(logfile,"password entered")    
    sleep(1)
    type(Key.ENTER)
    sleep(5)
    write_log_with_screenshot(logfile,"after login to facebook")
 
    if ok_reg.exists(okey_button):
        click(okey_button)
        sleep(3)        
        if exists(okey_button):
            click(okey_button)
        sleep(3)         
        verify(logfile,logged)                          

    write_log_with_screenshot(logfile, "Logged into Facebook successfully!")
 
    locate_facebook_section(logfile)        
    write_log(logfile, "Total Facebook login time is: " + str(datetime.now()-start_time))  
                
def LinkedInLogIn(logfile):

    start_time=datetime.now()   
 
    #LinkedInloginbutton = "lkLoginButton.png"
    #linkedin_section_img="lkLogedIn.png"
    #linkedIn_profile=(Pattern("1401281272285.png").similar(0.96))
    #LinkedLogeedIn=("1401281749494.png")
                
    if  not _Top_left_reg.exists(_PF_logo):
        
        load_browser_with_url(_PF_link,logfile)
        sleep(2)        
        wait_find(_PF_logo)
        write_log_with_screenshot(logfile, _PF_link + "link entered!")
        waitVanish(Page_not_ready)
        sleep(2) 
                
        write_log(logfile, "total time detecting browser is: " + str(datetime.now()-start_time))  
        wait(5)

    if  _Top_right_reg.exists(LinkedIn_top_icon):
        find(LinkedIn_top_icon).highlight(1)
        write_log_with_screenshot(logfile, "Find LinkedIn_top_icon, already logged in LinkedIn!")  
        mouseMove(Location(1000,120))
        locate_linkedIn_section(logfile)
        return
    #look for LinkedIn section image to locate LinkedIn section
    locate_linkedIn_section(logfile)
    verify(logfile, LinkedInloginbutton) 
    click (Pattern(LinkedInloginbutton).similar(0.70).targetOffset(223,0))
    wait(2)
    if exists (Pattern("rassentered.png").similar(0.91)):
        type(Key.TAB)
        type(Key.TAB)
        type(Key.TAB)
        type(Key.ENTER)
        write_log(logfile, "password was saved in cookies")
        wait(1)
        type("w", Key.CTRL)
        return
    verify(logfile, "passwordlk.png")

    if exists("1391454308746.png"):
                    
        type(Key.TAB)
        sleep(2)                
        type(_email)
        write_log_with_screenshot(logfile,"email entered")
        
    sleep(1)
    type(Key.TAB)
    sleep(1)
    type(_password)
    sleep(1)     
    write_log_with_screenshot(logfile,"password entered")                
    type(Key.ENTER)
    sleep(1)
    type("w", Key.CTRL)
    sleep(3)

    #verify(logfile,LinkedLogeedIn)
    verify(logfile,linkedin_section_img)
    write_log(logfile, "logged into LinkedIn successfully")
    write_log(logfile, "Total LinkedIn login time is: " + str(datetime.now()-start_time))  
    #close the logged in tab, suppose to close by itself. it's a bug right now, if fixed in the future, please delete this line
    sleep(5)
    locate_linkedIn_section(logfile) 
                
    write_log_with_screenshot(logfile, "screenshot after logged into linkedin!")
    write_log(logfile, "Total LinkedIn login time is: " + str(datetime.now()-start_time))


def TwitterLogIn(logfile):
    twitterLogin=(Pattern("twitterLogIn.png").similar(0.90))
    twitterLogo=(Pattern("twitterLogedIn.png").similar(0.91))
    
    if not exists(_PF_logo or twitterLogo):
        load_browser_with_url(_PF_link,logfile)
        sleep(2)      
        wait_find(_PF_logo)
        write_log_with_screenshot(logfile, _PF_link + "link entered!")
        waitVanish(Page_not_ready)
        sleep(2) 
    if locate_twitter_section(logfile)==1:
        click(twitterLogin.targetOffset(120,0))
        wait(3)
        if exists ("1400834986301.png"):
            click("1400835009686.png")
            wait(2)
            type("w", Key.CTRL)
            type("r", Key.CTRL)
            wait(5)
            return
            
        type("michael.scott.avg@gmail.com")
        type(Key.TAB)
        wait(1)
        type("US!pf.avg")
        type(Key.TAB)
        type(Key.ENTER)
        wait(2)
        type("w", Key.CTRL)
        type("r", Key.CTRL)
        wait(5)
        write_log(logfile, "You logged into Twitter ")
    else:
        
        write_log(logfile, "You already logged into Twitter")
        
        
def write_log(logfile,msg):
    with open(logfile, 'a+') as fo:
        fo.write("\n<p> " + str(datetime.now())+ ":   " + msg+  " </p>\n")

    
def write_log_with_screenshot(logfile,msg):
    write_log(logfile,msg)
    scr_shot=capture(0,0,1400,900)
    write_screenshot_log(logfile,scr_shot)

def write_img_log(logfile,img):
    print "img in write_img_log is: " + img
    path_common=_rootDir + _scriptName + "\\"
    print "path_common is: " + path_common

    dst_path, script_name =os.path.split(logfile)
    print "dst_path is: " + dst_path
    
    script_path, script_name=os.path.split(dst_path)
    path_script=_rootDir + script_name + ".sikuli\\"
    print "path_script is: " + path_script    
    src_file=""
    if not "\\" in img: #for the img doesn't have path, only have file name, add path to get full path for source file
        if os.path.exists(path_common + img): src_file = path_common + img;print "img is from common folder, full path:" + src_file
        if os.path.exists(path_script + img): src_file = path_script + img;print "img is from script folder, full path:" + src_file
        dst_file = dst_path + "\\" + img  #destination file with path
        
    else: #for the img with full path, change the path to destination path for copy
        src_file = img
        print "img is from full path folder, full path:" + src_file
        img_path,img_name=os.path.split(img)
        dst_file = dst_path + "\\" + img_name #destination file with path
        print "should be full path, dst_file is:" + dst_file
        img = img_name 
    #copy the file to log folder 
    print "src_file is:" + src_file
    print "dst_file is:" + dst_file
    shutil.copyfile(src_file, dst_file)
    
    #write to logfile
    with open(logfile, 'a+') as fo:
        msg='\n<img border=\"0" src="' + img + '"></img_new>\n'  
        fo.write(msg)         

def write_img_log0(logfile,img):

    with open(logfile, 'a+') as fo:
        try:                                           
            print(img)    
            if '\\PF-' in logfile:
                script_name_old=str(logfile).split("\\PF-")[0]
            if '\\Logs' in script_name_old:
                script_name=str(script_name_old).replace("\\Logs", "")
            if '\\PF_WebApp' in script_name:
                common=str(script_name).split("\\PF_WebApp")[0]
                common=common +"\\PF_common_FF.sikuli\\"+ img     
            if os.path.exists(common):
                scr=common
                print(scr)
                dst=script_name_old+"\\"+ img
                print(dst)                
                shutil.copyfile(scr, dst)
                #open(dst,"w").write(open(scr,"r").read())
                msg='\n<img border=\"0" src="' + img+ '"></img>\n'  
                fo.write(msg)           
                return
            if "common" in img:
                scr=img
                img_new=str(randint(10000,99999))+'.png'                 
                print("in common" +scr)
                dst=script_name_old+"\\"+ img_new
                print("in common"+dst)
                shutil.copyfile(scr, dst)
                #open(dst,"w").write(open(scr,"r").read())
                msg='\n<img border=\"0" src="' + img+ '"></img_new>\n'  
                fo.write(msg) 
                return
            scr=script_name +".sikuli\\"+ img
            print("not common" +scr)
            dst=script_name_old+"\\"+ img
            print("not common"+dst)
            shutil.copyfile(scr, dst)
            #open(dst,"w").write(open(scr,"r").read())
            msg='\n<img border=\"0" src="' + img+ '"></img>\n'  
            fo.write(msg)           
        except IOError, e:
            print "Unable to copy file. %s" % e

        except:
            msg="in exception: There is an except when write img log!"
            print msg
            fo.write(msg)
            
def write_screenshot_log(logfile, img):
    with open(logfile, 'a+') as fo:
        print "in screenshot def, Image path is: " + img        
        img_path,img_name=os.path.split(logfile)
        cmd = "copy %s %s" % (img, img_path)
        os.system(cmd)
        path1,img_name=os.path.split(str(img))

        #print "Image path after copy is: " + img_name        
        msg = '<p>Screen shot during test is <a href=' +img_name + '>here</a></p>'
        #print "Screenshot msg in screenshot log    is:     " + msg
        fo.write(msg)

def cleanTestScript(testScript, removeSikExt = False): 
    if ".py.sikuli" in testScript:
        testScript = testScript.replace(".py.sikuli", "")

    if ".sikuli" in testScript:
        testScript = testScript.replace(".sikuli", "")    

    
    if removeSikExt:
        testScript = testScript.replace(".sikuli", "")
    print(testScript)    
    return testScript


def create_log_folder(test_case_script_name, testCase):

    timeStamp = str(time.strftime("%H%M%S"))
    test_case_script_name = cleanTestScript(test_case_script_name)
    print(test_case_script_name)
    log_path = _rootDir +"Logs\\" + test_case_script_name #+ "/log"+timeStamp    	
    suite_path =_rootDir +"Logs\\"
    failed_log_path = _rootDir +"Failed_Logs\\"
    log_file= log_path +"\\" +str(testCase)+ "-log.html"  
    
    if not os.path.exists(suite_path):     
        try:
            print "before create logfile!"
            os.mkdir(suite_path)
            print "log path created:  " + suite_path

        except:
            pass 

    if not os.path.exists(failed_log_path):     
        try:
            print "before create logfile!"
            os.mkdir(suite_path)
            print "log path created:  " + suite_path

        except:
            pass 

    if os.path.exists(log_path):
        print "log folder exists, will delete this folder!" 
        try:
            shutil.rmtree(log_path)
            print "Log folder is deleted!"
        except:
            print "log folder is not deleted, will append to the previous log file!"  
            
    try:
        os.mkdir(log_path)
        print "log path created:  " + log_path

    except:
        pass # fail silently if remote directory already exists    
    write_log(log_file,"The common last modified on "+_last_modifed)         
    return log_file   

def wait_find(y): 
    i=0
    while (not exists(y)and i<5):
        sleep(2)
        i+=1
    if exists(y):
        find(y).highlight(1)
        return 1
    else: return 0   

def wait_find_reg(reg,y): 
    i=0
    while not reg.exists(y):
        sleep(2)
        i+=1                
    if reg.exists(y):
        reg.find(y).highlight(1)
        return 1
    else: return 0  
                                
def wait_click(y): 
    i=0
    while (not exists(y) and i<5):
        sleep(2)
        i+=1
    if exists(y):
        find(y).highlight(1)
        click(y)
        return 1
    else: return 0

def verify_continue(logfile,image):
    x = wait_find(Pattern(image).similar(0.90))
    screen_shot=capture(0,0,1440,900)
    if x==1: 
        write_log(logfile,"Following expected image was found:\n")
        write_img_log(logfile,str(image))
        write_screenshot_log(logfile,screen_shot)
        return 1
    else:
        write_log(logfile,"Not able to find following image:\n")
        write_img_log(logfile, str(image))
        write_screenshot_log(logfile,str(screen_shot))    
        return 0
    
def verify_continue_with_similarity(logfile,image,similarity):
    x = wait_find(Pattern(image).similar(similarity))   
    screen_shot=capture(0,0,1440,900)
    if x==1: 
        write_log(logfile,"Following expected image was found:\n")
        write_img_log(logfile,str(image))
        write_screenshot_log(logfile,screen_shot)
        mouseMove(Location(1000,110))                
        return 1
    else:
        write_log(logfile,"Not able to find following image:\n")
        write_img_log(logfile, str(image))
        write_screenshot_log(logfile,str(screen_shot))  
        mouseMove(Location(1000,110))                
        return 0

def verify(logfile,image):
    x = wait_find(Pattern(image).similar(0.85))
    screen_shot=capture(0,0,1440,900)
    if x==1: 
        write_log(logfile,"Following expected image was found:\n")
        write_img_log(logfile,str(image))
        write_screenshot_log(logfile,screen_shot)
        mouseMove(Location(1000,110))
    else:
        write_log(logfile,"Not able to find following image:\n")
        write_img_log(logfile, str(image))
        write_screenshot_log(logfile,str(screen_shot))    
        raise Exception("Not able to find image " + str(image))

def verify_exactly(logfile,image):
    x = wait_find(Pattern(image).similar(0.99))
    screen_shot=capture(0,0,1440,900)
    if x==1:                 
        write_log(logfile,"Following expected image was found:\n")
        write_img_log(logfile,str(image))
        write_screenshot_log(logfile,screen_shot)
        mouseMove(Location(1000,110))                
    else:
        write_log(logfile,"Not able to find following image:\n")
        write_img_log(logfile, str(image))
        write_screenshot_log(logfile,str(screen_shot))    
        raise Exception("Not able to find image " + str(image))    
  
def locate_item_line_by_line(logfile,img):
    i=0; k=0

    while (not exists(img) and i<9):
        print "In loop, i is:" + str(i)
        sleep(1)                
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        i+=1
    mouseMove(Location(1000,120))
    if exists(img):
        find(img).highlight(1)
        write_log(logfile,"Following expected image was found:\n")
        write_img_log(logfile,str(img))        
        write_log_with_screenshot(logfile,"See Screenshot:")
        k=1
    else:
        print "image not exists"
        write_log(logfile, "Locate image in locate_item_line_by_line, not able to find image: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        raise Exception("Locate_item_line_by_line Exception: Not able to locate image: " + img)
    
def locate_item_page_by_page(logfile,img):
    i=0
    print "img in locate_item_page_by_page is:" + str(img)
    while (not exists(Pattern(img).similar(0.90)) and i<4):
        type(Key.PAGE_DOWN)
        mouseMove(Location(1000,110))        
        i+=1
        sleep(3)
    if exists(img):
        find(img).highlight(1)             
        write_log(logfile, "Locate image in locate_item_line_by_line, image found: " + str(img))
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        k=1
    else:
        write_log(logfile, "Locate image in locate_item_line_by_line, not able to find image: " + str(img))
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        raise Exception("Locate_item_page_by_page Exception: Not able to locate image: " +  str(img))                

def testScriptPaths():
     print "_rootDir= ", _rootDir, "\n_thisScript= ", _thisScript, "\n_commonDashDir= ", _commonDashDir, "\n_config_file= ", _config_file
     print "_email=", _email, "\n_password", _password, "\n"

     print _config.get('Delete_history', 'screen1')


def PassCase(logfile, test_case_id):
    test_script_name = str(logfile).split("\\")[3]
    msg =   test_script_name + " - Test Case Passed!"
    write_log_with_screenshot(logfile,msg)
    load_browser_with_url(_passed_link,logfile)    
    write_log(_test_suite_log,msg)
    msg="Tested URL:" + _PF_link
    write_log(logfile,msg)
    msg="Closing Privacyfix after test case finished...."
    write_log(logfile, msg)
    sleep(10)                    
    close_pf_tabs(logfile)
                    
def FailTestCase(logfile, test_case_id):

    test_script_name = str(logfile).split("\\")[3]
    print "test_script_name is:" + test_script_name
    
    msg = test_script_name + " - Test Case Failed!" 
    write_log_with_screenshot(logfile, msg)    
    
    load_browser_with_url(_failed_link,logfile)   
    sleep(2)
    write_log(_test_suite_log,msg)
    print "test suite log file is: " + _test_suite_log
    write_log(logfile,"Tested URL:" + _PF_link)
    sleep(3)  
    
    #05/02/2014 -- copy failed log folder to _rootDir failed_logs folder
    timeStamp = str(time.strftime("%H%M%S"))
    Failed_Logs_Folder = _rootDir + "Failed_Logs\\" + test_script_name + "_" + timeStamp +"\\"
    src_folder=_rootDir+"Logs\\"+ test_script_name+"\\"
    print "src_folder is: " + src_folder
    print "Failed_Logs_Folder is:" + Failed_Logs_Folder
    try:
        shutil.copytree(src_folder, Failed_Logs_Folder) 
    except shutil.Error:
        print "shutil error occurred."+str(shutil.Error)
    close_pf_tabs(logfile) 
            
def close_pf_tabs(logfile):
    write_log_with_screenshot(logfile, "Screenshot before close PF tabs:")
    pf_tab="1398774355412.png"
    if exists(pf_tab):
        PF_tabs=findAll(pf_tab)
        for tab in PF_tabs:
            sleep(2)    
            click (pf_tab)
            sleep(1)
            type("w", Key.CTRL)
    write_log_with_screenshot(logfile, "PF tabs are closed")      

def rememberPassword (logfile):
    if not exists(ff_icon):load_browser_with_url("",logfile)
    #click("1391019226848.png")
    sleep(2)                
    type("t",KeyModifier.ALT)      
    sleep(1)
    type("o")   
    sleep(1)
    verify(logfile,"security1.png")             
    click("security1.png")
    sleep(1)                
    if exists  (Pattern("1390815475723.png").exact()):
    
        click("1390815475723.png")
        verify(logfile,"1390815503711.png")         
        
        click("1390815503711.png")
        write_log(logfile,"Remember password was successfully disabled. " )                  
    else :
        click("1390815503711.png")
        write_log(logfile,"Remember password was already disabled." )  

#Reset account function                
def reset_data(logfile):
    reg=Region(1333,52,101,51)
    reg.highlight(1)
    if not exists(PF_icon):return
    load_browser_with_url(_reset_url,logfile)
    sleep(3)
    click("resetAddon.png")
    sleep(2)
    click("1390825284047.png")  
    sleep(1) 
    type("F", KeyModifier.ALT)
    sleep(1)
    type("x")
    sleep(2)                
    if exists("1390997737067-1.png"):click("1390997737067-1.png")            
    sleep(2)            
    load_browser_with_url(_PF_link,logfile) 
    wait_find(_PF_logo1)           

    write_log(logfile,"ADD-ON reseted" ) 

                                
#Reset account function                
def reset_account(logfile):
    reg=Region(1333,52,101,51)
    reg.highlight(1)
    if not exists(PF_icon):return
                
    ClearBrowsingData(logfile)            
    FacebookLogin(logfile)
    sleep(3)
    load_browser_with_url(_reset_url,logfile)
    sleep(3)

    click("resetAddon.png")
    sleep(2)
    click("1390825284047.png")  
    sleep(1)                

    wait_click("1404770039709.png")

    click("1390825080898.png")
    sleep(4)
    write_log_with_screenshot(logfile,"1404770039709.png")           
    if exists("connecthere.png"):
        
        wait_click("connecthere2.png")
        sleep(4)

        if exists("1390827287140.png"):        
            click("1390827287140.png")
        #if exists("1390825888908.png"):        
            #click("1390825888908.png")
        sleep(2)
                

    type("F", KeyModifier.ALT)
    sleep(1)
    type("x")
    sleep(2)                
    if exists("1390997737067.png"):click("1390997737067.png")            
    sleep(2)                
    load_browser_with_url(_PF_link,logfile)   
    if exists("1390466175476-2.png"):click("1390466175476-2.png")
    sleep(1)
    type(Key.F5) 
    waitVanish(Page_not_ready)                
    sleep(2)                

def ifPassword(log_file):
    reg=Region(2,1,427,211)           

    reg1=Region(481,196,451,134)            
    reg2=Region(458,360,504,305)
 #   if reg1.exists("1393580178856.png") or reg2.exists   
    sleep(5)            
    if not reg.exists("fixedIfpassword.png"):                
        sleep(1)                
        type(_password)
        sleep(1)
        write_log_with_screenshot(log_file,"linkedIn login.")
        #click("1393248232619.png")
        type(Key.ENTER)
        
def verify_link(logfile, link):         
        sleep(1)
        type("l", Key.CTRL)
        sleep(1)
        type("c", Key.CTRL)
        x = Env.getClipboard() 
        x = x.split("//")[1]
        if (x in link):
            write_log_with_screenshot(logfile,"Link is correct")
        else:         
            write_log_with_screenshot(logfile, "Link is:" + x + "  Expect link is:" + link)
            raise Exception("Link is Incorrect")                
            
                
                                
                                
if __name__ == "__main__":
    # This runs when executing PF_common directly, it will NOT run when importing.
    # if indented (under the if statement, if not indented it will always run.)
    testScriptPaths()
    #logfile="C:\\Automation_Firefox\\log.html"
    #locate_google_section(logfile)
	#protection_values()    
	#lst=protection_values()        
	#print lst[0]
	#print lst[1]  
    #RemoveExt("C:\\Automation_FF\\log.html")
    
    #InstallExtension("C:\\Automation_Firefox\\log.html")

    #create_log_folder("time_test","testCase_test_id_111")
    #ClearBrowsingData()                #avoid install link autofill for _PF_link
	#print "say hi from PF_common"
    #load_browser_with_url("google.com")
    logfile="C:\\log111.html"
    #GoogleLogin(logfile)                
#    locate_linkedIn_section(logfile)                
    reset_account(logfile)                
    #FacebookLogin(logfile)
    #LinkedInLogIn(logfile)                     
    #FailTestCase(logfile, "test_case_id")
    #rite_log(_test_suite_log,"test")
    #load_browser_with_url("google.com\n")
    #print "Total time for installation is: " + str(datetime.now()-start_time