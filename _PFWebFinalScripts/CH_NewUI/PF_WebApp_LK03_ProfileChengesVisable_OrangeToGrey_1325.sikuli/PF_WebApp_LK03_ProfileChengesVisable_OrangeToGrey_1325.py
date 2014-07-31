import PF_common
reload(PF_common)




def PF_WebApp_LK03_ProfileChengesVisable_OrangeToGrey_1325(log_file):
    
    ProfileChengesVisable_Orange=("1404737580748.png")
    ProfileChengesVisable_hover=("1404737590307.png")
    check_click=("1404737600579.png")
    top_bar=("1404737629863.png")    
    
    CheckYourProfile_Settings=("1404737644471.png")
    fix_icon=("1404737662796.png")

    CheckYourProfile_Reviewed=("1404737679018.png")
    
    #verify the above images 
    #print str(fix_icon)
    PF_common.verify(log_file,ProfileChengesVisable_Orange)
    hover(ProfileChengesVisable_Orange)
    
    PF_common.verify(log_file,ProfileChengesVisable_hover)
    click(check_click)
    PF_common.ifPassword(log_file) 

    PF_common.verify(log_file,CheckYourProfile_Settings)
    PF_common.verify(log_file, top_bar)
      
    click(fix_icon)   
    PF_common.verify(log_file,CheckYourProfile_Reviewed)
            
PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1325"

#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.LinkedInLogIn(log_file)
        
        PF_WebApp_LK03_ProfileChengesVisable_OrangeToGrey_1325(log_file)
        PF_common.PassCase(log_file, test_case_id)

    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)