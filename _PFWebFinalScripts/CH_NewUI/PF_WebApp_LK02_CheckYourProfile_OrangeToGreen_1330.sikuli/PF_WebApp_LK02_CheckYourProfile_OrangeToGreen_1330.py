import PF_common
reload(PF_common)

    
def PF_WebApp_LK02_CheckYourProfile_OrangeToGreen_1330(log_file):
    
    CheckYourProfile_Orange=("1404736914050.png")
    CheckYourProfile_hover=("1404736924035.png")
    check_click=("1404736936417.png")
    top_bar=("1404736959652.png")    
    
    CheckYourProfile_Settings=("1404736972202.png")
    fix_icon=("1404736979721.png")

    CheckYourProfile_Reviewed=("1404736999120.png")
    

    #verify the above images 
    #print str(fix_icon)
    PF_common.verify(log_file,CheckYourProfile_Orange)
    hover(CheckYourProfile_Orange)
    
    PF_common.verify(log_file,CheckYourProfile_hover)
    click(check_click)   
    sleep(2)
    PF_common.ifPassword(log_file)
  
    PF_common.verify(log_file,CheckYourProfile_Settings)
    PF_common.verify(log_file, top_bar)
      
    click(fix_icon)
    
    PF_common.verify(log_file,CheckYourProfile_Reviewed)
    
PrivacyFix_link = PF_common._PF_link   
test_case_id="PF-1330"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.LinkedInLogIn(log_file)
        
        PF_WebApp_LK02_CheckYourProfile_OrangeToGreen_1330(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)