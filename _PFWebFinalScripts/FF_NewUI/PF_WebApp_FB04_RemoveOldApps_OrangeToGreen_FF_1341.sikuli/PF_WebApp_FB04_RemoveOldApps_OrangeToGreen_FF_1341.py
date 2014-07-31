import PF_common_FF as PF_common
reload(PF_common)
    
def PF_WebApp_FB04_RemoveOldApps_OrangeToGreen_1341(log_file):
    
    remove_old_apps_orange=("orange.png")
    remove_old_apps_green=("green.png")
    remove_old_apps_tooltip=("orange_hover.png")

    remove_old_apps_selection=("selection.png")
    fix_icon=("Fixes.png")
    remove_old_apps_topbar=("top_bar.png")
    remove_old_apps_green_tooltip = ("green_hover.png")

    
    #verify the above images 
    #print str(fix_icon)
 #   PF_common.locate_item_page_by_page(log_file,remove_old_apps_orange)
    PF_common.verify(log_file,remove_old_apps_orange)
    hover(remove_old_apps_orange)

    PF_common.verify(log_file,remove_old_apps_tooltip)
    mouseMove(Location(1000,120))
    click(remove_old_apps_orange)    
    sleep(2)
    
    PF_common.verify(log_file,remove_old_apps_topbar)
    PF_common.verify(log_file,remove_old_apps_selection)    

    click(fix_icon)
    sleep(2)


    
    PF_common.verify(log_file,remove_old_apps_green)
    hover(remove_old_apps_green)

    PF_common.verify(log_file,remove_old_apps_green_tooltip)
    
    


PrivacyFix_link = PF_common._PF_link

test_case_id="PF-1341"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)       
        PF_common.FacebookLogin(log_file)   
        
        

        
        PF_WebApp_FB04_RemoveOldApps_OrangeToGreen_1341(log_file)
        PF_common.PassCase(log_file, test_case_id)

             
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)        