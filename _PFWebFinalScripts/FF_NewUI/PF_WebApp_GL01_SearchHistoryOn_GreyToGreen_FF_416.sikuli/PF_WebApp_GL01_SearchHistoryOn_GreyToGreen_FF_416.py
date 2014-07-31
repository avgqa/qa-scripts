import PF_common_FF as PF_common
reload(PF_common)

    
def PF_SearchHistoryOn_AllowedToMostPrivate_416(log_file):
    
    search_history_on_allowed=("allowed.png")
    search_history_on_allowed_mouseover=("mouseover.png")
    search_history_on_allowed_click=("mouseoverclick.png")
    top_bar=("topbar.png")
    turn_on=("turnon.png")
    turn_off=("turnoff.png")
    fixes_icon=("fixes.png")

    search_history_most_private=("mostprivate.png")
    
    PF_common.verify(log_file, search_history_on_allowed)
    hover(search_history_on_allowed)
    PF_common.verify(log_file, search_history_on_allowed_mouseover)
    hover(search_history_on_allowed)
    sleep(1)
    click(search_history_on_allowed_click)
    sleep(5)
    PF_common.verify(log_file, top_bar)  
    click(turn_off)
    PF_common.verify(log_file, turn_on)
    click(fixes_icon)
    sleep(5)
    PF_common.verify(log_file, search_history_most_private)
    
PrivacyFix_link = PF_common._PF_link
test_case_id="PF-416"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.GoogleLogin(log_file)
        

        PF_SearchHistoryOn_AllowedToMostPrivate_416(log_file)

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
