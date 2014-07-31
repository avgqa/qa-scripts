from sikuli import *
import PF_common
reload(PF_common)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1344"
    
def PF_WebApp_FB06_App_Access_On_GreenToGrey_1344(log_file):
    
    apps_access_grey=("apps_access_grey.png")
    apps_access_green_mouseover=("apps_access_green_mouseover.png")
    
    apps_access_green_fix=("apps_access_green_fix.png")
    top_bar=("top_bar.png")
    fixes_icon=("fixes_icon.png")
    checkbox=("checkbox.png")
    
    save=("save.png")
    apps_access_green=("apps_access_green.png")

    PF_common.verify(log_file, apps_access_green)
    hover(apps_access_green)
    PF_common.verify(log_file, apps_access_green_mouseover)
    click(apps_access_green_fix)
    
    PF_common.verify(log_file, top_bar)
    i=0
    while exists(checkbox) and i<3:
        click(checkbox)
        sleep(5)
        i+=1
    click(save)
    sleep(2)
    click(fixes_icon)   

    PF_common.verify(log_file, apps_access_grey)
    
    
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
        PF_WebApp_FB06_App_Access_On_GreenToGrey_1344(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)