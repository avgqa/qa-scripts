import PF_common_FF as PF_common
reload(PF_common)

#setup link doesn't work consistant, not going to use it.
#setup_link="http://addons.privacyfix.com/pf/seenclear?uid=1e8e0c7992c57417cc4a6af0d3908f2e"

PF_link=PF_common._PF_link

test_case_id="PF_Firefox_setup"


hidefocus=("hidefocus.png")
fixes=("fixes.png")

FB01_green=("FB01_green.png")

def set_FB01_grey(log_file):
    
    mouseMove(Location(1000,120))
    click(Pattern(FB01_green).similar(0.90))
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    let_other_search =("LetOtherSearch.png")
    PF_common.verify_continue(log_file, let_other_search)
    sleep(1)
    click(let_other_search)
    sleep(2)
    click(fixes)
    sleep(5)
    mouseMove(Location(1000,100)) 
    PF_common.verify_continue(log_file,"FindableOnGoogle.png")
    PF_common.write_log_with_screenshot(log_file, "FB01 is set to grey!")                


FB02_green=("FB02_green.png")
def  set_FB02_grey(log_file):
    mouseMove(Location(1000,120))
    click(Pattern(FB02_green).similar(0.90))
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    noOne=("noOne_FB02.png")
    PF_common.verify_continue(log_file, noOne)
    sleep(2) 
    click(noOne)
    sleep(2)
    click("Friends.png")
            
    sleep(2)
    click(fixes)
    sleep(5)    
    mouseMove(Location(1000,100))    
    PF_common.verify_continue(log_file,"FaceMachingOn.png")
    PF_common.write_log_with_screenshot(log_file, "FB02 is set to grey!") 



FB04_green=("FB03_green.png")

def set_FB04_grey(log_file):
    mouseMove(Location(1000,120))
    click(Pattern(FB04_green).similar(0.90))
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    enabled=("enabled.png")
    PF_common.verify_continue(log_file,enabled)
    sleep(2)
    click(enabled)
    sleep(2)
    disabled=("disabled.png")
    PF_common.verify_continue(log_file,disabled)
    click(disabled)
    sleep(2)
    click(fixes)
    sleep(5)
    mouseMove(Location(1000,100)) 
    PF_common.verify_continue(log_file,"TagPreviewOff.png")
            
    PF_common.write_log_with_screenshot(log_file, "FB04 is set to grey!")    
    
    

FB06_green=("FB05_green.png")

def set_FB06_grey(log_file):
    mouseMove(Location(1000,120))
    click(Pattern(FB06_green).similar(0.90))
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    PF_common.wait_click("CheckBox_FB05.png") 
    sleep(1)
    click("SaveChanges_FB05.png")
    sleep(2)
    click(fixes)
    sleep(5)
    mouseMove(Location(1000,100))    
    PF_common.verify_continue(log_file,"AAppAccessOn.png")
            
    PF_common.write_log_with_screenshot(log_file, "FB06 is set to grey!")
    

    
FB07_green=("FB06_green.png")
def set_FB07_grey(log_file):
    mouseMove(Location(1000,120))
    click(Pattern(FB07_green).similar(0.90))
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    noOne_FB07=("noOne_FB06.png")
    PF_common.verify_continue(log_file,noOne_FB07)

    click(noOne_FB07)
    sleep(1)
    click("OnlyMyFriends_FB06.png")
    sleep(1)
    click("SaveChanges_FB06.png")
    sleep(1)
    click(fixes)
    sleep(5)
    mouseMove(Location(1000,100))    
    PF_common.verify_continue(log_file,"InFacebookAds.png")
    PF_common.write_log_with_screenshot(log_file, "FB07 is set to grey!")            
    

           

    
LK01_green=("LK01_green.png")
LK_save_changes=("LK_save_changes.png")

def set_LK01_grey(log_file):
    mouseMove(Location(1000,120))
    click(Pattern(LK01_green).similar(0.90))
    PF_common.ifPassword(log_file)
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))

    LK01_radio_button=("LK01_radio_button.png")
    PF_common.verify_continue(log_file, LK01_radio_button)
    click(LK01_radio_button)
    click(LK_save_changes)
    click(fixes)
    mouseMove(Location(1000,100))  
    PF_common.verify_continue(log_file,"LKo1_grey.png")          
    PF_common.write_log_with_screenshot(log_file, "LK01 is set to grey!") 
    
LK03_green=("LK03_green.png")

def set_LK03_grey(log_file):
    mouseMove(Location(1000,120))
    click(Pattern(LK03_green).similar(0.90))
    PF_common.ifPassword(log_file)
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    LK03_checkbox=("LK03_checkbox.png")
    PF_common.verify_continue(log_file, LK03_checkbox)
    click(LK03_checkbox)    
    click(LK_save_changes)
    sleep(2)
    click(fixes) 
    mouseMove(Location(1000,100))
    PF_common.verify_continue(log_file,"LK03_grey.png")
            
    PF_common.write_log_with_screenshot(log_file, "LK03 is set to grey!") 
    
    
LK05_green=("LK05_green.png")
def set_LK05_grey(log_file):
    mouseMove(Location(1000,120))
    click(Pattern(LK05_green).similar(0.90))
    PF_common.ifPassword(log_file)
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    LK05_only_you=("1390812494339.png")
    PF_common.verify_continue(log_file, LK05_only_you)
    click(LK05_only_you)
    sleep(1)
    click("LK05_your_connections.png");click(LK_save_changes)
    sleep(2)
    click(fixes)
    mouseMove(Location(1000,100))
    PF_common.verify_continue(log_file,"LK05_grey.png")
    PF_common.write_log_with_screenshot(log_file, "LK05 is set to grey!")  

    
         
GL01_green=("GL01_green.png")
def set_GL01_gray(log_file):
    GL01_gray=("GL01_gra.png")
    turnON=("turnON.png")
    mouseMove(Location(1000,120))
    click(Pattern(GL01_green).similar(0.90))
    sleep(2)
    PF_common.ifPassword(log_file)
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    PF_common.verify_continue(log_file,turnON)
    click(turnON)
    sleep(2)
    click(fixes)
    mouseMove(Location(1000,100))
    sleep(5)
    PF_common.verify_continue(log_file,GL01_gray)
    PF_common.write_log_with_screenshot(log_file, "GL01 is set to grey!") 
    
# Second item in Google section (YouTube history) is blocked by AP-882
GL02_green=("1398675957007.png")
def set_GL02_gray(log_file):
    GL02_gray=("1398675881814.png")
    resume=("1398676051128.png")
    pause=("1398676066429.png")    
    mouseMove(Location(1000,120))
    click(GL02_green)
    sleep(4)
    PF_common.ifPassword(log_file)
    sleep(4)
    if exists(Pattern(resume).similar(0.90)):
        click(Pattern(resume).similar(0.90))
        PF_common.verify_continue(log_file,pause)
    PF_common.load_browser_with_url("https://www.youtube.com/channel/UCOBefgX9GvHRr2Dn1hqllYw")    
    sleep(8)
    type("w", Key.CTRL)
    sleep(5)
    PF_common.verify_continue(log_file,GL02_gray)
    PF_common.write_log_with_screenshot(log_file, "GL02 is set to grey!")
        
GL03_green=("GL03_green.png")    
def set_GL03_gray(log_file):
    GL03_gray=("GL03_gra.png")
    settings=("GL_Ads_Settings.png")
    saveB=("Save_GL03.png")
    mouseMove(Location(1000,120))
    click(Pattern(GL03_green).similar(0.90))
    sleep(2)
    PF_common.ifPassword(log_file)
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))    
    PF_common.verify_continue(log_file,saveB)
    click(settings)
    sleep(2)
    click(saveB)
    sleep(2)
    click("1400760028072.png")
    sleep(5)
    PF_common.verify_continue(log_file,GL03_gray)
    PF_common.write_log_with_screenshot(log_file, "GL03 is set to grey!")


TW_save_changes=("TW_save_changes.png")
TW01_green=("TW01_green.png")
def set_TW01_gray(log_file):
    mouseMove(Location(1000,120))
    click(Pattern(TW01_green).similar(0.90))
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    click(Pattern("TW01_setting.png").similar(0.95))
    sleep(2)
    click(TW_save_changes)
    sleep(2)
    type(PF_common._password)
    sleep(2)
    type(Key.ENTER)
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    click(fixes)
    PF_common.verify_continue(log_file,"TW01_gray.png")
    PF_common.write_log_with_screenshot(log_file, "TW01 is set to grey!")
    

TW02_green=("TW02_green.png")
def set_TW02_gray(log_file):
    mouseMove(Location(1000,120))
    click(Pattern(TW02_green).similar(0.90))
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    click(Pattern("TW02_setting.png").similar(0.90))
    sleep(2)
    click(TW_save_changes)
    sleep(2)
    type(PF_common._password)
    sleep(2)
    type(Key.ENTER)
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    click(fixes)
    PF_common.verify_continue(log_file,"TW02_gray.png")
    PF_common.write_log_with_screenshot(log_file, "TW02 is set to grey!")
    
TW03_green=("TW03_green.png")
def set_TW03_gray(log_file):
    mouseMove(Location(1000,120))
    click(Pattern(TW03_green).similar(0.90))
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    click(Pattern("TW03_setting.png").similar(0.95))
    sleep(2)
    click(TW_save_changes)
    sleep(2)
    type(PF_common._password)
    sleep(2)
    type(Key.ENTER)
    sleep(5)
    click(Pattern(hidefocus).similar(0.90))
    click(fixes)
    PF_common.verify_continue(log_file,"TW03_gray.png")
    PF_common.write_log_with_screenshot(log_file, "TW03 is set to grey!")



def PF_check_required_init():

    PF_common.locate_tracking_section(log_file )
    rs=1

    PD02_Orange=("PD02_Orange.png")
    PD03_Orange=("PD03_Orange.png")
       
    t1=PF_common.verify_continue_with_similarity(log_file,PD02_Orange,0.90)
    t2=PF_common.verify_continue_with_similarity(log_file,PD03_Orange,0.90)
    
    if t1==0 or t2==0:
        PF_common.write_log_with_screenshot(log_file,"Personal Data & Tracking section is not orange")
        rs=2 
    else:
        PF_common.write_log_with_screenshot(log_file,"Personal Data & Tracking section IS orange!")      

    #PF_common.GoogleLogin(log_file)
    #if PF_common.verify_continue_with_similarity(log_file,"GoogleSection.png", 0.90)==0:
       # PF_common.write_log_with_screenshot(log_file,"Google section status is NOT set to orange!")
        #rs=3
 #       if exists(Pattern(GL01_green).similar(0.90)):set_GL01_gray(log_file)
#        if exists(Pattern(GL02_green).similar(0.90)):set_GL02_gray(log_file)  This item is blocked by AP-882
#        if exists(Pattern(GL03_green).similar(0.90)):set_GL03_gray(log_file)
 #   else: 
 #       PF_common.write_log_with_screenshot(log_file,"Google section IS SET  to orange!")

################################
#    PF_common.TwitterLogIn(log_file)
 #   if PF_common.verify_continue_with_similarity(log_file,"TW_section.png",0.90)==0:
 #       PF_common.write_log_with_screenshot(log_file,"Twitter section in IS NOT orange")
  #      rs=4
   #     if exists(Pattern(TW01_green).similar(0.90)):set_TW01_grey(log_file)
 #       if exists(Pattern(TW02_green).similar(0.90)):set_TW02_grey(log_file)
 #       if exists(Pattern(TW03_green).similar(0.90)):set_TW03_grey(log_file) 
 #   else:
 #       PF_common.write_log_with_screenshot(log_file,"Twitter section IS orange!") 
        
#################################
  
    PF_common.FacebookLogin(log_file)
   
    if PF_common.verify_continue_with_similarity(log_file,"FisrstTwoItems_FB.png",0.90)==0:
        PF_common.write_log_with_screenshot(log_file,"FB section1 is NOT orange")           
        rs=5 
        if exists(Pattern(FB01_green).similar(0.90)):set_FB01_grey(log_file)

        if exists(Pattern(FB02_green).similar(0.90)):set_FB02_grey(log_file)
    else:
        PF_common.write_log_with_screenshot(log_file,"First two items in FB section are orange!")
    
    type(Key.DOWN+Key.DOWN+Key.DOWN)

    if PF_common.verify_continue_with_similarity(log_file,"1400763451939.png",0.90)==0:
        PF_common.write_log_with_screenshot(log_file,"FB section2 is NOT orange")           
        rs=5 
        if exists(Pattern(FB04_green).similar(0.90)):set_FB04_grey(log_file)
        if exists(Pattern(FB06_green).similar(0.90)):set_FB06_grey(log_file)
        if exists(Pattern(FB07_green).similar(0.90)):set_FB07_grey(log_file)
    else:
        PF_common.write_log_with_screenshot(log_file,"Items from 4 till 9 are orange!")

   
    PF_common.LinkedInLogIn(log_file)

    if PF_common.verify_continue_with_similarity(log_file,"LK_section.png",0.90)==0:
        PF_common.write_log_with_screenshot(log_file,"Linked in IS NOT orange")
        rs=6
        if exists(Pattern(LK01_green).similar(0.90)):set_LK01_grey(log_file)
        if exists(Pattern(LK03_green).similar(0.90)):set_LK03_grey(log_file)
        if exists(Pattern(LK05_green).similar(0.90)):set_LK05_grey(log_file) 
    else:
        PF_common.write_log_with_screenshot(log_file,"LinkedIn section IS orange!") 
                   
    PF_common.write_log_with_screenshot(log_file, "end of Init")
    return rs

def reset_result(log_file):
    y=PF_check_required_init()
    PF_common.write_log(log_file, "value of y is:" +str(y))
    if y==1:
        msg="Required status are all already orange, ready to test!"
        PF_common.write_log_with_screenshot(log_file, msg)
        return
    if (y >1):
        #PF_Chrome_setup(log_file)
        PF_common.reset_account(log_file)
        y=PF_check_required_init()
        if y==1: 
            msg="Required status are set to orange, ready to test!"
            PF_common.write_log_with_screenshot(log_file, msg)
            return
        else: 
            msg="Chrome setup failed! Please check out!"+str(y)
            PF_common.write_log_with_screenshot(log_file,msg)
            raise Exception(msg)

        
        

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name,test_case_id)
 
                
        PF_common.rememberPassword(log_file)
        PF_common.ClearBrowsingData(log_file)                #avoid install link autofill for _PF_link        
        PF_common.InstallExtension(log_file)
        
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
