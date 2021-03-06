import PF_common
reload(PF_common)


    
def PF_SearchHistoryOff_MostPrivateToAllowed_419(log_file):
   
    
    search_history_off=("green.png")
    search_history_off_mouseover=("green_hover.png")
    search_history_off_click=("green_click.png")
    top_bar=("top_bar.png")
    turn_on=("turnon.png")
    turn_off=("turnoff.png")
    fixes_icon=("fixes.png")

    search_history_on_allowed=("gray.png")
    


    PF_common.verify(log_file,search_history_off)
    hover(search_history_off)
    PF_common.verify(log_file,search_history_off_mouseover)
    sleep(1)
    #hover(search_history_off)
    sleep(1)
    click(search_history_off_click)
    sleep(5)
    PF_common.verify(log_file, top_bar)  
    click(turn_on)
    sleep(1)
    PF_common.verify(log_file, turn_off)
    click(fixes_icon)
    sleep(5)
    PF_common.verify(log_file, search_history_on_allowed)
    

test_case_id="PF-419"

#Function_call
if __name__ == "__main__":
    log_file=""    
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.GoogleLogin(log_file)
        

        PF_SearchHistoryOff_MostPrivateToAllowed_419(log_file)

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