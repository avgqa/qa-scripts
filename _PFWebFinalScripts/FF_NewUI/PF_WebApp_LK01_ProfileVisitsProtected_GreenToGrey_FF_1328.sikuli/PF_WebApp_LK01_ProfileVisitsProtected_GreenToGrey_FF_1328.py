import PF_common_FF
reload(PF_common_FF)
    
def PF_WebApp_LK01_ProfileVisitsProtected_GreenToGrey_1328(log_file):
    
   
    ProfileVisitsProtected_green=("green.png")
    
    ProfileVisitsProtected_hover=("green_hover.png")
    top_bar=("top_bar.png")
    settings_saved=("settings_saved.png")
      
    recommended_setting=("recomended_settings.png")

    save_setting=("Savechanges_button.png")
    
    fix_icon="fix_icon.png"

    ProfileVisitsProtected_grey=("grey.png")
    

    PF_common_FF.locate_linkedIn_section(log_file)
    PF_common_FF.verify(log_file,ProfileVisitsProtected_green)
    hover(ProfileVisitsProtected_green)
    PF_common_FF.verify(log_file,ProfileVisitsProtected_hover)
    click(ProfileVisitsProtected_green)
    sleep(2)
    
    PF_common_FF.ifPassword(log_file)
        
    PF_common_FF.verify(log_file,top_bar)
    PF_common_FF.verify(log_file,recommended_setting) 
    click(Pattern(recommended_setting).similar(0.50).targetOffset(-130,0))
    click(save_setting)
    sleep(5)
    PF_common_FF.verify(log_file,settings_saved)
      
    click(fix_icon)
    sleep(2)
    PF_common_FF.verify(log_file,ProfileVisitsProtected_grey)

PrivacyFix_link = PF_common_FF._PF_link
test_case_id="PF-1328"


#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common_FF.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common_FF.InstallExtension(log_file)
        PF_common_FF.LinkedInLogIn(log_file)
        
        PF_WebApp_LK01_ProfileVisitsProtected_GreenToGrey_1328(log_file)
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
  


