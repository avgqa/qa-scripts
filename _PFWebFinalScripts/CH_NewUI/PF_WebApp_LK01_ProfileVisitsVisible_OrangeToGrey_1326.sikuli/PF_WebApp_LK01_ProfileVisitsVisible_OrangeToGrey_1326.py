import PF_common
reload(PF_common)


    
def PF_WebApp_LK01_ProfileVisitsVisible_OrangeToGrey_1326(log_file):
    
    
    ProfileVisitsVisible_orange=("1404727138623.png")
    ProfileVisitsVisible_hover=("1404727159153.png")
    top_bar=("1404727284774.png")
    ProfileVisitsVisible_settings=("1404727312893.png")    
    fix_icon=("1404727339586.png")
    ProfileVisitsVisible_allowed=("1404736556388.png")
    

    #verify the above images 
    #print str(fix_icon)
    PF_common.verify(log_file,ProfileVisitsVisible_orange)
    hover(ProfileVisitsVisible_orange)
    PF_common.verify(log_file,ProfileVisitsVisible_hover)
    click(Pattern(ProfileVisitsVisible_hover).similar(0.50).targetOffset(0,-5))
    sleep(3)
    PF_common.ifPassword(log_file)  
    
    PF_common.verify(log_file,top_bar)
    #PF_common.verify(log_file,ProfileVisitsVisible_settings)
    click(fix_icon)


    PF_common.verify(log_file,ProfileVisitsVisible_allowed)
    
PrivacyFix_link = PF_common._PF_link

test_case_id="PF-1326"

#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.LinkedInLogIn(log_file)
        
        PF_WebApp_LK01_ProfileVisitsVisible_OrangeToGrey_1326(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)