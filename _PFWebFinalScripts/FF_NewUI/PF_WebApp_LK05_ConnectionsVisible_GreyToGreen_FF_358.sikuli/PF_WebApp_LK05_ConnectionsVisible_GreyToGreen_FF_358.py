import PF_common_FF
reload(PF_common_FF)

    
def PF_WebApp_LK05_ConnectionsVisible_GreyToGreen_FF_358(log_file):
     
    ConnectionsVisible_grey=("grey.png")
    ConnectionsVisible_hover=("grey_hover.png")
    top_bar=("top_bar.png")
       
    settings_window=("settings.png")
    
    your_connections=("your_connectinions.png")    
       
    Only_You=("only_you.png")
    Only_You_select=("only_you2.png")
    save_changes_button=("save_changes.png")
    setiings_saved=("settings_saved.png")
    fix_icon=("fix_icon.png")

    ConnectionsVisible_green=("green.png")
    
    
    
    PF_common_FF.locate_linkedIn_section(log_file)
    PF_common_FF.verify(log_file,ConnectionsVisible_grey)
    hover(ConnectionsVisible_grey)     
    PF_common_FF.verify(log_file,ConnectionsVisible_hover)
    click(ConnectionsVisible_grey)
    sleep(2)
    
    PF_common_FF.ifPassword(log_file)

    PF_common_FF.verify(log_file,top_bar)
    PF_common_FF.verify(log_file,settings_window)
    click(your_connections)    
    hover(Only_You)
    click(Only_You_select)
    click(save_changes_button) 
    sleep(2)
    PF_common_FF.verify(log_file,setiings_saved)  
    
    click(fix_icon)
    sleep(2)
    PF_common_FF.verify(log_file,ConnectionsVisible_green)

       
#variables
PrivacyFix_link = PF_common_FF._PF_link
test_case_id="PF-358"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common_FF.create_log_folder(test_case_script_name, test_case_id)  

        PF_common_FF.InstallExtension(log_file)
        PF_common_FF.LinkedInLogIn(log_file)
        
        PF_WebApp_LK05_ConnectionsVisible_GreyToGreen_FF_358(log_file)
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