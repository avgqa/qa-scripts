import PF_common
reload(PF_common)

    
def PF_WebApp_LK04_Apps_checked_GreenToGreen_356(log_file):
    
    AppsChecked_Green=("green.png")
    AppsChecked_hover=("hover.png")
    check_click=("click.png")
    top_bar=("top_bar.png")    
    
    Settings=("settings.png")
    fix_icon=("fixes.png")

    AppsChecked_Green=("green.png")
 
    #verify the above images 
    #print str(fix_icon)
    PF_common.verify(log_file,AppsChecked_Green)
    hover(AppsChecked_Green)
    
    PF_common.verify(log_file,AppsChecked_hover)
    click(check_click)
    
    PF_common.ifPassword(log_file) 
    
    PF_common.verify(log_file,Settings)
   
    PF_common.verify(log_file, top_bar)
      
    click(fix_icon)
    PF_common.verify(log_file,AppsChecked_Green)
        
#variables
PrivacyFix_link = PF_common._PF_link
test_case_id="PF-356"

#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.LinkedInLogIn(log_file)
        
        PF_WebApp_LK04_Apps_checked_GreenToGreen_356(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)