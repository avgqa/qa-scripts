import PF_common_FF
reload(PF_common_FF)

    
def PF_WebApp_LK01_ProfileVisitsVisible_OrangeToGrey_1326(log_file):       
    ProfileVisitsVisible_orange=("orange.png")
    ProfileVisitsVisible_hover=("orange_hover.png")
    top_bar=("1400754958993.png")
    ProfileVisitsVisible_settings=("settings.png")    
    fix_icon=("fix_icon.png")
    ProfileVisitsVisible_grey=("grey.png")
    


    #PF_common_FF.locate_linkedIn_section(log_file)
    PF_common_FF.verify(log_file,ProfileVisitsVisible_orange)
    hover(ProfileVisitsVisible_orange)
    PF_common_FF.verify(log_file,ProfileVisitsVisible_hover)
    click(ProfileVisitsVisible_orange)
    sleep(2)
    
    PF_common_FF.ifPassword(log_file)
    PF_common_FF.verify(log_file,top_bar)
    PF_common_FF.verify(log_file,ProfileVisitsVisible_settings)
    click(fix_icon)

    PF_common_FF.verify(log_file,ProfileVisitsVisible_grey)



PrivacyFix_link = PF_common_FF._PF_link
test_case_id="PF-1326"


#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common_FF.create_log_folder(test_case_script_name, test_case_id)        
        
        PF_common_FF.InstallExtension(log_file)
        PF_common_FF.LinkedInLogIn(log_file)
        
        PF_WebApp_LK01_ProfileVisitsVisible_OrangeToGrey_1326(log_file)
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
 


