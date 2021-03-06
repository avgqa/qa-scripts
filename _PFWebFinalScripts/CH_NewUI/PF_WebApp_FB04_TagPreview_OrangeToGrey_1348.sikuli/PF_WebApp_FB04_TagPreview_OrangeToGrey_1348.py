from sikuli import *
import PF_common
reload(PF_common)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1348"
    
def PF_WebApp_FB04_TagPreview_OrangeToGrey_1348(log_file):
    
    
    tag_preview_orange=("tag_preview_orange.png")
    tag_preview_tooltip=("tag_preview_tooltip.png")
    tag_preview_tooltipclick=("tag_preview_tooltipclick.png")
    tag_preview_selection=("tag_preview_selection.png")
    fix_icon=("fix_icon.png")

    tag_preview_grey=("tag_preview_grey.png")
    tag_preview_topbar=("tag_preview_topbar.png")
    

    PF_common.verify(log_file,tag_preview_orange)
    hover(tag_preview_orange)

    PF_common.verify(log_file,tag_preview_tooltip)
    click(tag_preview_tooltipclick)

    PF_common.verify(log_file,tag_preview_topbar)
 
    PF_common.verify(log_file,tag_preview_selection)
    
    PF_common.verify(log_file,fix_icon)
    click(fix_icon)
    
    PF_common.verify(log_file,tag_preview_grey)


#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
        PF_WebApp_FB04_TagPreview_OrangeToGrey_1348(log_file)
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


