from sikuli import *
import PF_common
reload(PF_common)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1331"

def PF_WebApp_FB01_VisibleOnGoogle_GreyToGreen_1331(log_file):
    Findable_on_google_selection=("Findable_on_google_selection.png")
    Findable_on_google_checkbox=("Findable_on_google_checkbox.png")
    fix_icon=("fix_icon.png")
    
    Findable_on_google_grey=("Findable_on_google_grey.png")
    
    Findable_on_google_tooltipclick=("Findable_on_google_tooltipclick.png")
    Findable_on_google_tooltip=("Findable_on_google_tooltip.png")
    
    Findable_on_google_choice=("Findable_on_google_choice.png")
    Findable_on_google_choiceclick=("Findable_on_google_choiceclick.png")
    Not_Findable_on_google_green=("Not_Findable_on_google_green.png")
    
    
    
    
    Findable_on_google_topbar=("Findable_on_google_topbar.png")
  

    PF_common.verify(log_file, Findable_on_google_grey)
    hover(Findable_on_google_grey)
    
    PF_common.verify(log_file,Findable_on_google_tooltip)
    click(Findable_on_google_tooltipclick)
    sleep(5)

    PF_common.verify(log_file,Findable_on_google_topbar)
    sleep(3)

    PF_common.verify(log_file,Findable_on_google_selection)
    click(Findable_on_google_checkbox)

    PF_common.verify(log_file,Findable_on_google_choice)
    click(Findable_on_google_choiceclick)
    sleep(3)
    click(fix_icon)
    PF_common.verify(log_file,Not_Findable_on_google_green)
    
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
        PF_WebApp_FB01_VisibleOnGoogle_GreyToGreen_1331(log_file)
        
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