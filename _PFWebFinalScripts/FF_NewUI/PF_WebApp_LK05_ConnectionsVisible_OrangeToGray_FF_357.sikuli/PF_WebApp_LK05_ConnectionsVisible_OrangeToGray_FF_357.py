import PF_common_FF
reload(PF_common_FF)


    
def PF_WebApp_LK05_ConnectionsVisible_OrangeToGray_FF_357(log_file): 

    connections_visible_orange=("orange.png")
    connections_visible_orange_hover=("orange_hover.png")
    top_bar=("top_bar.png")
    fix_icon=("fix_icon.png")
    settings_window="settings.png"
    
    
    connections_visible_grey=("grey.png")

    
    PF_common_FF.locate_linkedIn_section(log_file) 
    PF_common_FF.verify(log_file, connections_visible_orange)
    hover(connections_visible_orange)
    PF_common_FF.verify(log_file, connections_visible_orange_hover)
    click(connections_visible_orange)
    sleep(2)
    
    PF_common_FF.ifPassword(log_file)
    
    PF_common_FF.verify(log_file, top_bar)
    PF_common_FF.verify(log_file, settings_window)
    click(fix_icon)
    sleep(2)
    
    PF_common_FF.verify(log_file, connections_visible_grey)
          


PrivacyFix_link=PF_common_FF._PF_link
test_case_id="PF-357"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common_FF.create_log_folder(test_case_script_name, test_case_id)        

        PF_common_FF.InstallExtension(log_file)    
        PF_common_FF.LinkedInLogIn(log_file)
        
        PF_WebApp_LK05_ConnectionsVisible_OrangeToGray_FF_357(log_file)
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