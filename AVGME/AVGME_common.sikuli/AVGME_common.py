
#09.07-Fixed logging  functions. Created LoginTOApp and InstallExtention, UninstallExtention,AppOpen. AddNewAccount finished but will test later.
#23.06- Michael -  checkImage, readelement - read link from txt file and verify in avg elements are present on page 
#23.06- David - two new functions LoginTOApp() and set_hotkey()- 


from __future__ import with_statement
import ConfigParser
import logging
import shutil
from sikuli import *
import os, re
from datetime import datetime
import time
from random import randint
#This is the common script for Chrome
_scriptName = "AVGME_common.sikuli"

_saveLogToRW = False
_useAutoUser = False

_log_root = "C:\\Logs\\"

if len(sys.argv) > 1 and sys.argv[1] == "logrw":
    _useAutoUser = True
    _saveLogToRW = True

print "_saveLogToRW: ", _saveLogToRW

if len(sys.argv) > 1 and sys.argv[1] == "autoUser":
    _useAutoUser = True

print "_useAutoUser: ", _useAutoUser

#_email = _config.get('Test_account', 'email1') 
#_password = _config.get('Test_account', 'pass1') 
#_email="lyemele@gmail.com"
#_password="qawsed1234"

#if _useAutoUser:
    # when a Driver launches the TC's always use mzhang account.  
    #_email = "mzhang0170@gmail.com"
    #_password = "zhang0170"

_passed_link = "dl.dropboxusercontent.com/u/40284694/passed.png"
_failed_link ="dl.dropboxusercontent.com/u/40284694/failed.png"
_chrome_appx86="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
_chrome_app="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
_test_suite_log="C://test_suite_log.html"
_ch1=("1387227872882.png") 
_ch2=("1387230266787.png")
redicon=(Pattern("1404895789903.png").similar(0.91))
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



if os.path.isfile(_chrome_appx86):
    #check for x86 path (x64 bit) 
    _chrome_app = _chrome_appx86

_chrome_app = _chrome_app + " --start-maximized"

_config=ConfigParser.ConfigParser(_dirMap)
_config.read(_config_file)
#Clear chrome browser history Data finction. Clear a browser history through browsers hot keys
#last update 0304_2014 by Kathy
def ClearBrowsingData():
    reg1=Region(146,108,298,57)
    reg2=Region(472,217,493,479)

    time=_config.get('Delete_history', 'screen1')
    begin=_config.get('Delete_history', 'screen2')
    begin1=_config.get('Delete_history', 'screen3')    
    load_browser_with_url("chrome://history\n ")
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
    find("1391606325401.png").highlight(1) #--verify cleanup is successful
    sleep(2)
    type("q", Key.CTRL+Key.SHIFT)     
    load_browser_with_url("")

  
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
    #write_log(log_file,"The common last modified"+_last_modifed)      
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

            
def wait_find(y): 
    i=0
    while (not exists(y)and i<5):
        sleep(2)
        
        i+=1
    if exists(y):
        find(y)#.highlight(1)
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

    x = wait_find(Pattern(image).similar(0.80))
    screen_shot=capture(0,0,1440,900)
    if x==1: 
        write_log(logfile,"Following expected image was found")
        write_img_log(logfile,str(image))
        write_screenshot_log(logfile,screen_shot)

    else:
        write_log(logfile,"Not able to find following image")
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
        if exists("1395170923573-1.png"):click("1395170923573-1.png")          
        sleep(2)
    type('l', KEY_CTRL)
    type(link+"\n")
    sleep(2)
    wait_find("1403263925018.png")
    mouseMove(Location(1000,100))
  
def locate_item_line_by_line(logfile,img):
    i=0
    k=0
    while (not exists(img) and i<12):
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        mouseMove(Location(1000,100))
        i+=1
    if exists(img):
        find(img).highlight(1)
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
    while (not exists(img) and i<6):
        type(Key.PAGE_DOWN)
        mouseMove(Location(200,50))        
        sleep(3)
        i+=1
        
    if exists(img):
        find(img).highlight(1)
        write_log(logfile, "Locate image in locate_page_by_page, image found: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        k=1
    else:
        write_log(logfile, "Locate image in locate_page_by_page, not able to find image: " +img)
        write_img_log(logfile, img)
        write_log_with_screenshot(logfile,"See Screenshot:")
        raise Exception("Locate_item_page_by_page Exception: Not able to locate image: " + img)    

def testScriptPaths():
     print "_rootDir= ", _rootDir, "\n_thisScript= ", _thisScript, "\n_commonDashDir= ", _commonDashDir, "\n_config_file= ", _config_file
     print _config.get('Delete_history', 'screen1')


def PassCase(log_file, test_case_id):
    load_browser_with_url(_passed_link)
    msg=str(test_case_id) +' Test Case Passed!'
    write_log_with_screenshot(log_file,msg)
    write_log(_test_suite_log,msg)
    msg="Tested URL:" 
    write_log(log_file,msg)
    msg="Closing browser after test case finished...."
    write_log(log_file, msg)
    sleep(15)    

    #msg="browser closed"
    #write_log_with_screenshot(log_file, msg)    
    #close_browser(log_file)
    
def FailTestCase(logfile, test_case_id):
    load_browser_with_url(_failed_link)
    msg=test_case_id + ' Test Case failed!'
    write_log_with_screenshot(logfile, msg)
    write_log(_test_suite_log,msg)
    print "test suite log file is: " + _test_suite_log
    write_log(logfile,"Tested URL:" )


    sleep(2)

    test_script_name = str(logfile).split("\\")[3]
    print "test_script_name is:" + test_script_name
    
    msg = test_script_name + " - Test Case Failed!"
    write_log_with_screenshot(logfile, msg)
    write_log(_test_suite_log,msg)
    print "test suite log file is: " + _test_suite_log

    sleep(3)  
    timeStamp = str(time.strftime("%H%M%S"))
    Failed_Logs_Folder = _rootDir + "Failed_Logs\\" + test_script_name + "_" + timeStamp +"\\"
    src_folder=_rootDir+"Logs\\"+ test_script_name+"\\"
    print "src_folder is: " + src_folder
    print "Failed_Logs_Folder is:" + Failed_Logs_Folder
    try:
        shutil.copytree(src_folder, Failed_Logs_Folder) 
    except shutil.Error:
        print "shutil error occurred."
    #msg="browser closed"
    #write_log_with_screenshot(logfile, msg)
    #close_browser(logfile)

def close_browser(logfile):    
    verify(logfile,"1388806538311.png")
    click("1388806538311.png")
    verify(logfile,"1388806596083.png")
    click("1388806596083.png")
    write_log_with_screenshot(logfile, "The above test case is done, browser closed!")

#disable autofill for chrome browser
def disable_autofill(logfile):
    load_browser_with_url("chrome://settings/")
    search_field=("1397084129692.png")
    wait_find(search_field)
    click(search_field)
    type("Password")
    
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

def add_sites(p):
    sites=_thisScript+"\\"+"login_signup.txt"
    with open(sites, 'r') as f:
        site_list = [line.strip() for line in f]                    
    return site_list[p]


image="avgme-mapping"
def readelement(link,image,logfile): 
    load_browser_with_url(link)
    wait(10)
    type(Key.F12)
    sleep(2)
    type("f", KeyModifier.CTRL)
    sleep(2)
    type(image)
    sleep(2)
    #type(Key.ENTER)
    if exists ("1403508890042.png"):
        hover("1403508890042.png")
    wait(2)    
    username=("1403525464402.png")
    password=("1403525481129.png")
    if exists (username):
        msg=("element email from site " +" ---------------was found")
        print (msg)
        write_log(logfile,msg)
        if exists(Pattern("1403508994132.png").similar(0.90)):
            msg=("image email from site " +  " ---------------was found")
            print (msg)
            write_log(logfile,msg)
    else:
        msg=("element email from site " + " ---------------was not found")
        print (msg)
        write_log(logfile,msg)
    type(Key.ENTER)
    if exists (password):
        msg=("element password from  site " +  " ---------------was found")
        print (msg)
        write_log(logfile,msg)
        if exists(Pattern("1403509007657.png").similar(0.90)):
            msg=("image password from  site " +  " ---------------was found")
            print (msg)
            write_log(logfile,msg)
    else:      
        msg=("element password from  site " + " ---------------was not found")
        print (msg)
        write_log(logfile,msg)


    sleep(2)
    type(Key.F12)


def fill_fields(logfile):
    Close=("1405584053375.png")
    Topbar=( "1405584104731.png")
    greenlock=("1405582009901.png")
    #greenlock1=("")
    count = 0
    wait(1)
    if not exists (greenlock):
        return 0
    
    lock=findAll(greenlock)
    for greenlock in lock:
        click(greenlock)
        wait(1)
        type("michael.scott.avg@gmail.com")
        wait(1)
        
        count += 1
    type(Key.ENTER)
    wait(2)
    if verify_continue(logfile,Topbar)==1:
        click(Close)
    
    return count

def verifyAccount(logfile):
    Accounts=("1405585354472.png")
    Item=("1405585496047.png")
    Address=("1405587024826.png")
    Username=("1405587244668.png")
    Remove=("1405587728444.png")
    Delete=("1405587762833.png")
    NoAccounts=("1405588247786.png")
    Trash=("1405343738103.png")

        
    data=""
    click(redicon)
    wait(3)
    if exists(Accounts):
        click(Accounts)
    if verify_continue(logfile,Item) ==1:
        click(Item)
        wait(2)
        click(Address)
        type("a", KeyModifier.CTRL)
        wait(1)
        type("c", KeyModifier.CTRL)
        wait(2)
        data=Env.getClipboard()
        write_log(logfile,"Stored Address was----------"+str(data))
        click(Username)
        wait(1)
        type("a", KeyModifier.CTRL)
        wait(1)
        type("c", KeyModifier.CTRL)
        wait(2)
        data1=Env.getClipboard()
        write_log(logfile,"Stored Username was----------"+str(data1))
        click(Remove)
        wait(1)
        click(Delete)
        
    elif verify_continue(logfile,Item) ==0:   
        write_log(logfile,"Site data wasnt stored")
    while exists(Item):
        hover(Item)    
        verify(logfile,Trash)
        click(Trash)
        verify(logfile,Delete)
        click(Delete)
        
        
    verify_continue(logfile,NoAccounts)    
    return data     
        
        
        
        
    

    

def checkImage(logfile):
    sites=_thisScript+"\\"+"login_signup.txt"
    with open(sites, 'r') as f:
        line = f.readline()
        while line:
            write_log(logfile,"-----------------------------------------------------------------------------------------------")
            readelement(line,image,logfile)
            write_log_with_screenshot(logfile,line)
            print line
            if fill_fields(logfile)>=1:
        
                verifyAccount(logfile)
            line = f.readline()
        f.closed

def set_hotkey():
    print("1")
    load_browser_with_url("chrome://extensions/")
    click("1403523893400.png")
    sleep(2)
    click("1403524300016.png")
    sleep(1)
    type("m", KEY_CTRL)  
    sleep(2)
    type(Key.ESC)
    close_browser(log_file)

def LoginTOApp(logfile):
    
    login=("1405340124887.png")
    password=("1405340138333.png")
    masterpassword=("1406545572859.png")
    
    loggedin=("1404910191023.png")
    
    #type("m", KEY_CTRL)
    print("LoginTOApp")
    load_browser_with_url("http://www.google.com/")
    sleep(6)
    click(redicon)
    sleep(6)
    
    if exists(loggedin):
        write_log(logfile,"You are alredy logged into AVG Me") 
        return
    if exists(login):
        click(login)
        sleep(2)
        type("michael.scott.avg@gmail.com")
    wait(2)    
    if exists(password):
        click(password)
        sleep(2)
        type("US!pf.avg")
        sleep(2)
        type(Key.ENTER)
    if exists(masterpassword):
        click(masterpassword)
        sleep(2)
        type("US!pf.avg")
        sleep(2)
        type(Key.ENTER)
    sleep(2)
    write_log_with_screenshot(logfile,"See Screenshot:")
    type(Key.ESC)
    write_log(logfile,"You are succesfully logged in") 



def InstallExtention(logfile):
        
        Free=("1404895678910.png")
        Add=("1404895706525.png")
        Options=(Pattern("1404895861227.png").similar(0.91))
        Server=( "1409301894446.png")
        Save=("1404896133634.png")
        AvgPass=("1404898394393.png")
        load_browser_with_url("")
        wait(2)
        if exists (redicon):
            write_log(logfile,"Extention was installed") 
            return
            
        load_browser_with_url("https://chrome.google.com/webstore/detail/avgme/ifbiffgejacbblpoellfaeijobciillc?authuser=0")
        wait(6)
        verify(logfile,Free)
        click(Free)
        wait(2)
        verify(logfile,Add)
        click(Add)
        wait(10)
        #verify(logfile,redicon)
        rightClick(redicon)        
        wait(2)
        #hover(Options)
        click(Options)
        wait(3)
        if exists (Server):
            click(Server)
            wait(2)
            type("a", KeyModifier.CTRL)
            wait(2)
            type(Key.DELETE)
            type("http://atltavgme01.cloud-int.avg.com")
            wait(2)
            click(Save)
        #verify(logfile,redicon)
        write_log(logfile,"Extention was installed successfully") 
        write_log_with_screenshot(logfile,"See Screenshot:")
            


def UninstallExtention(logfile):   
    load_browser_with_url("https://google.com//")
    wait(5)
    if not exists (redicon):     
        write_log(logfile,"Extention was uninstalled") 
        print("Extention was uninstalled") 
        return
    rightClick(redicon)  
    wait(2)
    click("1404912423421.png")
    wait(2)
    click("1404912455198.png")
    if not exists (redicon):   
        write_log(logfile,"Extention was installed successfully") 
        print("Extention was uninstalled successfully") 
        
def AppOpen(logfile):
    if not exists (redicon):     
        write_log(logfile,"Opening browser")      
        load_browser_with_url("https://google.com//")
    #verify(logfile,redicon)
    if not exists("1404898394393.png"):
        click(redicon)
        write_log(logfile,"Opening app")        
        
    
    
def AddNewAccount(logfile) :
    GmailAcc=("1405341461409.png")
    AddNew=("1404913650255.png")
    Name=("1405685022627.png")
    Address=("1404913768988.png")
    Username=("1404913804945.png")
    Passowrd=("1405338004216.png")
    SaveChanges=("1404914048588.png")
    Stored=( "1406207698374.png")
    Advanced=("1405341526448.png")
    Speed=("1405341545558.png")
    AppOpen(logfile)
    #verify(logfile,redicon)
    click(redicon)
    wait(4)
    if exists (GmailAcc):
        write_log(logfile,"Google account was already created")
        return
    verify(logfile,AddNew)
    click(AddNew)
    wait(3)
    click(Name)
    type("gmail")
    wait(3)
    click(Address)
    type("https://accounts.google.com")
    wait(3)
    click(Username)
    type("michael.scott.avg")
    wait(3)
    click(Passowrd)
    type("US!pf.avg")
    wait(3)

   # verify(logfile,Advanced)
  #  click(Advanced)
  #  verify(logfile,SaveChanges)
    click(SaveChanges)    
    wait(3)
    #verify(logfile,Speed)
   # click(Speed)
    verify(logfile,Stored)
    write_log(logfile,"Accout was created")
    
  
def delItem(log_file):   
    Item=("1409316568129.png")
    Trash=("1405343738103-1.png")
    Delete=("1405587762833-1.png")
    click(redicon)
    wait(1)
    while exists(Item):
        #verify(log_file,Item)
        hover(Item)    
        verify(log_file,Trash)
        click(Trash)
        verify(log_file,Delete)
        click(Delete)
        wait(3)    

def LogOut(logfile):
    
    Logout=("1406026564033.png")
    Welcome=("1406026672231.png")
    
    AppOpen(logfile)
    if exists(Logout):
        click(Logout)
    verify(logfile,Welcome)    
        
    
  
    
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=create_log_folder(test_case_script_name, test_case_id)

        delItem(log_file)


    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        write_log(log_file,msg)        
        FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        print "exception"
        write_log(log_file,msg)        
        FailTestCase(log_file, test_case_id)    
    
    