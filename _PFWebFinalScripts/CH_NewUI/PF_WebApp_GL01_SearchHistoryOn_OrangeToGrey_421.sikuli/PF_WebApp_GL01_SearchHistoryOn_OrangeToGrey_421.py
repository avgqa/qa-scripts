import PF_common
reload(PF_common)

    
def PF_SearchHistoryOn_OrangeToAllowed_421(log_file):
    
   
    search_history_on_orange=("orange.png")
    search_history_on_orange_mouseover=("orange_hover.png")
    search_history_fix=("orange_click.png")
    top_bar=("top_bar.png")
    turn_off=("turn_off.png")
    fixes_icon=("Fixes.png")

    search_history_allowed=("Gray.png")
    

    PF_common.verify(log_file, search_history_on_orange)
    hover(search_history_on_orange)
    PF_common.verify(log_file, search_history_on_orange_mouseover)
    #hover(search_history_on_orange)
    sleep(1)
    click(search_history_fix)
    sleep(5)
    PF_common.verify(log_file, top_bar)  
    PF_common.verify(log_file, turn_off) 
    click(fixes_icon)
    sleep(5)
    PF_common.verify(log_file, search_history_allowed)     
    



#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.GoogleLogin(log_file)
        

        PF_SearchHistoryOn_OrangeToAllowed_421(log_file)

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
