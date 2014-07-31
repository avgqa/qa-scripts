from sikuli import *
import PF_common
reload(PF_common)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1306"

def PF_WebApp_FB01_VisibleOnGoogle_OrangeToGrey_1306(log_file):
       
    visible_on_google_orange=("visible_on_google_orange.png")
    
    
    visible_on_google_tooltip=("visible_on_google_tooltip.png")
    
    visible_on_google_click=("visible_on_google_click.png")
    
    visible_on_google_selection=("visible_on_google_selection.png")
    fix_icon=("fix_icon.png")

    visible_on_google_grey=("visible_on_google_grey.png")
    
    visible_on_google_topbar=("visible_on_google_topbar.png")
    

    #verify the above images 
    #print str(fix_icon)
    
    PF_common.verify(log_file,visible_on_google_orange)
    hover(visible_on_google_orange)

    PF_common.verify(log_file,visible_on_google_tooltip)
    click(visible_on_google_click)


    PF_common.verify(log_file,visible_on_google_topbar)
 
    PF_common.verify(log_file,visible_on_google_selection)
    
    PF_common.verify(log_file,fix_icon)
    click(fix_icon)
    
    PF_common.verify(log_file,visible_on_google_grey)
    
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
        PF_WebApp_FB01_VisibleOnGoogle_OrangeToGrey_1306(log_file)
        PF_common.PassCase(log_file, test_case_id)

    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        print "exception"
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)