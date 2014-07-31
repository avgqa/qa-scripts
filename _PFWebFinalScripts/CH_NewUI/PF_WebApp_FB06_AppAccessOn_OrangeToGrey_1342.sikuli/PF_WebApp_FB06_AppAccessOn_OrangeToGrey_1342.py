from sikuli import *
import PF_common
reload(PF_common)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1342"

def PF_Web_FB06_AppAccessOn_OrangeToGreen_1342(log_file):
    
    
    apps_access_orange=("apps_access_orange.png")
    apps_access_orange_mouseover=("apps_access_orange_mouseover.png")
    apps_access_orange_fix=("apps_access_orange_fix.png")
    top_bar=("top_bar.png")
    fixes_icon=("fixes_icon.png")
    apps_others_use=("apps_others_use.png")
    apps_access_revieved=("apps_access_revieved.png")
       

    PF_common.verify(log_file, apps_access_orange)
    hover(apps_access_orange)
    PF_common.verify(log_file, apps_access_orange_mouseover)
    click(apps_access_orange_fix)
    PF_common.verify(log_file, top_bar)
    PF_common.verify(log_file, apps_others_use)
    click(fixes_icon)
    mouseMove(Location(1000,150)) 
    PF_common.verify(log_file, apps_access_revieved)
        
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
        PF_Web_FB06_AppAccessOn_OrangeToGreen_1342(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)