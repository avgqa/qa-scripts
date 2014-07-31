import PF_common
reload(PF_common)


    
def PF_WebApp_LK03_ProfileChengesVisable_GreyToGreen_1338(log_file):
    
    
    ProfileChengesVisable_Grey=("1404737741488.png")
    ProfileChengesVisable_hover=("1404737749709.png")
    check_click=("1404737756607.png")
    top_bar=("1404737629863-1.png")    
    
    CheckYourProfile_Settings=("1404737813279.png")
    check_setting_click=("1404737825920.png")
    click_save=("1404737859995.png")
    success=("1404738118949.png")
    fix_icon=("1404737865578.png")

    CheckYourProfile_green=("1404737895250.png")
    
    

    #verify the above images 
    #print str(fix_icon)
    PF_common.verify(log_file,ProfileChengesVisable_Grey)
    hover(ProfileChengesVisable_Grey)
    
    PF_common.verify(log_file,ProfileChengesVisable_hover)
    click(check_click)
    sleep(2)
    PF_common.ifPassword(log_file) 
  
    PF_common.verify(log_file,CheckYourProfile_Settings)
    PF_common.verify(log_file, top_bar)

    PF_common.verify(log_file,check_setting_click) 
    click(check_setting_click)

    PF_common.verify(log_file,click_save)
    click(click_save)
    sleep(3)
    PF_common.verify(log_file, success)
    click(fix_icon)
  
    PF_common.verify(log_file,CheckYourProfile_green)
    
PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1338"

#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.LinkedInLogIn(log_file)
        
        PF_WebApp_LK03_ProfileChengesVisable_GreyToGreen_1338(log_file)
        PF_common.PassCase(log_file, test_case_id)

    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)