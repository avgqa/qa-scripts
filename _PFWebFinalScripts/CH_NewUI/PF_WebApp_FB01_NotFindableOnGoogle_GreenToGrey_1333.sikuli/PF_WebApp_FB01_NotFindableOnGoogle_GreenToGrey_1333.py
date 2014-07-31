from sikuli import *
import PF_common
reload(PF_common)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1333"
  
def PF_WebApp_FB01_NotFindableOnGoogle_GreenToGrey_1333(log_file):
    
    not_findable_on_google_selection=("not_findable_on_google_selection.png")
    not_findable_on_google_checkbox=("not_findable_on_google_checkbox.png")
    fix_icon=("fix_icon.png")
    

    not_findable_on_google_grey=("not_findable_on_google_grey.png")
    
    not_findable_on_google_grey_tooltip=("not_findable_on_google_grey_tooltip.png")
    
    
    not_findable_on_google_green=("not_findable_on_google_green.png")
     
    not_findable_on_google_tooltip=("not_findable_on_google_tooltip.png")
    
    not_findable_on_google_tooltipclick=("not_findable_on_google_tooltipclick.png")
    
    not_findable_on_google_topbar=("not_findable_on_google_topbar.png")


    #verify the above images 
    #print str(fix_icon)
    
    PF_common.verify(log_file,not_findable_on_google_green)
    hover(not_findable_on_google_green)
    
    PF_common.verify(log_file,not_findable_on_google_tooltip)
    click(not_findable_on_google_tooltipclick)

    PF_common.verify(log_file,not_findable_on_google_topbar)

    PF_common.verify(log_file,not_findable_on_google_selection)
    click(not_findable_on_google_checkbox)
    sleep(3)
    click(fix_icon)
    PF_common.verify(log_file,not_findable_on_google_grey)
   

#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)

        PF_WebApp_FB01_NotFindableOnGoogle_GreenToGrey_1333(log_file)
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