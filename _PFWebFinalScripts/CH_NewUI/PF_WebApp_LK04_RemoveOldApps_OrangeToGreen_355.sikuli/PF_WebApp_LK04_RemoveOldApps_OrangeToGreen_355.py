import PF_common
reload(PF_common)

    
def PF_WebApp_LK04_RemoveOldApps_OrangeToGreen_355(log_file):
    
    RemoveOldApps_Orange=("orange.png")
    RemoveOldApps_hover=("hover.png")
    check_click=("click.png")
    top_bar=("top_bar.png")    
    
    Settings=("settings.png")
    fix_icon=("fixes.png")

    Appschecked_Reviewed=("green.png")
    

    #verify the above images 
    #print str(fix_icon)
    PF_common.verify(log_file,RemoveOldApps_Orange)
    hover(RemoveOldApps_Orange)
    
    PF_common.verify(log_file,RemoveOldApps_hover)
    click(check_click)   
    sleep(2)
    PF_common.ifPassword(log_file)
  
    PF_common.verify(log_file,Settings)
    PF_common.verify(log_file, top_bar)
      
    click(fix_icon)
    
    PF_common.verify(log_file,Appschecked_Reviewed)
    
PrivacyFix_link = PF_common._PF_link   
test_case_id="PF-355"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.LinkedInLogIn(log_file)
        
        PF_WebApp_LK04_RemoveOldApps_OrangeToGreen_355(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)