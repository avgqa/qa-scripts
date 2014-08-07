#Helper functions for the PF iOS platform
#from sikuli.Sikuli import *
from __future__ import with_statement
# import settings
import shutil
from pawt import swing
#from java import net
from javax.swing import JButton, JFrame
#integrate the sikuli global namespace to this namespace
from sikuli import *

import os
from os.path import expanduser
import ConfigParser

reload(os)
import sys
reload(sys)
from datetime import datetime

Android ="/Users/sturman/Downloads/adt-bundle-mac-x86_64-20130917/sdk/tools/emulator64-x86"

_passed_link = "dl.dropboxusercontent.com/u/40284694/passed.png"
_failed_link ="dl.dropboxusercontent.com/u/40284694/failed.png"
_safari_app="~/Applications/Safari"
#_chrome_app="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

_PF_logo="pf_logo.png"

_rootDir = os.path.dirname(sys.argv[0])
#print "_rootDir is: " + _rootDir

if ".sikuli" in os.path.basename(_rootDir):
    # Running in command line returns the path including the sikuli script, different from IDE
    _rootDir = os.path.dirname(_rootDir)
_rootDir = _rootDir + "/"


_thisScript = _rootDir + "PF_Android_common.sikuli"

#_commonDashDir = _thisScript + "\\config_dash\\"
#_dirMap = {"dir":_commonDashDir}
#_config_file= _commonDashDir + "config.txt" 
_test_suite_log=_rootDir + "/test_suite_log.html"

_email="michael.scott.avg@gmail.com"    
_password="US!pf.avg"

def clearCookiesOnPF(logfile, sleepTime = 3, pf_gear = None, findGear = True, pln=None):
   # Clear Cookies helper function for PF iOS Platform 
    switchApp(Android)
    

    try: 

        if findGear:
            if pf_gear is None:
                pf_gear = find("gear.png")
            pf_gear.highlight(1)
            click(pf_gear)
            sleep(sleepTime)
        
        if pln:
            pln("1393574851071.png")
        pf_reset = wait("1393574889246.png")
        
        
        hover(Pattern("reset$log.png").targetOffset(-87,1))

        mouseDown(Button.LEFT)
        wait(12)
        mouseUp(Button.LEFT)
        doubleClick(pf_reset)
        wait(5)
    except:
        e,b,c = sys.exc_info()
        if pln:
            pln("Cookies not cleared due to error:")  
            pln("%s %s %s" % (e,b,c))
        else:
            print "Cookies not cleared due to error:"  
            print e,b,c       
        pass
    apps=("1393494311633.png")
    pFApp=("1393494366550.png")
    verify(logfile,apps)   
    click(apps)
    sleep(7)
    pf=("1393494526477.png")
    pf_region = find(pf)
    center = pf_region.getCenter()
    Settings.DelayAfterDrag = 0.06
    Settings.DelayBeforeDrop = 0.06    
    Settings.MoveMouseDelay = -1
    dragDrop(center,center.left(300))
    AppOpen (logfile)
    Tutorial(logfile)



def dragAndDrop (AfterDrag= -1,BeforeDrop = -1):
    
    
    sim = switchApp(Android)
    sim_region = sim.focusedWindow()
    center = sim_region.getCenter()
    sleep(2)


    Settings.DelayAfterDrag = AfterDrag
    Settings.DelayBeforeDrop = BeforeDrop
    Settings.MoveMouseDelay = -1
    dragDrop(center.right(50),center.left(250))
  

def locateItem (logfile,item):
    k=0 
    while (not exists (Pattern(item).similar(0.90)) and k<8) : 
        sim = switchApp(Android)   
        sleep(1)        
        k+=1  
        sim_region = sim.focusedWindow()
        center = sim_region.getCenter()
        Settings.DelayAfterDrag = 0.05
        Settings.DelayBeforeDrop = 0.05      
        Settings.MoveMouseDelay = -1
        dragDrop(center.below(50), center.above(50))   
    verify(logfile,item)    

def locateItemWebPage (logfile,item):
    k=0 
    while (not exists (item) and k<10) : 
        sim = switchApp(Android)   
        sleep(1)        
        k+=1  
        sim_region = sim.focusedWindow()
        center = sim_region.getCenter()
        Settings.DelayAfterDrag = 0.05
        Settings.DelayBeforeDrop = 0.05      
        Settings.MoveMouseDelay = -1
        dragDrop(center.below(100), center.above(50))   
    verify(logfile,item)         
        
def LocateOnTop (logfile,item):
    k=0
    if exists(item):return
    while (not exists (item) and k <6):   
        sim = switchApp(Android)
        k+=1           
        sim_region = sim.focusedWindow()
        center = sim_region.getCenter()
        Settings.DelayAfterDrag = 0.05
        Settings.DelayBeforeDrop = 0.05
        Settings.MoveMouseDelay = -1
        dragDrop(center.above(150), center.below(150))   
    verify(logfile,item) 

def verify(logfile,image):
    x = wait_find(Pattern(image).similar(0.90))
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

def verify_continue(logfile,image,similarity):
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
  

def create_log_folder(test_case_script_name, testCase):
    #automationRootPath = expanduser("~/Documents/qa-automation/Privacy-Fix/Mobile App/iOS/Demo/")
    log_path=_rootDir  + test_case_script_name + "/log"
    log_file= log_path +"/" +str(testCase)+ "-log.html"  
    print "log path created:  " + log_path
    
    if os.path.exists(log_path):
        print "log folder exists, will delete this folder!" 
        try:
            shutil.rmtree(log_path)
            print "Log folder is deleted!"
        except:
            print "log folder is not deleted, will append to the previous log file!"  
            
    try:
        os.mkdir(log_path)
    except:
        pass # fail silently if remote directory already exists    
         
    return log_file    

def write_log(logfile,msg):
    #fo=open(logfile, 'a+')
    with open(logfile, 'a+') as fo:
        fo.write("\n<p> " + str(datetime.now())+ ":   " + msg + " </p>\n")

def wait_find(y): 
    i=0
    while (not exists(y)and i<2):
        sleep(2)
        i+=1
    if exists(y):
        find(y).highlight(1)
        return 1
    else: return 0       


def write_img_log(logfile,img):
    with open(logfile, 'a+') as fo:

        try:

            img_path=_thisScript+"/"+img

            if os.path.exists(img_path):#for image in PF_common
                img1 = "../../PF_iOS_common.sikuli/" + img 
                msg = "img" + img + " is under common"

                msg='\n<img border=\"0" src="' + img1+ '"></img>\n'  
                fo.write(msg)

            else:  #for images in test_id.sikuli
                img1="../" + img
                
                msg='\n<img border=\"0" src="' + img1+ '"></img>\n'  
                fo.write(msg)           

        except:
            msg="in exception: There is an except when write img log!"
            print msg
            fo.write(msg)
        
def write_screenshot_log(logfile, img):
    #fo=open(logfile, "a+")
    with open(logfile, 'a+') as fo:
        img_path,img_name=os.path.split(logfile)
        shutil.copy (img, img_path) 
        path1,img_name=os.path.split(str(img))
        img= img_path +"/"+ img_name     
        img = img.replace(" ", "%20")    
        msg = '<p>Screen shot during test is <a href=file:///' + img + '>here</a></p>'    
   
        fo.write(msg)
   
    
def write_log_with_screenshot(logfile,msg):
    write_log(logfile,msg)
    scr_shot=capture(0,0,1680,1050)
    write_screenshot_log(logfile,scr_shot)

def FB_logIn(log_file):
    
    switchApp(Android)
    
    
    connectToFacebook = ("fBLogin.png")
    fbConnectTopbar = ("fBTopbar.png")
    email_field = ("fBEmail.png") 
    password_field = ("fBPassword.png")
    logInButton = ("fBLoginConfirm.png")
    fixesButton = ("fixes.png")
    wait (1)  

    if not exists (connectToFacebook):
        
        msg="You are already connected to Facebook"
        print msg
        write_log_with_screenshot(log_file,msg)
        return
        
        #sleep (13)
    else:
        verify (log_file,connectToFacebook)       
        
        click (connectToFacebook)
        sleep(5)
        while exists("1393509657639.png"):
            sleep(5)
        verify (log_file,email_field)     
        click (email_field)
        sleep (5)
        type (_email)
        verify (log_file,password_field)     
        type(Key.TAB)
        #click (password_field)
        sleep (3)
        type (_password)
        sleep (3)
        click (logInButton)
        
        sleep(5)
       


def Google_logIn(logfile):
    
    Google_section_img=("google_img.png")
    More_sectioni_img=("more_img.png")
    
    
    
    
    connectToGoogle = ("connectToGoogle.png")
    googleConnectTopbar = ("googleConnectTopbar.png")
    email_field = ("googleEmail.png") 
    password_field = ("googlePassword.png")
    logInButton = ("googleSingin.png")
    fixesButton = ("googleFixes.png")
    switchApp(Android)
  
    locateItem(logfile,Google_section_img)  
    locateItem(logfile,More_sectioni_img)
    
    if exists (connectToGoogle):
        click (connectToGoogle)
        sleep (5)        
        click (email_field)
        sleep (5)
        type (_email)
        sleep(2)
        type(Key.TAB)
        #click (password_field)
        sleep (3)
        type (_password)
        sleep (3)
        click (logInButton)
        
        sleep(10)
        
    else:
        msg="You are already logged in to Google"
        write_log_with_screenshot(logfile,msg)
        print msg

def Tutorial(log_file):
    sim = switchApp(Android)
    if exists("tutorialGear.png") :
        msg ="Tutorial was already skipped"
        print (msg)
        write_log(log_file,msg)
        return
        
       


    continue_text = ("countinue.png")

    
    t=verify_continue(log_file, continue_text, 0.90)
    
    if t==0:
        write_log_with_screenshot(log_file, "Tutorial was not shown!")
        print "Tutorial was not shown!"
    else:        
        write_log_with_screenshot(log_file, "Tutorial was shown!")
        doubleClick(continue_text)
        sleep(1)
    #Let us help you with your privacy settings
        dragAndDrop ()
        #sleep(1)
    #Understand your settings
    
        dragAndDrop ()
       # sleep(1)
    #See why they matter
        dragAndDrop ()
       # sleep(1)
        
    verify(log_file,_PF_logo)
    
    write_log_with_screenshot(log_file,"PrivacyFix App is opened")
    

def PassCase(logfile, test_case_id):
    msg=str(test_case_id) + "Test Case Passed!"
    print (msg + 'Test Case Passed!')
    os.system("open -a Safari http://dl.dropboxusercontent.com/u/40284694/passed.png")    
    wait(10)
    os.system("/usr/bin/osascript -e \'tell application \"safari\" to quit\'")  
    #write_log(logfile,msg)
    write_log_with_screenshot(logfile,msg)
    write_log(_test_suite_log,msg)
    #PopUp('http://dl.dropboxusercontent.com/u/40284694/passed.png')   


    
def FailTestCase(logfile, test_case_id):
    
    msg=test_case_id + " Test Case failed!\n"
    #write_log(logfile,msg)
    os.system("open -a Safari http://dl.dropboxusercontent.com/u/40284694/failed.png")
    wait(10)
    os.system("/usr/bin/osascript -e \'tell application \"safari\" to quit\'")  
    
    write_log_with_screenshot(logfile, msg)
    write_log(_test_suite_log,msg)
    #print "test suite log file is: " + _test_suite_log


    
def AppOpen (log_file):

    
    if exists(_PF_logo):
        msg = 'App is already opened'
        write_log_with_screenshot(log_file,msg)
        

        print msg
        return
    App.focus (Android)

    PF= ( "pFLogo.png")
    menu=("menu.png")
    home=("1393496048670.png")
    if exists(home):
        click(home)
        wait(2)
    if exists(menu):
        click(menu)
        wait(2)
    if not exists (PF):
        print "need to slide to find PF_icon"
        sim = switchApp(Android)
        sim_region = sim.focusedWindow()
        sim_center = sim_region.getCenter()
        Settings.DelayAfterDrag = -1
        Settings.DelayBeforeDrop = -1
        Settings.MoveMouseDelay = -1
        dragDrop(sim_center.right(200), sim_center.left(200))
        verify(log_file,PF)
        print "slide and found PF_icon"
        click (PF)
        
    else:
        verify(log_file,PF)
        click (PF)
    Tutorial(log_file)        





#test_case_id="PF-1646"
#script_path, test_case_script_name=os.path.split(sys.argv[0])
#test_case_script_name=test_case_script_name + ".sikuli"
#log_file=create_log_folder(test_case_script_name,test_case_id)

#Tutorial(log_file)
#locateItem (log_file,"1392974802755.png")