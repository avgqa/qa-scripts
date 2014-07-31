from sikuli import *
import PF_common
reload(PF_common)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1341"
    
def PF_WebApp_FB05_RemoveOldApps_OrangeToGreen_1341(log_file):
    
    remove_old_apps_orange=("remove_old_apps_orange.png")
    remove_old_apps_green=("remove_old_apps_green.png")
    remove_old_apps_tooltip=("remove_old_apps_tooltip.png")
    remove_old_apps_click=("remove_old_apps_click.png")
    remove_old_apps_selection=("remove_old_apps_selection.png")
    fix_icon=("fix_icon.png")
    remove_old_apps_topbar=("remove_old_apps_topbar.png")
    apps_checked_hover=("apps_checked_hover.png")

    
    PF_common.verify(log_file,remove_old_apps_orange)
    hover(remove_old_apps_orange)
    
    PF_common.verify(log_file,remove_old_apps_tooltip)
    click(remove_old_apps_click)
    sleep(10)

    PF_common.verify(log_file,remove_old_apps_topbar)
 
    PF_common.verify(log_file,remove_old_apps_selection)
    
    PF_common.verify(log_file,fix_icon)
    click(fix_icon)
    sleep(10)
    
    PF_common.verify(log_file,remove_old_apps_green)
    hover(remove_old_apps_green)

    PF_common.verify(log_file,apps_checked_hover)

#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
                
        PF_WebApp_FB05_RemoveOldApps_OrangeToGreen_1341(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        