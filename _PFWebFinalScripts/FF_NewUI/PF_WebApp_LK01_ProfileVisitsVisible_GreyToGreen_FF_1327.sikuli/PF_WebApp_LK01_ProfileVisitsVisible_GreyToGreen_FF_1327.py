import PF_common_FF
reload(PF_common_FF)
   
def PF_WebApp_LK01_ProfileVisitsVisible_GreyToGreen_FF_1327(log_file):
    
        
    ProfileVisitsVisible_grey=("grey.png")
    ProfileVisitsVisible_hover=("grey_hover.png")
    top_bar=("top_bar.png")
    
    top_bar01=("top_bar01.png")
    
    profile_changes_anonymous=("settings_anonymous.png")
    profile_changes_save=("save_button.png")
    settings_saved=("settings_saved.png")
     
    fix_icon="fix_icon.png"

    ProfileVisitsVisible_green=("green.png")
    
    

    PF_common_FF.locate_linkedIn_section(log_file) 
    PF_common_FF.verify(log_file,ProfileVisitsVisible_grey)
    hover(ProfileVisitsVisible_grey)  
    PF_common_FF.verify(log_file,ProfileVisitsVisible_hover)
    click(ProfileVisitsVisible_grey)
    sleep(2)
    
    PF_common_FF.ifPassword(log_file)
        
    PF_common_FF.verify(log_file,top_bar)
    PF_common_FF.verify(log_file,profile_changes_anonymous)
    click(Pattern(profile_changes_anonymous).similar(0.75).targetOffset(-95,0))
    PF_common_FF.verify(log_file,profile_changes_save)
    click(profile_changes_save)
    sleep(2)        
    
    PF_common_FF.verify(log_file,settings_saved)    
    click(fix_icon)
    sleep(2)
    
    PF_common_FF.verify(log_file,ProfileVisitsVisible_green)


PrivacyFix_link = PF_common_FF._PF_link
test_case_id="PF-1327"

      
#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common_FF.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common_FF.InstallExtension(log_file)
        PF_common_FF.LinkedInLogIn(log_file)
        
        PF_WebApp_LK01_ProfileVisitsVisible_GreyToGreen_FF_1327(log_file)
        PF_common_FF.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        print "before f"
        msg =  "Find Failed Exception: %s " % f

        PF_common_FF.write_log(log_file,msg)  
        print "after f"
        PF_common_FF.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        print "exception"
        PF_common_FF.write_log(log_file,msg)        
        PF_common_FF.FailTestCase(log_file, test_case_id)
  


