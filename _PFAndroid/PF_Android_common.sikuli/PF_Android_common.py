#3/25/2014 -- David
# added check for loading settings to GL_login and FB_login and appOpen finctions
# added verify after login to Google
#3/25/2014 -- Kathy
#change iOS common folder to PF_Android_common in write_img_log function
#3/27/2014 -- added loop and verify tutorial images to sliding tutorial page in Tutorial function
#             added lines in FB login handle the black screen, changed wait time to 15 sec in FB login and Google login
#             line 75, changed pf_gear to image instead of a region(region is physical location, it stucked in an infinite loop in one test)
#4/04/2014 -- David added sleep after close browseer in pass and fail function
#4/4/2014 --  Kathy: added go to top of main page in AppOpen function to avoid google section icon not able to locate issue
#4/24/2014 -- Michael new logging function, Pass Fail save results to suite log
#8/07/2014 -- Michael Changed images and logic, added  zenLogin, twitterLogin functions

from __future__ import with_statement
# import settings
import shutil
from pawt import swing
#from java import net
from javax.swing import JButton, JFrame
#integrate the sikuli global namespace to this namespace
from sikuli import *

import ConfigParser
import logging
from sikuli import *
import os, re
from datetime import datetime
import os
from os.path import expanduser
import ConfigParser

reload(os)
import sys
reload(sys)
from datetime import datetime

#Android ='Nexus 4 - 4.2.2 - API 17 - 480x800'
Android ='Nexus S - 4.1.1 - API 16 - 480x800'
#Android ='Galaxy S2 - 4.1.1 - API 16 - 480x800'
sim = switchApp(Android)

_chrome_appx86="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
_chrome_app="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
_passed_link = "dl.dropboxusercontent.com/u/40284694/passed.png"
_failed_link ="dl.dropboxusercontent.com/u/40284694/failed.png"

_PF_logo=("1407394387605.png")



#_rootDir = os.path.dirname(sys.argv[0])
_rootDir = os.path.dirname(sys.argv[0].replace("/", "\\"))
print "sys.argv[0] in common is:" + sys.argv[0]
#print "_rootDir is: " + _rootDir

if ".sikuli" in os.path.basename(_rootDir):
    # Running in command line returns the path including the sikuli script, different from IDE
    _rootDir = os.path.dirname(_rootDir)
_rootDir = _rootDir + "\\"
print "_rootDir is:" + _rootDir

_thisScript = _rootDir + "PF_Android_common.sikuli"

#_commonDashDir = _thisScript + "\\config_dash\\"
#_dirMap = {"dir":_commonDashDir}
#_config_file= _commonDashDir + "config.txt" 
_test_suite_log=_rootDir + "\\test_suite_log.html"

_email="jonnylast2013@gmail.com"    
_password="US!pf.avg"

def clearCookiesOnPF(logfile, sleepTime = 3, pf_gear = None, findGear = True, pln=None):
   # Clear Cookies helper function for PF iOS Platform 
    switchApp(Android)
    

    try: 

        if findGear:
            if pf_gear is None:
                pf_gear = ("gear.png")
            find(pf_gear).highlight(1)
            click(pf_gear)
            sleep(sleepTime)
            write_log_with_screenshot(logfile, "after click on gear!")
            while exists("Black_Gear.png") or exists(Pattern("1395662626803.png").exact()):
                click("Back_buttton.png")
                sleep(2)
                write_log_with_screenshot(logfile, "after click on back button on the bottoe!")
                click(pf_gear)
                sleep(sleepTime)
        if pln:
            pln("reset1.png")
        pf_reset = wait("reset2.png")
        
        
        hover("Reset_hover.png")
        sleep(1)

        mouseDown(Button.LEFT)
        wait(12)
        mouseUp(Button.LEFT)
        doubleClick(pf_reset)
        wait(5)
        Tutorial(logfile)
    except:
        e,b,c = sys.exc_info()
        if pln:
            pln("Cookies not cleared due to error:")  
            pln("%s %s %s" % (e,b,c))
        else:
            print "Cookies not cleared due to error:"  
            print e,b,c       
        pass
    home=("home1.png")
    apps=("apps.png")
    pFApp=("PFAPP.png")
    verify(logfile,home)   
    click(home)
    verify(logfile,apps)   
    click(apps)
    sleep(2)
    hover(pFApp)
    mouseDown(Button.LEFT)
    wait(5)
    mouseUp(Button.LEFT)
    click("removeFromLis.png")
    sleep(2)
    verify(logfile,home)   
    click(home)
    AppOpen (logfile)
    Tutorial(logfile)



def dragAndDrop ():
    
    
    sim = switchApp(Android)
    sim_region = sim.focusedWindow()
    center = sim_region.getCenter()
    sleep(2)

    Settings.DelayAfterDrag =  -2
    Settings.DelayBeforeDrop =  -2
    Settings.MoveMouseDelay = -1
    dragDrop(center.right(150),center.left(250))
  

def locateItem (logfile,item):
    k=0 
    while (not exists (Pattern(item).similar(0.90)) and k<8) : 
        sim = switchApp(Android)   
        sleep(1)        
        k+=1  
        sim_region = sim.focusedWindow()
        center = sim_region.getCenter()
        wheel(center, WHEEL_DOWN, 2)
        #dragDrop(center.below(150), center.above(50))   
    verify(logfile,item)    

def locateItemWebPage (logfile,item):
    k=0 
    while (not exists (Pattern(item).similar(0.90)) and k<12) : 
        sim = switchApp(Android)   
        sleep(1)        
        k+=1  
        sim_region = sim.focusedWindow()
        center = sim_region.getCenter()
        wheel(center, WHEEL_DOWN, 5)
    verify(logfile,item)                
        
def LocateOnTop (logfile,item):
    k=0
    
    while (not exists (Pattern(item).similar(0.90)) and k<12):   
        sim = switchApp(Android)
        k+=1           
        sim_region = sim.focusedWindow()
        center = sim_region.getCenter()
        wheel(center, WHEEL_UP, 2)
    verify(logfile,item) 

def verify(logfile,image):
    x = wait_find(Pattern(image).similar(0.90),logfile)
    screen_shot=capture(0,0,1600,1200)
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
    x = wait_find(Pattern(image).similar(similarity),logfile)
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
    sute_path=_rootDir +"Logs\\"
    log_file= log_path +"\\" +str(testCase)+ "-log.html"  
    if not os.path.exists(sute_path):     
        try:
            print "before create logfile!"
            os.mkdir(sute_path)
            print "log path created:  " + sute_path

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
         
    return log_file   



def write_log(logfile,msg):
    #fo=open(logfile, 'a+')
    with open(logfile, 'a+') as fo:
        fo.write("\n<p> " + str(datetime.now())+ ":   " + msg + " </p>\n")

def checkLoading(logfile):
    wheeL=(Pattern("Wheel.png").similar(0.44))
    speed=(Pattern("1395842225470.png").similar(0.90))
    blackscreen=(Pattern("1395925615798.png").similar(0.90))
    k=0
    print "k is:" + str(k)
    while(not exists (speed) or exists(wheeL)):    
        print("Downloading in progress")
        App.focus(Android)
        test=App.focusedWindow()
        scr_shot=capture(test)
        write_log(logfile,"Downloading in progress")  
        write_screenshot_log(logfile,scr_shot)
        #write_img_log(logfile,y)
        sleep (4)
        k+=1
        if k>5:
            return 0  
            #break

def wait_find(y,logfile): 

    i=0
    msg="looking for image:" + str(y)
    print msg
    write_log(logfile,msg)
    
    checkLoading(logfile)
    while (not exists(y)and i<7):
        
        checkLoading(logfile)
        wait(2)
        i+=1    
        print("waiting for image")
        
    #while (not exists(y)and i<5):
     #   sleep(2)
    #    i+=1
    if exists(y):
        find(y).highlight(1)
        return 1
    else: return 0       


def write_img_log(logfile,img):
    print(str(img))
    with open(logfile, 'a+') as fo:
        try:                                           
                
            if '\\PF-' in logfile:
                script_name_old=str(logfile).split("\\PF-")[0]
            if '\\Logs' in script_name_old:
                script_name=str(script_name_old).replace("\\Logs", "")
            if '\\PF_Android' in script_name:
                common=str(script_name).split("\\PF_Android")[0]
                common=common +"\\PF_Android_common.sikuli\\"+ img     
            if os.path.exists(common):
                scr=common
                dst=script_name_old+"\\"+ img             
                shutil.copyfile(scr, dst)
                #open(dst,"w").write(open(scr,"r").read())
                msg='\n<img border=\"0" src="' +img+'"></img>\n'  
                fo.write(msg)           
                return
            if "common" in img:
                scr=img
                img_new=str(randint(10000,99999))+'.png'                 
                dst=script_name_old+"\\"+ img_new
                shutil.copyfile(scr, dst)
                #open(dst,"w").write(open(scr,"r").read())
                msg='\n<img border=\"0" src="'+img+ '"></img_new>\n'  
                fo.write(msg) 
                return
            scr=script_name +".sikuli\\"+ img
            dst=script_name_old+"\\"+ img
            shutil.copyfile(scr, dst)
            #open(dst,"w").write(open(scr,"r").read())
            msg='\n<img border=\"0" src="'+img+  '"></img>\n'  
            fo.write(msg)           
        except IOError, e:
            print "Unable to copy file. %s" % e

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
        msg = '<p>Screen shot during test is <a href=' + img_name + '>here</a></p>'    
   
        fo.write(msg)
   
    
def write_log_with_screenshot(logfile,msg):
    write_log(logfile,msg)
    scr_shot=capture(0,0,1680,1050)
    write_screenshot_log(logfile,scr_shot)

def FB_logIn(log_file):
    

    
    
    connectToFacebook = ("1407398302935.png")
    fbConnectTopbar = ("1407398438166.png")
    email_field = ("FBEmail.png") 
    password_field = ("FBPassword.png")
    logInButton = ("1407398455367.png")
    fixesButton = ("1407398118226.png")
    logged=("1407399202564.png")
 

    sim = switchApp(Android)
    sim_region = sim.focusedWindow()
    center = sim_region.getCenter()

    wait (5) 
    wheel(center, WHEEL_DOWN, 20)
    sleep(2)
    hover("1395926778937.png")
    if exists(connectToFacebook):
        verify (log_file,connectToFacebook)       
        click (connectToFacebook)
        sleep(10)
        blackAndWhiteScreen(connectToFacebook,log_file)
        verify (log_file,email_field)     
        click (email_field)
        sleep (5)
        type (_email)
        verify (log_file,password_field)     
        type(Key.TAB)
        sleep (3)
        type (_password)
        sleep (3)
        click (logInButton)
        sleep(30)     
        #while exists(wheeL):
         #   write_log_with_screenshot(log_file,"Wheel detected")
         #   sleep(5)
        verify (log_file,logged) 
        msg="You are connected to Facebook"
        print msg
        write_log_with_screenshot(log_file,msg)

    else:   
        msg="You are already connected to Facebook"
        print msg
        write_log_with_screenshot(log_file,msg)
        return
        
    

       


def Google_logIn(logfile):
    
    Google_section_img=("1407400454220.png")
    More_sectioni_img=("1407400461238.png")
    wheeL=(Pattern("Wheel.png").similar(0.40))
    
    reenter=("1395653717827.png")
    
    connectToGoogle = ("1407398094610.png")
 
    googleConnectTopbar = ("1407400521923.png")
    email_field = ("GLEMAIL.png") 
    password_field = ("GLPASSWORD.png")
    logInButton = ("GLSingIn.png")
    fixesButton = ("1407398108530.png")
    GoogleLogo=("gplus.png")
    switchApp(Android)
    sim = switchApp(Android)
    sim_region = sim.focusedWindow()
    center = sim_region.getCenter()

    wait(2)
    wheel(center, WHEEL_UP, 30)  
    locateItem(logfile,Google_section_img)  
    locateItem(logfile,More_sectioni_img)
    hover(_PF_logo)
    sleep(1)
    if exists (connectToGoogle):
        click (connectToGoogle)
        sleep (5) 
        if not exists(reenter):
            verify (logfile,email_field)     
            click (email_field)
            sleep (5)
            type (_email)
            sleep(2)         
        click(password_field)    
        sleep (3)
        type (_password)
        sleep (3)
        click (logInButton)  
        sleep(30)
        verify(logfile,GoogleLogo)
        #while exists(wheeL):
           # write_log_with_screenshot(logfile,"Wheel detected")
           # sleep(5)
        if (exists(GoogleLogo)):
            write_log_with_screenshot(logfile,"You are sucessfully logged into Google")
        
    else:
        msg="You are already logged in to Google"
        write_log_with_screenshot(logfile,msg)
        print msg

def Tutorial(log_file):

    if exists("gear2.png") :
        msg ="Tutorial was already skipped"
        print (msg)
        write_log(log_file,msg)
        return
    tutorial1=("welcome.png")

    
       


    continue_text = ("GetStarted.png")

    
    t=verify_continue(log_file, continue_text, 0.90)
    
    if t==0:
        write_log_with_screenshot(log_file, "Welcome page was not shown!")
        print "Tutorial was not shown!"
    else:        
        
        verify(log_file,tutorial1)        
        dragAndDrop()
        click(continue_text)  
        sleep(2) 
                   
        msg="Welcome page was shown" 
        print msg        


    verify(log_file,_PF_logo)
    
    write_log_with_screenshot(log_file,"PrivacyFix App is opened")
    

def PassCase(logfile, test_case_id):
    w=0
    try:
        if '.sikuli' and 'PF_Android_' in logfile:
            w=str(logfile).split(".sikuli")[0].split("PF_")[1]
        if '\\PF-' in w:
            w=w.split('\\PF-')[0]
    except   ValueError :
        print ("cant be converted into string")  
    except :
        print("Test case name is not correct, please change")         
    msg =   w + " - Test Case Passed!"
    print msg
    os.system("start chrome http://dl.dropboxusercontent.com/u/40284694/passed.png")
    write_log(logfile,msg)
    write_log_with_screenshot(logfile,msg)
    write_log(_test_suite_log,msg)
    #PopUp('http://dl.dropboxusercontent.com/u/40284694/passed.png')   
    sleep(15)    
    type("q", Key.CTRL+Key.SHIFT)   
    sleep(2)
    App.focus (Android)


    
def FailTestCase(logfile, test_case_id):    
    w=0
    os.system("start chrome http://dl.dropboxusercontent.com/u/40284694/failed.png")
    try:
        if '.sikuli' and 'PF_Android_' in logfile:
            w=str(logfile).split(".sikuli")[0].split("PF_")[1]
        if '\\PF-' in w:
            w=w.split('\\PF-')[0]
        test_script_name1 = str(logfile).split(".sikuli")[0].split(_rootDir)[1].replace("Logs\\","").split("\\PF-")[0]
        print(test_script_name1 )
    
    except   ValueError :
        print ("cant be converted into string")  
    except :
        print("Test case name is not correct, please change")

    msg =   w + " - Test Case Failed!"
    write_log(logfile,msg)
    write_log_with_screenshot(logfile, msg)
    write_log(_test_suite_log,msg)
    print msg
    sleep(15)    
    #print "test suite log file is: " + _test_suite_log
    type("q", Key.CTRL+Key.SHIFT)
    sleep(2)
    timeStamp = str(time.strftime("%H%M%S"))
    Failed_Logs_Folder = _rootDir + "Failed_Logs\\" + test_script_name1# + "_" + timeStamp +"/"
    print "Failed_Logs_Folder is:" + Failed_Logs_Folder 
            
    src_folder=_rootDir+"Logs\\"+ test_script_name1+"\\"
    print "src_folder is:" + src_folder
            
    print "src_folder is: " + src_folder
    print "Failed_Logs_Folder is:" + Failed_Logs_Folder+ "\\"
    if os.path.exists(Failed_Logs_Folder):
        print "log folder exists, will delete this folder!" 
        try:
            shutil.rmtree(Failed_Logs_Folder)
            print "Log folder is deleted!"
        except:
            print "log folder is not deleted, will append to the previous log file!"  
    wait(1)
    try:
        shutil.copytree(src_folder, Failed_Logs_Folder) 
    except shutil.Error, e:
        
        print "shutil error occurred."
        print e
    App.focus (Android)
    
def AppOpen (log_file):
    
    sim = switchApp(Android) 
    sim_region=sim.focusedWindow()
    center = sim_region.getCenter()
    fixes=("1407398108530.png")    
    back=("1395993486132.png")
    if exists (fixes):
        click (fixes)
    if exists (back):
        click (back)    
    wheeL=(Pattern("Wheel.png").similar(0.40))    
    if exists(_PF_logo):
        msg = 'App is already opened'
        write_log_with_screenshot(log_file,msg)
        print msg
        while not exists(Pattern("1396673216085.png").similar(0.91)):   
            print "not at the top"
            App.focus(Android)
            sleep(1)
            wheel(center, WHEEL_UP, 16)
            
        if exists(wheeL):sleep(5)
        return

    

    PF= ( "PFMenuLogo.png")
    menu=("menu.png")
    home=("home1.png")
    AVG=("1407394387605.png")
    verify(log_file,home)
    click(home)
    wait(3)
    verify(log_file,menu)
    click(menu)
    wait(3)
    
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
        sleep(2)
        
        
        #while exists(wheeL):
           # write_log_with_screenshot(log_file,"Wheel detected")
          #  sleep(5)
        
    else:
        verify(log_file,PF)
        click (PF)
        sleep(2)
       # while exists(wheeL):
          #  write_log_with_screenshot(log_file,"Wheel detected")
          #  sleep(5)
    sleep(2)    
    Tutorial(log_file) 
    verify(log_file,AVG)

def IfPass(log_file):
    reenter=("1395653717827.png")
    if exists(reenter):
        verify(log_file,reenter)
        click(reenter)
        sleep(1)
        type(Key.TAB)
        sleep(1)
        type(_password)
        type(Key.TAB)
        sleep(1)
        type(Key.ENTER)
        sleep(5)
        write_log_with_screenshot(log_file, "Password for Google entered")
    else: write_log_with_screenshot(log_file, "You are already logged to Google")

def blackAndWhiteScreen(item,log_file):
    i=0
    sleep(1)
    while (exists(Pattern("Black_Gear.png").similar(0.90)) or exists(Pattern("1395662626803.png").exact())and i<10):
        click("Back_buttton.png")
        sleep(2)
        msg=("going back")
        write_log(log_file,msg)
        print(msg)
        i+=1
        click (item)
     
    
    if (exists(Pattern("Black_Gear.png").similar(0.90)) or exists(Pattern("1395662626803.png").exact())):
        
            

        click("1395997193551.png")
        click("1395997214636.png")
        click("1395997240033.png")
        click("1395997253361.png")
        click("1395997272315.png")
        click("1395997282619.png")
        click("1395997297258.png")
        AppOpen (log_file)
        verify(log_file,item)
        click(item)
          
            
def Twitter_logIn(logfile):
    
    Facebook_section_img=("FBLogo.png")
    Twitter_section_img=("TWLogo.png")
    wheeL=(Pattern("Wheel.png").similar(0.40))
    
    reenter=("1395653717827.png")
    
    connectToTwitter = ("ConnectToTwitter.png")
 
    TwitterConnectTopbar = ("1407411197759.png")
    email_field = ("1407401447007.png") 
    password_field = ("1407401452700.png")
    logInButton = ("1407401458908.png")
    fixesButton = ("1407398108530.png")
    TwitterLogo=("1407403032469.png")
    switchApp(Android)
    sim = switchApp(Android)
    sim_region = sim.focusedWindow()
    center = sim_region.getCenter()

    wait(2)
    wheel(center, WHEEL_UP, 30)  
    locateItem(logfile,Twitter_section_img)  
    locateItem(logfile,Facebook_section_img)
    hover(_PF_logo)
    sleep(1)
    if (exists (connectToTwitter)and not exists(TwitterLogo)):
        click (connectToTwitter)
        sleep (5) 
        if not exists(reenter):
            verify (logfile,email_field)     
            click (email_field)
            sleep (5)
            type (_email)
            sleep(2)         
        click(password_field)    
        sleep (3)
        type (_password)
        sleep (3)
        click (logInButton)  
        sleep(30)
        verify(logfile,TwitterLogo)
        #while exists(wheeL):
           # write_log_with_screenshot(logfile,"Wheel detected")
           # sleep(5)
        if (exists(TwitterLogo)):
            write_log_with_screenshot(logfile,"You are sucessfully logged into Twitter")
        
    else:
        msg="You are already logged in to Twitter"
        write_log_with_screenshot(logfile,msg)
        print msg    
    
    
    
    
    
def zenLogin(logfile):
    Zen=("1407413479946.png")
    ZenUI=("1407413519949.png")
    ZenLogin=("1407413549908.png")
    LogInTab=("1407413685874.png")
    Email=("1407413706129.png")
    Password=("1407413718527.png")
    LogInButton=("1407414094429.png")
    

    verify(logfile,Zen)
    click(Zen)
    verify(logfile,ZenUI)
    verify(logfile,ZenLogin)
    click(ZenLogin)
    if exists(LogInTab):
        click(LogInTab)
    verify(logfile,Email)
    click(Email)
    type(_email)
    verify(logfile,Password)
    click(Password)
    type(_password)
    verify(logfile,LogInButton)
    click(LogInButton)
    
    

test_case_id="PF-1646"
script_path, test_case_script_name=os.path.split(sys.argv[0])
test_case_script_name=test_case_script_name + ".sikuli"
log_file=create_log_folder(test_case_script_name,test_case_id)
zenLogin(log_file)
#logfile="C:\\log111.html"
#AppOpen (logfile)
#clearCookiesOnPF(logfile)
#Tutorial(logfile)
#FB_logIn(logfile)
