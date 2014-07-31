import PF_common
reload(PF_common)

    
def PF_WebApp_GL_InGoogleAds_OrrangeToAllow_517(log_file):
    
    profile_visits_orange=("orange.png")
    ornage_hover=("orange_hover.png")
    orange_click=("orange_click.png")

    top_bar=("top_bar.png")
    fix_button=("Fixes.png")
    allowed=("gray.png")
    check_box=("check-box.png")
    

    PF_common.verify(log_file,profile_visits_orange)
    hover(profile_visits_orange)
    PF_common.verify(log_file, ornage_hover)
    sleep(1)
    click(orange_click)
    sleep(5)
    PF_common.verify(log_file, top_bar)  
    PF_common.verify(log_file,check_box)
    sleep(1) 
    click(fix_button)
    sleep(5)
    PF_common.verify(log_file, allowed)

    
    

test_case_id="PF-517"
#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.GoogleLogin(log_file)
        

        PF_WebApp_GL_InGoogleAds_OrrangeToAllow_517(log_file)

        PF_common.PassCase(log_file, test_case_id)

     
               
    except FindFailed, f:
        print "before f"
        msg =  "Find Failed Exception: %s " % f

        PF_common.write_log(log_file,msg)  
        print "after f"
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        print "exception"
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
