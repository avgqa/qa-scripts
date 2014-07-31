import PF_common
reload(PF_common)


    
def PF_WebApp_LK01_ProfileVisitsVisible_GreyToGreen_1327(log_file):
    
    
    ProfileVisitsVisible_allowed=("1404727400486.png")
    ProfileVisitsVisible_hover=("1404727407948.png")
    top_bar=("1404727293281.png")
    
    profile_changes_anonymous=("1404727468319.png")
    profile_changes_save=("1404727488168.png")
    settings_saved=("1404727519637.png")
     
    fix_icon=("1404727352364.png")

    ProfileVisitsVisible_mostprivate=("1404736335016.png")
    

    PF_common.verify(log_file,ProfileVisitsVisible_allowed)
    hover(ProfileVisitsVisible_allowed)
    
    PF_common.verify(log_file,ProfileVisitsVisible_hover)
    click(Pattern(ProfileVisitsVisible_hover).similar(0.75).targetOffset(0,-5))
    sleep(3)
    
    PF_common.ifPassword(log_file)
                 
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,profile_changes_anonymous)
    click(Pattern(profile_changes_anonymous).similar(0.75).targetOffset(-91,0))

    PF_common.verify(log_file,profile_changes_save)
    click(profile_changes_save)

    PF_common.verify(log_file,settings_saved)
    PF_common.verify(log_file,fix_icon)
    click(fix_icon)
     
    PF_common.verify(log_file,ProfileVisitsVisible_mostprivate)

PrivacyFix_link = PF_common._PF_link   
test_case_id="PF-1327"

#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file = PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.LinkedInLogIn(log_file)
        
        PF_WebApp_LK01_ProfileVisitsVisible_GreyToGreen_1327(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        type("l", KEY_CTRL)
        type(failed_link)    
        type(Key.ENTER)
        print msg
        PF_common.write_log(log_file,msg)
        PF_common.write_log (log_file,'PF-1327 Test Case failed!')  

    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)