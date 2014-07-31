
#4/11/2014 --- Kathy: changed image to smaller one in close_pf_tabs, to match PF family tab.
#4/15/2014 --- Kathy: added code in load browser, make sure browser is open to prevent typing link in other application.
#4/16/2014 --- Kathy: added lines in ClearBrowsingData() to return if history data is cleared, and verify 
                #history data is cleared after the clear action.
#5/1/2014 --- Kathy: change load browser, include url in the browser open command line to avoid install link showing incorretly
              #also kept the old load browser for the link has : in it which won't wrok in command line if url has :
              #the old load browser functin is used by ClearBrowsingData, disable_autofill, etc.

#05/02/2014 -- Added create failed logs folder in create function, added copy failed log folder to _rootDir failed_logs folder                      
#05/22/2014 -- David chanegd Locate FB, TW, Tracking, LK, Google sections; changed FB login, GL login, LK login
#05/23/2014 -- David created twitter login function, edited locate TW functions; added bigger simularity into verify function
#07/04/2014 -- Michael: fixed ClearBrowsingData, new InstallExtension, fixed Facebook and Google login
#07/07/2014 -- Michael: Fixed install extension

from __future__ import with_statement
import ConfigParser
import logging
import shutil
from sikuli import *
import os, re
from datetime import datetime
import time
from random import randint
############## Below is Ron's code, please don't touch #################
#This is the common script for Chrome
_scriptName = "PF_common.sikuli"

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

#_email = _config.get('Test_account', 'email1') 
#_password = _config.get('Test_account', 'pass1') 

_email="michael.scott.avg@gmail.com"
#_email="tester1avg@gmail.com"

#_password="avg123avg"
#_email="michael.scott.avg@gmail.com"
_password="US!pf.avg"

############## Below is Ron's code, please don't touch #################
if _useAutoUser:
    # when a Driver launches the TC's always use mzhang account.  
    _email = "mzhang0170@gmail.com"
    _password = "zhang0170"
############## Above is Ron's code, please don't touch #################

_last_modifed="7.21.2014 uploaded by kathy"
_passed_link = "dl.dropboxusercontent.com/u/40284694/passed.png"
_failed_link ="dl.dropboxusercontent.com/u/40284694/failed.png"
_chrome_appx86="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
_chrome_app="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
_install_link = "https://www.privacyfix.com/start/install"
_PF_link="privacyfix.com/start/"
_reset_url="http://privacyfix.com/start/reset"
_rootDir = os.path.dirname(sys.argv[0])
print "_rootDir is: " + _rootDir

#_test_suite_log="W:\\privacy-fix\\CH_test_setup_0502.html"
#_test_suite_log=_rootDir + "\\test_suite_log.html"
#print "_test_suite_log is: " + _test_suite_log

_ch1=("1387227872882.png") 
_ch2=("1387230266787.png")
_PF_logo=("1394850440234.png")

_PF_logo1=("1394848892120.png")


PF_icon=(Pattern("1386656905238.png").similar(0.90))
PF_icon_green=(Pattern("1394609482119.png").similar(0.90))
PF_icon_orange=(Pattern("1394609529596.png").similar(0.90))
Page_not_ready="1400659899854.png"


_rootDir = os.path.dirname(sys.argv[0].replace("/", "\\"))



if ".sikuli" in os.path.basename(_rootDir):

    _rootDir = os.path.dirname(_rootDir)
_rootDir = _rootDir + "\\"
#_rootDir = "W:\\scripts\\web_app\\chrome\\"
#_scriptName = 
_thisScript = _rootDir + _scriptName
print "_thisScript is:" +_thisScript
print "_rootDir: ", _rootDir
_test_suite_log=_rootDir + "\\test_suite_log.html"
print "_test_suite_log is: " + _test_suite_log

_commonDashDir = _thisScript + "\\config_dash\\"
_dirMap = {"dir":_commonDashDir}
_config_file= _commonDashDir + "config.txt" 



if os.path.isfile(_chrome_appx86):
    #check for x86 path (x64 bit) 
    _chrome_app = _chrome_appx86

_chrome_app = _chrome_app + " --start-maximized"

_config=ConfigParser.ConfigParser(_dirMap)
_config.read(_config_file)
FB_section_img=_config.get('Facebook_Login', "FB_section_img")

#Clear chrome browser history Data finction. Clear a browser history through browsers hot keys
#last update 0304_2014 by Kathy
def ClearBrowsingData(logfile):
    reg1=Region(146,108,298,57)
    reg2=Region(472,217,493,479)

    time=_config.get('Delete_history', 'screen1')
    begin=_config.get('Delete_history', 'screen2')
    begin1=_config.get('Delete_history', 'screen3')    
    load_browser_with_url(logfile,"chrome://history")
    if exists("1397592933995.png"):
        find("1397592933995.png").highlight(1)
        print "history is already cleaned!"
        return
    
    reg1.highlight(1)
    clear_browsing_data=("common_clear_browsing_data.png")
    wait_find_reg(reg1,clear_browsing_data)
    reg1.click(clear_browsing_data)
    sleep(2)
    reg2.highlight(1)   
    clear_browsing_history=(Pattern("common_browsing_history.png").similar(0.95))     
    if reg2.exists(clear_browsing_history):click(clear_browsing_history);sleep(1)

    download_history=(Pattern("common_clear_download_history.png").similar(0.95))
    if reg2.exists(download_history):click(download_history);sleep(1)

    clear_cookies=(Pattern("common_clear_cookies.png").similar(0.90))
    if reg2.exists(clear_cookies):click(clear_cookies);sleep(1)
    
    empty_cache=(Pattern("common_clear_cached_images.png").similar(0.95))   
    if reg2.exists(empty_cache):click(empty_cache);sleep(1)
    
    clear_password=(Pattern("common_clear_password.png").similar(0.95))    
    if reg2.exists(clear_password):click(clear_password);sleep(1)
    
    clear_autofill=(Pattern("common_clear_auto_file.png").similar(0.95))   
    if reg2.exists(clear_autofill):click(clear_autofill);sleep(1)

    hosted_app_data=(Pattern("common_clear_hosted_app_data.png").similar(0.97))
    if reg2.exists(hosted_app_data):click(hosted_app_data);sleep(1)

    reg2.click(time)
    sleep(2)
    reg2.click(begin1)
    sleep(1)
    type(Key.TAB)
    sleep(1)
    type(Key.ENTER)
    sleep(2)
    load_browser_with_url(logfile,"chrome://history\n ")
    if exists ("1397592933995.png"):
        print "Chrome history enteries deleted!"
    sleep(2)
    type("q", Key.CTRL+Key.SHIFT)     
    load_browser_with_url(logfile,"")

#added at 03062014 by Kathy
def reset_data(logfile):

    load_browser_with_url(logfile,_reset_url)
    sleep(5)
    
    #if not exists(PF_icon):return

    wait_click("1390478039571-1.png")

    click("1390478149468-1.png")     
    sleep(2)
    type("q", Key.CTRL+Key.SHIFT)
    load_browser_with_url(logfile,_PF_link)   
    
    if exists("1390466175476-3.png"):click("1390466175476-3.png")    
    sleep(2)

 
def reset_account(logfile):
    FacebookLogin(logfile)

    load_browser_with_url(logfile,_reset_url)
    sleep(7)

    if not exists(PF_icon):return


    wait_click("1390478039571.png")

    click("1390478149468.png")

    click("1390478078510.png")
    click("1390478168609.png")
    #wait_click("1390478291311.png")
    #sleep(2)
    #click("1390478307596.png")
    #sleep(2)
    #click("1390478321250.png")
    #sleep(2)
    load_browser_with_url(logfile,_PF_link)   
    if exists("1390466175476.png"):click("1390466175476.png")
    sleep(2)
    type("q", Key.CTRL+Key.SHIFT)
    sleep(2)
    load_browser_with_url(logfile,_PF_link)
    sleep(2)

#remove extension function.
def RemoveExt(logfile):
    if not exists(_ch1) and not exists(_ch2): 
        App.open(_chrome_app)
        wait_find(_ch2)
    #config=ConfigParser.ConfigParser()
    #config.read(config_file)
    PF_icon = _config.get('Uninstall', "button1")
    PF_icon_settings = _config.get('Uninstall', "button2")
    sleep(3)
    if exists(PF_icon):
        type("t", KeyModifier.CTRL)
        rightClick(PF_icon)
        sleep(1)
        type("r")
        sleep(2)
        type(Key.LEFT)
        type(Key.ENTER)
        write_log(logfile,"\n<p>Extension was remowed</p>\n")
    else:
        write_log(logfile, "PF already removed!")
        return
    write_log(logfile, "<p>extension removed successfully</p>\n")
    
#Install extension function. Take a install_link variable defined earlier and pass as argument
def InstallExtension(logfile):
    start_time=datetime.now()
    disable_autofill(logfile)  
    
    Get_AVG_PF = ("1404464088333.png")
    Add = ("1404464100931.png")

    Arrow= ("1389957193540.png")
    Skip= ("1389957226628.png")

    reg2=Region(23,0,1417,215)
    pfTab=("1400745489468.png")
    
    if reg2.exists(pfTab):        
        click (pfTab)
        print "PF is already installed!"
        write_log_with_screenshot(logfile, "PF is already installed!")
        return
    
    
    load_browser_with_url(logfile,"about:blank",)   
    sleep(3)            
    if exists(Pattern(PF_icon).similar(0.90) or PF_icon_green or PF_icon_orange):
        find(PF_icon).highlight(1)
        print "PF is already installed!"
        write_log_with_screenshot(logfile, "PF is already installed!")
        return
    load_browser_with_url(logfile,_install_link)
    verify(logfile,Get_AVG_PF)
    click(Get_AVG_PF)
    wait(2)
    click(Add)


    wait(5)
    i=0
    while (i < 3):
        if exists(Arrow):click(Arrow)
        wait(2)
        i+=1  
        print "i is:" + str(i)


   
    sleep(5)
    type(Key.ESC)

    sleep(1)
    type("w", Key.CTRL)
    sleep(1)
    ClearBrowsingData(logfile) 
    write_log(logfile, "History data cleared!")
    write_log_with_screenshot(logfile, "Extension installed successfully")
    write_log(logfile, "Total time for installation is: " + str(datetime.now()-start_time))  

def locate_linkedIn_section(logfile):

    linkedIn_section_img =_config.get('Google_Login', 'linkedIn_section_img')
    linkedIn_section_img1=("1400741734805.png")
    not_logged=("1400742418324.png")
    if not exists(linkedIn_section_img):
        load_browser_with_url(logfile,_PF_link)
        wait_find(Page_not_ready)
        sleep(5)
        type(Key.END)
        sleep(2)
    if exists(Pattern(not_logged).similar(0.98)):
        write_log(logfile,"Following expected image was found:\n")
        write_img_log(logfile,str(not_logged))
        write_log(logfile,"You are not logged to LinkedIn")
        return 0
    else:
        sleep(2)
        locate_item_page_by_page(logfile,linkedIn_section_img)
        locate_item_line_by_line(logfile,linkedIn_section_img1, 0.95)
        mouseMove(Location(1000,100))
        return 1
     
#find google section image, an Tracking section image
#This is to make sure the whole google section is completely showing on screen
def locate_google_section(logfile):
    google_section_img=_config.get('Google_Login', 'google_section_img')
    tracking_section_img=_config.get('Google_Login', 'tracking_section_img')
    type(Key.HOME)
    sleep(2)
    if not exists(google_section_img):
        load_browser_with_url(logfile,_PF_link)
        wait_find(Page_not_ready)
        sleep(5)
    type(Key.DOWN+Key.DOWN+Key.DOWN+Key.DOWN+Key.DOWN)
    mouseMove(Location(1000,120))
    
def locate_tracking_section(logfile):    #locate both tracking and websites section together
   
    if not exists(Page_not_ready):
        load_browser_with_url(logfile,_PF_link)
        wait_find(Page_not_ready)
        sleep(5)    
    mouseMove(Location(1000,120))    
    

def locate_facebook_section(logfile):

    fb_logged_in=("1400660343807.png")    
    if not exists(fb_logged_in):
        load_browser_with_url(logfile,_PF_link)
        sleep(5)
        wait_find(Page_not_ready)
    i=0
    while (not exists(fb_logged_in) and i<2):
        type(Key.PAGE_DOWN)
        mouseMove(Location(1000,110))        
        i+=1
        sleep(3)
    if (not exists (fb_logged_in)):
        type(Key.HOME)
        return 0
    else:
        bottom=("1400745371262.png")  
        locate_item_line_by_line(logfile,bottom, 0.98)
        return 1

def locate_twitter_section(logfile):
    TW_logged_in=(Pattern("1400763752222.png").similar(0.91))
    if not exists(TW_logged_in):
        load_browser_with_url(logfile,_PF_link)
        sleep(5)
        wait_find(Page_not_ready)
    type(Key.HOME)    
    mouseMove(Location(1000,110))    
    type(Key.PAGE_DOWN)
    sleep(2)
    if exists(Pattern("1400764599480.png").similar(0.90)):
        return 0
    else:
        return 1

def Twitter_login(logfile):
    start_time=datetime.now()
    write_log(logfile, "detecting browser...")
    loginbutton=("1400828304260.png")
    loggedin=("1400829473286.png")
    TW_logged_in=("1400829560638.png")
    twitter_page=("1400829906443.png")
    if locate_twitter_section(logfile)==1:
        mouseMove(Location(1000,120))
        write_log_with_screenshot(logfile, "Twitter is already logged in!")  
        write_log(logfile, "total time detect logged in is: " + str(datetime.now()-start_time)) 
        return
    locate_item_page_by_page(logfile,loginbutton, 0.95)
    click(Pattern(loginbutton).similar(0.95).targetOffset(224,0))
    wait_find(twitter_page)
    type("mscott0380")
    sleep(1)
    type(Key.TAB)
    sleep(1)
    type("US!pf.avg")
    sleep(1)
    type(Key.ENTER)
    verify(logfile,loggedin)
    type('w', Key.CTRL)
    wait_find(TW_logged_in)
    locate_twitter_section(logfile)
    mouseMove(Location(1000,120))
    write_log_with_screenshot(logfile, "Successfully logged in into Twitter")  
    write_log(logfile, "total time detect logged in is: " + str(datetime.now()-start_time)) 
    
#Login to google account
def GoogleLogin(logfile):
    start_time=datetime.now()

    write_log(logfile, "detecting browser...")
    if not exists(_PF_logo):
        load_browser_with_url(logfile,_PF_link)
        wait_find(Page_not_ready)
        if exists("1390466175476.png"):click("1390466175476.png")
        sleep(5)

    write_log(logfile, "total time detecting browser is: " + str(datetime.now()-start_time))   
    locate_google_section(logfile)

    google_login=(Pattern("1404713461410.png").similar(0.84))
    
    if exists(google_login):
        #load_browser_with_url("https://accounts.google.com")
        #click(google_login)
        google_account_link="https://accounts.google.com/Login?continue=https://history.google.com/history/settings%3Fhl%3Den&hl=en"
        load_browser_with_url(logfile,google_account_link)
        wait_find("1395097448887.png")
        sleep(2)
        if exists(Pattern("1400736781514.png").similar(0.90)):
            sleep(2)
            type(_email)
            sleep(1)
            type(Key.TAB)
        type(_password)
        sleep(1)
        type(Key.ENTER)
        sleep(2)
        verify(logfile,"1404475286567.png")
                
        write_log(logfile, "logged into Google successfully\n")
        write_log(logfile, "Total time for Google login is: " + str(datetime.now()-start_time))  
        load_browser_with_url(logfile,_PF_link)
        wait_find(Page_not_ready)
        locate_google_section(logfile)
        write_log(logfile,"logged into Google successfully\n")
        mouseMove(Location(1000,100))
           
    else: 
        write_log(logfile, "Already logged into Google!\n")
        print "Already logged into Google!\n"        
        write_log(logfile, "Total time for Google login is: " + str(datetime.now()-start_time)) 
        mouseMove(Location(200,50))
        
#Logging to Facebook
def FacebookLogin(logfile):
    
    start_time=datetime.now()
    FB_reg=Region(0,0,300,300)
    Maybe_reg=Region(720,450,720,450)
    FB_reg.highlight(1)    
    logged = _config.get('Facebook_Login', "logged")
    loginbutton = ("1404474223554.png")
    fb_logged_in_icon=_config.get('Facebook_Login', "fb_logged_in_icon")
    FB_section_img=_config.get('Facebook_Login', "FB_section_img")
    #locate_facebook_section(logfile)
    if locate_facebook_section(logfile)==1:
        mouseMove(Location(1000,120))
        write_log_with_screenshot(logfile, "Facebook is already logged in!")  
        write_log(logfile, "total time detect logged in is: " + str(datetime.now()-start_time)) 
        return
    #if login button shown in facebook section, then login to facebook section
    fb_logo = _config.get('Facebook_Login', "FB_logo")
    cert_warning = _config.get('Facebook_Login', "cert_warning")
    proceed = _config.get('Facebook_Login', "proceed")
    locate_item_page_by_page(logfile,loginbutton)
    click(Pattern(loginbutton).similar(0.90).targetOffset(224,0))
    sleep(2)

    ok_reg=Region(700,450,300,300)   
    
    ok_button=("1396524852014.png")
    okay=("1396524883128.png")
    
    if ok_reg.exists(ok_button):
        click(ok_button) 
        wait_click(ok_button)
    sleep(2)
    if ok_reg.exists(okay):
        click(okay) 
        wait_click(okay)
    write_log(logfile, "total time after detect OK button is: " + str(datetime.now()-start_time))     
    wait_find(fb_logo)
    login_reg=Region(514,264,312,145)
    login_reg.highlight(1)
    
    if login_reg.exists(Pattern("1390183106564.png").similar(0.90)) or login_reg.exists(Pattern("1389809891723.png").similar(0.90)):
        sleep(2)
        type(_email)
        sleep(2)
        write_log_with_screenshot(logfile,"email entered")
        type(Key.TAB)
        sleep(2)
    type(_password)
    write_log_with_screenshot(logfile,"password entered")    
    sleep(2)
    type(Key.ENTER)
    sleep(5)
    write_log_with_screenshot(logfile,"after login to facebook")
    write_log(logfile, "total time detecting logged in is: " + str(datetime.now()-start_time))
    
    if ok_reg.exists(ok_button):
        click(ok_button) 
        wait_click(ok_button)
    
    
    verify(logfile,fb_logged_in_icon)
    write_log_with_screenshot(logfile, "Logged into Facebook successfully!")
    locate_item_line_by_line(logfile,"1400745387897.png",0.98)

    write_log(logfile, "Total Facebook login time is: " + str(datetime.now()-start_time))  
    mouseMove(Location(1000,100))
                
def LinkedInLogIn(logfile):

    start_time=datetime.now()     
    logged_in_linkedIn = _config.get('LinkedIn_check', 'logged_in_linkedIn')
    loginbutton = _config.get('LinkedIn_check', 'screen1')
    linkedin_section_img=_config.get('LinkedIn_check', 'linkedin_section_img')
    linkedIn_profile=_config.get('LinkedIn_check', 'linkedIn_profile')  
    
    #if profile image exists, it means linkedin is logged in already
    if locate_linkedIn_section(logfile)==1:
        write_log_with_screenshot(logfile, "Already logged in LinkedIn!")  
        mouseMove(Location(1000,100))
        return
        
    verify(logfile, loginbutton) 
    click (Pattern(loginbutton).similar(0.95).targetOffset(223,4))
    verify(logfile, "1389206359172.png")
            
    if exists("1387572272054.png"):
        sleep(1)

        type(_email)
        sleep(1)
        type(Key.TAB)
    type(_password)
    type(Key.ENTER)
    sleep(5)
    verify(logfile,logged_in_linkedIn)
    write_log_with_screenshot(logfile, "logged into LinkedIn successfully")
    write_log(logfile, "LinkedIn login time is: " + str(datetime.now()-start_time))  
    #close the logged in tab, suppose to close by itself. it's a bug right now, if fixed in the future, please delete this line
    type('w', Key.CTRL)
    sleep(1)
    wait_find(linkedin_section_img)
    write_log_with_screenshot(logfile, "Total LinkedIn login time is: " + str(datetime.now()-start_time))
     
def write_log(logfile,msg):
    with open(logfile, 'a+') as fo:
        fo.write("\n<p> " + str(datetime.now())+ ":   " + msg + " </p>\n")

    
def write_log_with_screenshot(logfile,msg):
    write_log(logfile,msg)
    scr_shot=capture(0,0,1440,900)
    write_screenshot_log(logfile,scr_shot)



def write_screenshot_log(logfile, img):
    
    with open(logfile, 'a+') as fo:
        #print "in screenshot def, Image path is: " + img        
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

    #timeStamp = str(time.strftime("%H%M%S"))
    test_case_script_name = cleanTestScript(test_case_script_name)
    print(test_case_script_name)
    log_path = _rootDir +"Logs\\" + test_case_script_name #+ "-"+timeStamp  
    
    ##### Ron's code, don't touch #######
    if _saveLogToRW:
        log_path = _log_root + cleanTestScript(testScript, True)
    ##### Ron's code, don't touch #######    
    
    suite_path=_rootDir +"Logs\\"
    Failed_log_foler=_rootDir + "Failed_Logs\\"
    log_file= log_path +"\\" +str(testCase)+ "-log.html"  
    
    if not os.path.exists(suite_path):     
        try:
            print "before create logfile folder!"
            os.mkdir(suite_path)
            print "log path created:  " + suite_path

        except:
            pass 

    if not os.path.exists(Failed_log_foler):     
        try:
            print "before create Failed_logs folder!"
            os.mkdir(Failed_log_foler)
            print "Failed_Logs folder created:  " + Failed_log_foler
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
        print "before create logfile!"
        os.mkdir(log_path)
        print "log path created:  " + log_path

    except:
        pass # fail silently if remote directory already exists    
    write_log(log_file,"The common last modified"+_last_modifed)      
    return log_file   

def write_img_log(logfile,img):
    print "img is:" + img
    path_common=_rootDir + _scriptName + "\\"
    print "path_common is: " + path_common

    dst_path, script_name =os.path.split(logfile)
    print "dst_path is: " + dst_path
    print "script_name is" + script_name
    
    script_path, script_name=os.path.split(dst_path)
    path_script=_rootDir + script_name + ".sikuli\\"
    print "path_script is: " + path_script
    
    src_file=""
    if not "\\" in img: #for the img doesn't have path, only have file name, add path to get full path for source file
        if os.path.exists(path_common + img): src_file = path_common + img;print "img is from common folder, full path:" + src_file
        if os.path.exists(path_script + img): src_file = path_script + img;print "img is from script folder, full path:" + src_file
        print "img without path, src_file is:" + src_file
        dst_file = dst_path + "\\" + img  #destination file with path
        print "dst_file is: " + dst_file
    else: #for the img with full path, change the path to destination path for copy
        src_file = img
        path, img_name=os.path.split(img)
        dst_file = dst_path + "\\" + img_name #destination file with path
        print "img file has full path, src_file is:" + src_file
        print "dst_file is: " + dst_file
    #copy the file to log folder 
    shutil.copyfile(src_file, dst_file)
    
    #write to logfile
    with open(logfile, 'a+') as fo:
        msg='\n<img border=\"0" src="' + dst_file+ '"></img_new>\n'  
        fo.write(msg)         

def write_img_log0(logfile,img):

    w=""
    with open(logfile, 'a+') as fo:

        try:                                           
                
            if '\\PF-' in logfile:
                script_name_old=str(logfile).split("\\PF-")[0]
            if '\\Logs' in script_name_old:
                script_name=str(script_name_old).replace("\\Logs", "")
            if '\\PF_WebApp' in script_name:
                common=str(script_name).split("\\PF_WebApp")[0]
                common=common +"\\PF_common.sikuli\\"+ img     
            if os.path.exists(common):
                scr=common
                print(scr)
                dst=script_name_old+"\\"+ img
                print(dst)                
                shutil.copyfile(scr, dst)
                #open(dst,"w").write(open(scr,"r").read())
                msg='\n<img border=\"0" src="' + dst+ '"></img>\n'  
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
                msg='\n<img border=\"0" src="' + dst+ '"></img_new>\n'  
                fo.write(msg) 
                return
            scr=script_name +".sikuli\\"+ img
            print("not common" +scr)
            dst=script_name_old+"\\"+ img
            print("not common"+dst)
            shutil.copyfile(scr, dst)
            #open(dst,"w").write(open(scr,"r").read())
            msg='\n<img border=\"0" src="' + dst+ '"></img>\n'  
            fo.write(msg)           
        except IOError, e:
            print "Unable to copy file. %s" % e

        except:
            msg="in exception: There is an except when write img log!"
            print msg
            fo.write(msg)
            
            
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
    while (not reg.exists(y)and i<5):
        sleep(2)
        i+=1
    if reg.exists(y):
        reg.find(y).highlight(1)
        return 1
    else: return 0 

def wait_click(y): 
    i=0
    while (i<5):
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
        return 1
    else:
        write_log(logfile,"Not able to find following image:\n")
        write_img_log(logfile, str(image))
        write_screenshot_log(logfile,str(screen_shot))    
        return 0

def verify(logfile,image):

    x = wait_find(Pattern(image).similar(0.90))
    screen_shot=capture(0,0,1440,900)
    if x==1: 
        write_log(logfile,"Following expected image was found:\n")
        write_img_log(logfile,image)
        write_screenshot_log(logfile,screen_shot)

    else:
        write_log(logfile,"Not able to find following image:\n")
        write_img_log(logfile,image)
        write_screenshot_log(logfile,str(screen_shot))    
        raise Exception("Not able to find image " + str(image))

def verify_exactly(logfile,image):

    x = wait_find(Pattern(image).similar(0.99))
    screen_shot=capture(0,0,1440,900)
    if x==1: 
        write_log(logfile,"Following expected image was found:\n")
        write_img_log(logfile,str(image))
        write_screenshot_log(logfile,screen_shot)
    else:
        write_log(logfile,"Not able to find following image:\n")
        write_img_log(logfile, str(image))
        write_screenshot_log(logfile,str(screen_shot))    
        raise Exception("Not able to find image " + str(image))    

def load_browser_with_url_0(logfile,link):
    reg1=Region(1268,25,171,35)
    start_time=datetime.now()
    reg1.highlight(1)
    if reg1.exists("1393420720867.png"): type("w", Key.CTRL);sleep(1)
    
        #write_log(logfile, "total time detecting chrome not open is: " + str(datetime.now()-start_time))
    App.open(_chrome_app + "  " + link)
    
    print "total time open chrome is: " + str(datetime.now()-start_time)
    wait_find_reg(reg1,"1393420720867.png")
    if exists("1395170923573.png"):click("1395170923573.png")          
    print "total time detecting chrome is loaded: " + str(datetime.now()-start_time)


def load_browser_with_url(logfile, link):
    reg1=Region(1268,25,171,35)
    start_time=datetime.now()
    reg1.highlight(1)
    if not reg1.exists("1393420720867.png"):  
        #write_log(logfile, "total time detecting chrome not open is: " + str(datetime.now()-start_time))
        App.open(_chrome_app)

        print "total time open chrome is: " + str(datetime.now()-start_time)
        wait_find_reg(reg1,"1393420720867.png")
        if exists("1395170923573.png"):click("1395170923573.png")          
        print "total time detecting chrome is loaded: " + str(datetime.now()-start_time)

    else:    
        switchApp("Google Chrome")
        if exists("1395170923573.png"):click("1395170923573.png")             

    sleep(3) 
    type('l', KEY_CTRL)
    sleep(2)
    type(link)
    sleep(2)
    type(Key.ENTER)
    sleep(2)
    type(Key.HOME)
    mouseMove(Location(1000,100))

 
def locate_item_line_by_line(logfile,img, pattern=0.90):
    i=0
    k=0
    
    while (not exists(Pattern(img).similar(pattern)) and i<12):
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        mouseMove(Location(1000,100))
        i+=1
    if exists(Pattern(img).similar(pattern)):
        find(Pattern(img).similar(pattern)).highlight(1)
        write_log(logfile, "Locate image in locate_item_line_by_line, image found: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        k=1
    else:
        write_log(logfile, "Locate image in locate_item_line_by_line, not able to find image: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        raise Exception("Locate_item_line_by_line Exception: Not able to locate image: " + img)
    
def locate_item_page_by_page(logfile,img, pattern=0.90):
    i=0
    type(Key.HOME)
    sleep(1)
    while (not exists(Pattern(img).similar(pattern)) and i<6):
        type(Key.PAGE_DOWN)
        mouseMove(Location(200,50))        
        sleep(3)
        i+=1
        
    if exists((Pattern(img).similar(pattern))):
        find((Pattern(img).similar(pattern))).highlight(1)
        write_log(logfile, "Locate image in locate_page_by_page, image found: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        k=1
    else:
        write_log(logfile, "Locate image in locate_page_by_page, not able to find image: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        raise Exception("Locate_item_page_by_page Exception: Not able to locate image: " + img)



def get_img_value(logfile,image,text):
    wait_click("1388032151500.png")
    sleep(1)
    
    type(Key.F12)
    wait_click("1388032189908.png")
    
    type("f", Key.CTRL)
    sleep(3)
    type(text)
    sleep(3)
    write_log_with_screenshot(logfile, "after enter search text")
    #type(Key.ENTER)
    sleep(2)
    write_log_with_screenshot(logfile, "search result screen after one more enter:")
    #type(Key.ENTER)
 #   write_log_with_screenshot(logfile, "search result screen after two more enter:")    
    
    if exists(image):
        click(image)
        sleep(1)
        type("c", KEY_CTRL)
        write_log_with_screenshot(logfile, "CTRL_C pressed!")
        sleep(2)
        #App.open("%windir%\system32\notepad.exe")
        #sleep(3)
        #type("v", Key.CTRL)
        data=Env.getClipboard()
        print "txt: " + str(data)
        value1=(data.split('>')[1]).split('<')[0]
        value1=int(value1.replace('%',''))
        type(Key.F12)        
        print value1
        return value1

    else : print "fail"

def get_protection_value(logfile):
    
    search_txt1="1391414402816.png"
    
    #search_txt2="1386700206064-1.png"

    #search_txt1= "1387454285798.png"
    
    switchApp("Google Chrome")
    #search_str2="num_private_settings\n"
    search_str1="strong#fb_protection_percent.percentage"
    #print "search img: " +str(search_txt1)
    percent_value = get_img_value(logfile,search_txt1, search_str1)
    msg="Protection value is:" + str(percent_value)
    write_log_with_screenshot(logfile, msg)
    mouseMove(Location(1000,100))
    return percent_value
    

def testScriptPaths():
     print "_rootDir= ", _rootDir, "\n_thisScript= ", _thisScript, "\n_commonDashDir= ", _commonDashDir, "\n_config_file= ", _config_file
     print _config.get('Delete_history', 'screen1')


def PassCase(log_file, test_case_id):
    load_browser_with_url(log_file,_passed_link)
    test_script_name = ""

    test_script_name = str(log_file).split("\\")[3]
    print "test_script_name is:" + test_script_name
     
    msg =   test_script_name + " - Test Case Passed!"
    
    write_log_with_screenshot(log_file,msg)
    write_log(_test_suite_log,msg)
    msg="Tested URL:" + _PF_link
    write_log(log_file,msg)
    msg="Closing browser after test case finished...."
    write_log(log_file, msg)
    sleep(10)    
    close_pf_tabs(log_file)

    
def FailTestCase(logfile, test_case_id):
    load_browser_with_url(logfile,_failed_link)   
    sleep(2)

    test_script_name = str(logfile).split("\\")[3]
    print "test_script_name is:" + test_script_name
    
    msg = test_script_name + " - Test Case Failed!"
    write_log_with_screenshot(logfile, msg)
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
        print "shutil error occurred."
    #shutil.move(Failed_Logs_Folder,Failed_Logs_Folder+"_"+timeStamp)       
    close_pf_tabs(logfile)  


def close_pf_tabs(logfile):
    write_log_with_screenshot(logfile, "Screenshot before close PF tabs:")
    pf_tab=("1397187372215.png")
    
    if exists(pf_tab):
        PF_tabs=findAll(pf_tab)
        for tab in PF_tabs:
            click (pf_tab)
            type("w", Key.CTRL)
    write_log_with_screenshot(logfile, "PF tabs are closed")     
    
def close_browser(logfile):    
    verify(logfile,"1388806538311.png")
    click("1388806538311.png")
    verify(logfile,"1388806596083.png")
    click("1388806596083.png")
    write_log_with_screenshot(logfile, "The above test case is done, browser closed!")
    
def ifPassword(logfile):
    if exists("1406121015600.png"):
        sleep(2)
        type(_password)
        sleep(1)
        type(Key.ENTER)
        sleep(2)


def verify_link(logfile, link):         
        sleep(1)
        type("l", Key.CTRL)
        sleep(1)
        type("c", Key.CTRL)
        x=Env.getClipboard()        
        if (x==link):
            write_log(logfile,"Link is correct")
        else:         
            write_log(logfile, "Link is Incorrect")
            raise Exception("Link is Incorrect")

#disable autofill for chrome browser
def disable_autofill(logfile):
    load_browser_with_url(logfile,"chrome://settings/search#password")

    wait_find("1398984037415.png")

    
    auto_complete1=("auto_comlete_url-1.png")

    if exists(Pattern(auto_complete1).similar(0.95)):
        find(auto_complete1).highlight(1)        
        click(auto_complete1)
    auto_complete2=("1395321409938-1.png")

    if exists(Pattern(auto_complete2).similar(0.95)):
        find(auto_complete2).highlight(1)        
        click(auto_complete2)    
    sleep(1)

    #disable password autofill

    enable_autofill_password=("enable_autofill_password-1.png")
    offer_save_password=("1397084314994.png")
    
    
    if exists(Pattern(enable_autofill_password).similar(0.95)):
        find(enable_autofill_password).highlight(1)        
        click(enable_autofill_password)

    if exists(Pattern(offer_save_password).similar(0.95)):
        find(offer_save_password).highlight(1)           
        click(offer_save_password)


if __name__ == "__main__":
    # This runs when executing PF_common directly, it will NOT run when importing.
    # if indented (under the if statement, if not indented it will always run.)
    print "sys.argv: ", sys.argv 
    #testScriptPaths()
#test_case_id="3233"
#logfile='C:\\Automation_PF\\Logs\\PF_WebApp_FB01_Findable_OnGoogle_GreyToGreen_1331\\PF-1331-log.html'
#img='C:\\Automation_PF\\PF_common.sikuli\\config_dash\\Delete_history\\begin.png'
#write_img_log(logfile,img) 
#ClearBrowsingData()
#load_browser_with_url(_PF_link)
#App.open(_chrome_app + "  " + _PF_link)
#load_browser_with_url("privacyfix.com/start")