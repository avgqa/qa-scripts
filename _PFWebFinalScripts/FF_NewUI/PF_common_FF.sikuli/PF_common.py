from __future__ import with_statement
import ConfigParser
import logging
from sikuli import *
import os, re
from datetime import datetime


_passed_link = "dl.dropboxusercontent.com/u/40284694/passed.png"
_failed_link ="dl.dropboxusercontent.com/u/40284694/failed.png"
_chrome_appx86="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
_chrome_app="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
_install_link = "https://stage.privacyfix.com/start/install"
_PF_link="https://stage.privacyfix.com/start/"
_ch1=("1387227872882.png") 
_ch2=("1387230266787.png")
_PF_logo="1387925221847.png"
#_email = _config.get('Test_account', 'email1') 
#_password = _config.get('Test_account', 'pass1') 

_rootDir = os.path.dirname(sys.argv[0].replace("/", "\\"))

if ".sikuli" in os.path.basename(_rootDir):
    # Running in command line returns the path including the sikuli script, different from IDE
    _rootDir = os.path.dirname(_rootDir)
_rootDir = _rootDir + "\\"
#_rootDir = "W:\\scripts\\web_app\\chrome\\"

_thisScript = _rootDir + "PF_common.sikuli"

_commonDashDir = _thisScript + "\\config_dash\\"
_dirMap = {"dir":_commonDashDir}
_config_file= _commonDashDir + "config.txt" 

if os.path.isfile(_chrome_appx86):
    #check for x86 path (x64 bit) 
    _chrome_app = _chrome_appx86

_chrome_app = _chrome_app + " --start-maximized"

_config=ConfigParser.ConfigParser(_dirMap)
_config.read(_config_file)
_email = _config.get('Test_account', 'email1') 
_password = _config.get('Test_account', 'pass1') 
#_email="aleoshina@gmail.com"
#_password="leoshinaA"

#Clear chrome browser history Data finction. Clear a browser history through browsers hot keys
def ClearBrowsingData():
    time=_config.get('Delete_history', 'screen1')
    begin=_config.get('Delete_history', 'screen2')
    begin1=_config.get('Delete_history', 'screen3')    
    load_browser_with_url(" ")
    sleep(2)
    type("l", KEY_CTRL)
    type("chrome://history\n")#Num Lock keyboard should be disabled 
    wait_click("1386356581840.png")
    if wait_find(begin):
        type(Key.ENTER)
    else:
        wait_click(time)
        sleep(2)
        click(begin1)
        sleep(2)
        type(Key.TAB)
        type(Key.ENTER)        
    sleep(2)
    #type(Key.F4, KeyModifier.ALT)
   

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
    write_log(logfile, "start installation. Detecting chrome browser...")

    if not exists(_ch1) and not exists(_ch2): App.open(_chrome_app)

    write_log(logfile, "Finished detecting chrome browser...")
    
    PF_icon=Pattern("1386656905238.png").similar(0.90)
    
    if exists(PF_icon):
        print "PF is already installed!"
        write_log(logfile, "PF is already installed!")
        return
    
    load_browser_with_url(_install_link)
    cert_warning = _config.get('Facebook_Login', "cert_warning")
    proceed = _config.get('Facebook_Login', "proceed")
    print "sections: " + str(_config.sections()[0])
    a=_config.get('Installation_check', 'screen1')
    items=len(_config.items('Installation_check'))
    print "a is: ", str(a)
   
    i=1
    print "items is: ", items
    while (i < items):
        print "i is: ", i

        screen=_config.get('Installation_check', 'screen'+str(i))

        verify(logfile,screen)
        click(screen)
        if exists(cert_warning):
            click(proceed)
        i+=1     
    sleep(2)
    ClearBrowsingData() 
    write_log(logfile, "<p>extension installed successfully</p>\n")
    write_log(logfile, "Total time for installation is: " + str(datetime.now()-start_time))  

def locate_linkedIn_section(logfile):
    #load_browser_with_url(_PF_link)
    type(Key.HOME)  
    if not exists(_PF_logo):
        load_browser_with_url(_PF_link)
        wait_find(_PF_logo)
    
    linkedIn_section_img =_config.get('Google_Login', 'linkedIn_section_img')
    google_section_img=_config.get('Google_Login', 'google_section_img')
    #print "LinkedIn image: " + linkedIn_section_img
    locate_item_page_by_page(logfile, linkedIn_section_img)   
    sleep(1)
    locate_item_line_by_line(logfile, google_section_img)
    mouseMove(Location(200,10))
     
#find google section image, and use down key to find Tracking section image
#This is to make sure the whole google section is completely showing on screen
def locate_google_section(logfile):
 #   load_browser_with_url(_PF_link)
    type(Key.HOME)
    sleep(1)
    if not exists(_PF_logo):
        load_browser_with_url(_PF_link)
        wait_find(_PF_logo)
    #google_section_img=_config.get('Google_Login', 'google_section_img')
    #tracking_section_img=_config.get('Google_Login', 'tracking_section_img')
    #print "Google section img: " + google_section_img
    #print "tracking section img: " + tracking_section_img
    #locate_item_page_by_page(logfile, google_section_img)
    #sleep(1)
    #locate_item_line_by_line(logfile,tracking_section_img)
    type(Key.END)
    type(Key.PAGE_UP)
    type(Key.PAGE_UP)
    mouseMove(Location(200,10))
    
def locate_tracking_section(logfile):    
    type(Key.HOME)
    if not exists(_PF_logo):
        load_browser_with_url(_PF_link)
        wait_find(_PF_logo)
    type(Key.END)
    #websites_section_end =_config.get('Google_Login', 'websites_section_img_2')
   # verify(logfile,websites_section_end)
    type(Key.PAGE_UP)  
    mouseMove(Location(200,10))
    

def locate_websites_section(logfile):
    type(Key.HOME)
    if not exists(_PF_logo):
        load_browser_with_url(_PF_link)
        wait_find(_PF_logo)
    type(Key.END)
    type(Key.PAGE_UP)
    type(Key.DOWN)
    type(Key.DOWN)
    mouseMove(Location(200,10))
   # websites_section_img =_config.get('Google_Login', 'websites_section_img')
   # websites_section_img_2 =_config.get('Google_Login', 'websites_section_img_2')
    #print "Websites section image: " + websites_section_img_2
    #locate_item_page_by_page(logfile, websites_section_img)
    #sleep(1)
    
 #   locate_item_line_by_line(logfile, websites_section_img_2)   
    

#Login to google account
def GoogleLogin(logfile):
    start_time=datetime.now()
    type(Key.HOME)
    write_log(logfile, "detecting browser...")
    if not exists(_PF_logo):
        load_browser_with_url(_PF_link)
        wait_find(_PF_logo)
    write_log(logfile, "total time detecting browser is: " + str(datetime.now()-start_time)) 

    
    locate_google_section(logfile)

    google_login=("1387304206285.png")
    
    if exists(google_login):
        load_browser_with_url("https://accounts.google.com")
        sleep(2)
        if exists(Pattern("1387572416970.png").similar(0.90)):
            type(_email)
            sleep(1)
            type(Key.TAB)
        type(_password)
        sleep(1)
        type(Key.ENTER)
        sleep(2)
        verify(logfile,"1388176974274.png")       
        write_log(logfile, "logged into Google successfully\n")
        write_log(logfile, "Total time for Google login is: " + str(datetime.now()-start_time))  
        load_browser_with_url(_PF_link)
        wait_find(_PF_logo)
        locate_google_section(logfile)
        write_log(logfile,"logged into Google successfully\n")
        mouseMove(Location(200,10))
           
    else: 
        write_log(logfile, "Already logged into Google!\n")
        print "Already logged into Google!\n"        
        write_log(logfile, "Total time for Google login is: " + str(datetime.now()-start_time)) 
        mouseMove(Location(200,10))
        
#Logging to Facebook
def FacebookLogin(logfile):
    
    start_time=datetime.now()

    type(Key.HOME)
    
    if not exists(_PF_logo):
        load_browser_with_url(_PF_link)
        wait_find(_PF_logo)
    write_log(logfile, "total time detecting browser is: " + str(datetime.now()-start_time))  
            
    logged = _config.get('Facebook_Login', "logged")
    loginbutton = _config.get('Facebook_Login', "loginbutton")
    fb_logged_in_icon=_config.get('Facebook_Login', "fb_logged_in_icon")

    #if in Facebook section, and login button is not there, then it's logged in.
    if  verify_continue(logfile,fb_logged_in_icon)==1:
        write_log(logfile, "Facebook is already logged in!")
        mouseMove(Location(200,10))
        return
    #if login button shown in facebook section, then login to facebook section
    fb_logo = _config.get('Facebook_Login', "FB_logo")
    cert_warning = _config.get('Facebook_Login', "cert_warning")
    proceed = _config.get('Facebook_Login', "proceed")
    verify(logfile,loginbutton)
    click(Pattern(loginbutton).similar(0.90))
    sleep(2)
    ok_button=("1388298867679.png")
    
    if exists(ok_button):
        click(ok_button) 
        wait_click(ok_button)
        
    wait_find(fb_logo)
    if exists(Pattern("1387572170616.png").similar(0.95)) or exists(Pattern("1388377018768.png").similar(0.95)):
        type(_email)
        sleep(1)
        type(Key.TAB)
    type(_password)
    sleep(1)
    type(Key.ENTER)
    sleep(5)
    if exists(ok_button):
        click(ok_button) 
        wait_click(ok_button)
    
    
    verify(logfile,fb_logged_in_icon)
    write_log(logfile, "Logged into Facebook successfully!")
 
    if exists(cert_warning):
        click(proceed)        
    write_log(logfile, "Total Facebook login time is: " + str(datetime.now()-start_time))  
                
def LinkedInLogIn(logfile):

    start_time=datetime.now()                            
    type(Key.HOME)    
    if not exists(_PF_logo):
        load_browser_with_url(_PF_link)
        wait_find(_PF_logo)
        
    write_log(logfile, "total time detecting browser is: " + str(datetime.now()-start_time))  
            
    logged_in_linkedIn = _config.get('LinkedIn_check', 'logged_in_linkedIn')
    loginbutton = _config.get('LinkedIn_check', 'screen1')
    linkedin_section_img=_config.get('LinkedIn_check', 'linkedin_section_img')
    linkedIn_profile=_config.get('LinkedIn_check', 'linkedIn_profile')  
    
    #look for LinkedIn section image to locate LinkedIn section
    locate_linkedIn_section(logfile)
    
    #if profile image exists, it means linkedin is logged in already
    if exists(linkedIn_profile):
        write_log_with_screenshot(logfile, "Already logged in LinkedIn!")  
        mouseMove(Location(200,10))
        return
        
    verify(logfile, loginbutton) 
    click (Pattern(loginbutton).similar(0.70).targetOffset(223,4))
    sleep(5)
    if exists("1387572272054.png"):
        type(_email)
        sleep(1)
        type(Key.TAB)
    type(_password)
    type(Key.ENTER)
    sleep(3)

    verify(logfile,logged_in_linkedIn)
    write_log(logfile, "logged into LinkedIn successfully")
    write_log(logfile, "Total LinkedIn login time is: " + str(datetime.now()-start_time))  
    #close the logged in tab, suppose to close by itself. it's a bug right now, if fixed in the future, please delete this line
    type('w', Key.CTRL)
    locate_linkedIn_section(logfile)
    mouseMove(Location(200,10))
    
     
def write_log(logfile,msg):
    #fo=open(logfile, "a")
    with open(logfile, 'a+') as fo:
        fo.write("\n<p> " + str(datetime.now())+ ":   " + msg + " </p>\n")

    
def write_log_with_screenshot(logfile,msg):
    write_log(logfile,msg)
    scr_shot=capture(0,0,1400,900)
    write_screenshot_log(logfile,scr_shot)

def write_img_log(logfile, img):
#    fo=open(logfile, "a")
    with open(logfile, 'a+') as fo:
        print "img path: " +img
    #if the img is from common, do not use split
    #if img is under xxx.sikuli, it only has the file name, doesn't have path, need to add the test case folder path to it.
    #if img is from PF_common, it comes a full path, no need to use split.
        if "common.sikuli" in img and not "\\" in img:
            img="C:\\Automation_PF\\PF_common\\" + img
        if not "\\" in img:
            img_path,img_name=os.path.split(logfile)
            img_path,img_name=os.path.split(img_path)      
            msg='\n<img border=\"0" src="' + img_path+"\\"+ img + '"></img>\n'
        else:msg='\n<img border=\"0" src="' + img + '"></img>\n'
        print "log image: ", msg
        fo.write(msg)


def write_screenshot_log(logfile, img):
#    fo=open(logfile, "a+")
    with open(logfile, 'a+') as fo:
        print "Image path is: " + img        
        img_path,img_name=os.path.split(logfile)
        cmd = "copy %s %s" % (img, img_path)
        os.system(cmd)
        path1,img_name=os.path.split(str(img))

        img= img_path +"\\"+ img_name
        print "Image path after copy is: " + img        
        msg = '<p>Screen shot during test is <a href=file:///' + img + '>here</a></p>'
        print "Screenshot msg in screenshot log    is:     " + msg
        fo.write(msg)
        #write_log(logfile, "message of the link is: " + msg\n")
        #msg='\n<img border=\"0" src="' + img + '" width="1200" height="800"></img>\n'

def cleanTestScript(testScript):
    if ".py.sikuli" in testScript:
        testScript = testScript.replace(".py.sikuli", ".sikuli")
    return testScript


def create_log_folder(testScript,testCase):
    log_path=_rootDir + cleanTestScript(testScript)+ "\\log\\"
    log_file= log_path +str(testCase)+ "-log.html"
    print log_path 
    cmd = "mkdir %s" % (log_path)
    print "log path created:  " + log_path
    os.system(cmd)
    return log_file
            
def wait_find(y): 
    i=0
    while (not exists(y)and i<5):
        sleep(2)
        i+=1
    if exists(y):
        return 1
    else: return 0   

def wait_click(y): 
    i=0
    while (i<5):
        sleep(2)
        i+=1
    if exists(y):
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

def verify(logfile,image):
    x = wait_find(Pattern(image).similar(0.80))
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

def load_browser_with_url(link):
    if not exists(_ch1) and not exists(_ch2): 
        App.open(_chrome_app)
        wait_find(_ch2)
        mouseMove(Location(200,10))
    switchApp("Google Chrome")
    sleep(2)
    type('l', KEY_CTRL)
    type(link+"\n")
    sleep(5)
    mouseMove(Location(200,10))

def load_browser_with_url_firefox(link):
    App.open("C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
    type('D', Key.ALT)
    type(link+"\n")
    sleep(5)
    mouseMove(Location(200,10))
    
def locate_item_line_by_line(logfile,img):
    i=0
    k=0
    while (not exists(img) and i<9):
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        mouseMove(Location(200,10))
        i+=1
    if exists(img):
        write_log(logfile, "Locate image in locate_item_line_by_line, image found: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        k=1
    else:
        write_log(logfile, "Locate image in locate_item_line_by_line, not able to find image: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        raise Exception("Locate_item_line_by_line Exception: Not able to locate image: " + img)
    
def locate_item_page_by_page(logfile,img):
    i=0
    while (not exists(img) and i<4):
        type(Key.PAGE_DOWN)
        mouseMove(Location(200,10))        
        i+=1
        sleep(3)
    if exists(img):
        write_log(logfile, "Locate image in locate_item_line_by_line, image found: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        k=1
    else:
        write_log(logfile, "Locate image in locate_item_line_by_line, not able to find image: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")



def get_img_value(image,text):
    wait_click("1388032151500.png")
    
    type(Key.F12)
    wait_click("1388032189908.png")
    
    type("f", Key.CTRL)
    sleep(3)
    type(text)
    sleep(3)
    type(Key.ENTER)
    
    if exists(image):
        click(image)
        type("c", KEY_CTRL)
        print "CTRL_C pressed!"
        sleep(2)
        #App.open("%windir%\system32\notepad.exe")
        sleep(3)
        type("v", Key.CTRL)
        data=Env.getClipboard()
        print "txt: " + str(data)
        value1=(data.split('>')[1]).split('<')[0]
        value1=int(value1.replace('%',''))
        type(Key.F12)        
        print value1
        return value1

    else : print "fail"

def get_protection_value(logfile):
    
    search_txt1="search_txt1_img.png"
    
    #search_txt2="1386700206064-1.png"

    #search_txt1= "1387454285798.png"
    
    switchApp("Google Chrome")
    #search_str2="num_private_settings\n"
    search_str1="fb_protection_percent\n"
    print "search img: " +str(search_txt1)
    percent_value = get_img_value(search_txt1, search_str1)
    #list2 = get_img_value(search_txt2,search_str2)
    #print percent_value
    write_log(logfile,"Protection value is:" + str(percent_value))
    screen_shot=capture(0,0,1440,900)
    write_screenshot_log(logfile,screen_shot)
    return percent_value
    

def testScriptPaths():
     print "_rootDir= ", _rootDir, "\n_thisScript= ", _thisScript, "\n_commonDashDir= ", _commonDashDir, "\n_config_file= ", _config_file
     print _config.get('Delete_history', 'screen1')


def PassCase(log_file, test_case_id):
    type("l", KEY_CTRL)
    type(_passed_link +"\n")
    sleep(5)
    msg=str(test_case_id) +' Test Case Passed!'
    write_log (log_file,msg)
    msg="Tested URL:" + _PF_link
    write_log(log_file,msg)

def FailTestCase(logfile, test_case_id):
    type("l", KEY_CTRL)
    type(_failed_link)    
    type(Key.ENTER)
    write_log (logfile, test_case_id + ' Test Case failed!')
    msg="Tested URL:" + _PF_link
    write_log(logfile,msg)

def get_img_value_firefox(image):
    sleep(6)
    type(Key.F12)
    #sleep(6)
    wait_click("1388481656140.png")
    wait_click("1388481667291.png")
    wait_click("1388481681375.png")
    sleep(3)
       
    if exists(image):
        click(image)
        sleep(2)
        type(Key.RIGHT)
        type(Key.DOWN)
        type(Key.ENTER)
        type("c", KEY_CTRL)
        print "CTRL_C pressed!"
        sleep(2)
        #App.open("%windir%\system32\notepad.exe")
        sleep(3)
        type("v", Key.CTRL)
        data=Env.getClipboard()
        print "txt: " + str(data)
        value1=int(data.replace('%',''))
        type(Key.F12)        
        print value1
        return value1

    else : print "fail"

def get_protection_value_firefox(logfile):
    
    search_txt1="1388482910074.png"
       
    switchApp("Firefox")
    #search_str2="num_private_settings\n"
    #search_str1="fb_protection_percent\n"
    print "search img: " +str(search_txt1)
    percent_value = get_img_value_firefox(search_txt1)
    #list2 = get_img_value(search_txt2,search_str2)
    #print percent_value
    write_log(logfile,"Protection value is:" + str(percent_value))
    screen_shot=capture(0,0,1350,850)
    write_screenshot_log(logfile,screen_shot)
    return percent_value     

if __name__ == "__main__":
    # This runs when executing PF_common directly, it will NOT run when importing.
    # if indented (under the if statement, if not indented it will always run.)
    testScriptPaths()
	#protection_values()    
	#lst=protection_values()        
	#print lst[0]
	#print lst[1]  
    #RemoveExt("C:\Automation_PF\log.html")
	#InstallExtension("C:\Automation_PF\log.html")



	#print "say hi from PF_common"
	#load_browser_with_url("google.com")
    #logfile="C:\\Automation\\log.html"
	#write_img_log(logfile, img)
	#ClearBrowsingData()
   # RemoveExt(logfile)
    #InstallExtension(logfile)
#    write_log_with_screenshot(logfile,"hi, just a test")
    #scr=capture(0,0,1400,900)
    #write_screenshot_log(logfile,scr)

    #FacebookLogin(logfile)
    #LinkedInLogIn(logfile)
    #GoogleLogin(logfile)
	#locate_google_section(logfile)
	#locate_websites_section(logfile)
	#locate_linkedIn_section(logfile)
    #get_protection_value(logfile)
    
    #start_time=datetime.now()
#    logfile="C:\\Automation\\log.html" 
    #locate_google_section(logfile)
 #   locate_tracking_section(logfile)
 #   locate_websites_section(logfile)
    #sleep(3)
    #print "Total time for installation is: " + str(datetime.now()-start_time)