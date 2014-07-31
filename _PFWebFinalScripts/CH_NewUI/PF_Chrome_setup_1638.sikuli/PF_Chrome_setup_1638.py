# Last changes:
# - Linked in section has been updated
# - we have added reset for Google section
#05/02/2014 -- Kathy: change script id to PF-1638, and added 1638 to the script name.
#06/25/2014-- Michael: changed images and added new logic. 
#Can't verify correctly because currently on production item status doesn't change after fixing it and some remain the same


import PF_common
reload(PF_common)


#setup link doesn't work consistant, not going to use it.
#setup_link="http://addons.privacyfix.com/pf/seenclear?uid=1e8e0c7992c57417cc4a6af0d3908f2e"
PF_link=PF_common._PF_link
browser_type="Chrome"
test_case_id="PF_1638"

fix_icon=("fixes.png")


FB01_green=("fb1.png")


def set_FB01_grey(log_file):
        click(FB01_green)
        sleep(5)
        PF_common.verify(log_file,"1396333260662.png")
        click(Pattern("1396333268916.png").similar(0.91))
        sleep(4)
        click(fix_icon)
        
        sleep(5)
        mouseMove(Location(1000,100)) 
        PF_common.verify(log_file,"fb1grery.png")
        PF_common.write_log_with_screenshot(log_file, "FB01 is set to grey!")                

FB02_green=("1404473650618.png")
def set_FB02_grey(log_file):
    click(FB02_green)
    sleep(5)
    PF_common.verify(log_file,"1404473746361.png")
    click("1404473764442.png")
    sleep(2)
    click("1404473808957.png")
    sleep(3)
    click(fix_icon) 
    sleep(5)
    mouseMove(Location(1000,100)) 
    PF_common.verify(log_file,"1404473847855.png")
    PF_common.write_log_with_screenshot(log_file, "FB02 is set to grey!")   
    
FB04_green=("fb2green.png")
def set_FB04_grey(log_file):
    click(FB04_green)
    sleep(5)
    PF_common.verify(log_file,"1396333369062.png")
    click("1396333360141.png")
    sleep(2)
    click("1396333407392.png")
    sleep(3)
    click(fix_icon) 
    sleep(5)
    mouseMove(Location(1000,100)) 
    PF_common.verify(log_file,"fb2grey.png")
            
    PF_common.write_log_with_screenshot(log_file, "FB04 is set to grey!")    
    
    

FB06_green=("fb6green.png")

def set_FB06_grey(log_file):
    click(FB06_green)
    sleep(5)
    PF_common.wait_click("1390020887226.png") 
    sleep(2)
    click("1396333454235.png")
    sleep(3)
            
    click(fix_icon)
    sleep(5)
    mouseMove(Location(1000,100))    
    PF_common.verify(log_file,"fb6grey.png")
            
    PF_common.write_log_with_screenshot(log_file, "FB06 is set to grey!")
    

    
FB07_green=("fb8green.png")
def set_FB07_grey(log_file):
    click(FB07_green)
    sleep(5)
    PF_common.verify(log_file,("1396333514212.png"))
    click("1396333538808.png")
    sleep(1)
    click("1396333582627.png")
    sleep(1)
    click("1396333605262.png")
    sleep(3)
    click(fix_icon)
    mouseMove(Location(1000,100))    
    sleep(5)
    PF_common.verify(log_file,"fb8grey.png")
    PF_common.write_log_with_screenshot(log_file, "FB07 is set to grey!")            
    


           

    
LK01_green=("lk1green.png")
def set_LK01_grey(log_file):
    click(LK01_green)
    sleep(3)
    if exists("1389742039148.png"):
        type(PF_common._password)
        sleep(1)
        click("1389742095839.png")
        sleep(5)     
    PF_common.verify(log_file,"1390020628935.png")
    click("1390020628935.png")
    click("1389817979018.png")
    click(fix_icon)
    mouseMove(Location(1000,100))    
    sleep(5)
    PF_common.verify(log_file,"lk1grey.png")
            
    PF_common.write_log_with_screenshot(log_file, "LK01 is set to grey!") 
    
LK03_green=("lk3green.png")

def set_LK03_grey(log_file):
    click(LK03_green)
    sleep(5)
    if exists("1389742039148.png"):
        type(PF_common._password)
        sleep(1)
        click("1389742095839.png")
        sleep(3)     
    PF_common.verify(log_file,"1390068268007.png")
            
    click("1390068268007.png")
    
    click("1389818291777.png")
    sleep(3)
    click(fix_icon) 
    sleep(5)
    mouseMove(Location(1000,100))
    PF_common.verify(log_file,"lk3grey.png")
            
    PF_common.write_log_with_screenshot(log_file, "LK03 is set to grey!") 
    
    
LK05_green=("lk5green.png")
def set_LK05_grey(log_file):
    click(LK05_green)
    sleep(5)
    if exists("1389742039148.png"):
        type(PF_common._password)
        sleep(1)
        click("1389742095839.png")
        sleep(3)    
    PF_common.verify(log_file,"1389818632828.png")
    click("1389818632828.png")
    sleep(2)
    click("1389818887123.png");click("1389818951938.png")
    sleep(3)
    click(fix_icon)
    sleep(5)
    mouseMove(Location(1000,100))
    PF_common.verify(log_file,"lk5grey.png")
    PF_common.write_log_with_screenshot(log_file, "LK05 is set to grey!")  

    
         
GL01_green=("1403699957947.png")

def set_GL01_grey(log_file):
    click(GL01_green)
    sleep(5)
    PF_common.verify(log_file,"1397822686053.png")
    click("1397822710861.png")
    sleep(2)
    click(fix_icon)
    sleep(5)
    mouseMove(Location(1000,100))
    PF_common.verify(log_file, "1397822850994.png")
    PF_common.write_log_with_screenshot(log_file, "GL01 is set to grey!")  

    
GL02_green=("1403700407750.png")
def set_GL02_grey(log_file):
    click(GL02_green)
    sleep(5)
    resume=(Pattern("1397824304800.png").similar(0.91))
    if exists(resume):click(resume)
    sleep(2)
    PF_common.load_browser_with_url(log_file,"https://www.youtube.com/watch?v=02DQL00zivI&index=10&list=PLRnM5wRWOH8Bs1cTbybzZdCCC7jmh64jU\n")
    sleep(10)
    type("w", Key.CTRL) 
    PF_common.locate_google_section(log_file)
    PF_common.verify(log_file,"1403700538421.png" )

    
GL03_green=("1403700548890.png")

def set_GL03_grey(log_file):
    click(GL03_green)
    sleep(5)
    PF_common.verify(log_file, "1397823232052.png")
    click("1397823339801.png")
    sleep(2)
    click("1397823384109.png")
    sleep(2)
    click("1397824049012.png")
    sleep(5)
    mouseMove(Location(1000,100))
    PF_common.verify(log_file, "1403700605466.png")

def FixGoogleSection(log_file):
    PF_common.GoogleLogin(log_file)
    if PF_common.verify_continue_with_similarity(log_file,"1404474658234.png",0.95)==0:
       PF_common.write_log_with_screenshot(log_file,"Google section is not orange")
       rs=7
    
    if exists(Pattern(GL01_green).similar(0.90)):set_GL01_grey(log_file);rs=7
    if exists(Pattern(GL02_green).similar(0.90)):set_GL02_grey(log_file);rs=7 
    if exists(Pattern(GL03_green).similar(0.90)):set_GL03_grey(log_file);rs=7 

def PF_check_required_init(log_file):
    sleep(2)
    rs=1
   
    PF_common.load_browser_with_url(log_file, PF_common._PF_link)
    sleep(2)

    PF_common.wait_find("1396563774390.png")
    wait(10)
    #FixGoogleSection(log_file)
    PF_common.FacebookLogin(log_file)
        
    PF_common.write_log_with_screenshot(log_file,"FB section1 before check!")
    FBFirstSection=("1404805532966.png")
    FBSecondSection=("1404805548873.png")
    pf_common.locate_linkedIn_section(log_file) 
    if PF_common.verify_continue_with_similarity(log_file,FBFirstSection,0.93)==0 or PF_common.verify_continue_with_similarity(log_file,FBSecondSection,0.93)==0 :
        PF_common.write_log_with_screenshot(log_file,"FB section1 in is not orange")           
        rs=2
    
    if exists(Pattern(FB01_green).similar(0.90)):set_FB01_grey(log_file);rs=2        
    if exists(Pattern(FB02_green).similar(0.90)):set_FB02_grey(log_file);rs=2
    if exists(Pattern(FB04_green).similar(0.90)):set_FB04_grey(log_file);rs=2
    if exists(Pattern(FB06_green).similar(0.90)):set_FB06_grey(log_file);rs=2
    if exists(Pattern(FB07_green).similar(0.90)): set_FB07_grey(log_file);rs=3
    
    PF_common.LinkedInLogIn(log_file)
    wait(10)
    if PF_common.verify_continue_with_similarity(log_file,"1404735275920.png",0.95)==0:
        
        PF_common.write_log_with_screenshot(log_file,"Linked in is not orange")
        rs=4
    
    if exists(Pattern(LK01_green).similar(0.90)):set_LK01_grey(log_file);rs=4 
    if exists(Pattern(LK03_green).similar(0.90)):set_LK03_grey(log_file);rs=4 
    if exists(Pattern(LK05_green).similar(0.90)):set_LK05_grey(log_file);rs=4 
    return rs

def reset_result(log_file):
    y=PF_check_required_init(log_file)
    PF_common.write_log(log_file, "value of y is:" +str(y))
    if y >1:
        #PF_Chrome_setup(log_file)
        PF_common.reset_account(log_file)
        y=PF_check_required_init(log_file)
        if y==1:PF_common.write_log_with_screenshot(log_file, "Required status are set to orange, ready to test!")
        else: 
            PF_common.write_log_with_screenshot(log_file,"Chrome setup failed! Please check out and restart setup!"+str(y))
            raise Exception("Chrome setup failed! Please check out and restart setup!"+str(y))
    else:
        PF_common.write_log_with_screenshot(log_file, "Required status are all already orange, ready to test!")

#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, "PF_Chrome_setup")
        print "Log_file: "+log_file
        print "email is: " +PF_common._email

        PF_common.disable_autofill(log_file)
        PF_common.InstallExtension(log_file)
        PF_common.ClearBrowsingData(log_file)

        reset_result(log_file)    
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        print "msg: "+msg
        PF_common.write_log_with_screenshot(log_file,msg)

        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        print "msg: "+msg
        PF_common.write_log_with_screenshot(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
