import PF_common
reload(PF_common)


    
def PF_WebApp_LK01_ProfileVisitsProtected_GreenToGrey_1328(log_file):
       
    ProfileVisitsProtected_green=("1404727575602.png")
    
    ProfileVisitsProtected_hover=("1404727588061.png")
    top_bar=("1404727300695.png")
    settings_saved=("1404727528522.png")
      
    recommended_setting=("1404727625280.png")

    save_setting=("1404727497030.png")
    
    fix_icon=("1404727363177.png")

    ProfileVisitsProtected_allowed=("1404735804215.png")
    

    #verify the above images 
    #print str(fix_icon)
    PF_common.verify(log_file,ProfileVisitsProtected_green)
    hover(ProfileVisitsProtected_green)
    PF_common.verify(log_file,ProfileVisitsProtected_hover)
    click(Pattern(ProfileVisitsProtected_hover).similar(0.50).targetOffset(0,-5))
    sleep(2)
    PF_common.ifPassword(log_file)
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,recommended_setting) 
    
    click(Pattern(recommended_setting).similar(0.50).targetOffset(-122,0))
    click(save_setting)

    PF_common.verify(log_file,settings_saved)
      
    click(fix_icon)
    
    PF_common.verify(log_file,ProfileVisitsProtected_allowed)

PrivacyFix_link = PF_common._PF_link   
test_case_id="PF-1328"

#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.LinkedInLogIn(log_file)
        
        PF_WebApp_LK01_ProfileVisitsProtected_GreenToGrey_1328(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)