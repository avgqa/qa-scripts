import PF_common_FF as PF_common
reload(PF_common)



    
def PF_WebApp_FB04_TagPreview_GreyToGreen_FF1351 (log_file):

    
    tag_preview_selection=("disabled.png")
    fix_icon=("Fixes.png")
    tag_preview_grey=("grey-1.png")
    tag_previw_grey_tooltip=("grey_hover.png")
    tag_preview_choice=("choice.png")
    tag_preview_choiceclick=("enabled.png")
    tag_preview_green=("Green.png")
    tag_preview_topbar=("Top_bar.png")

    

    #verify the above images 
    #print str(fix_icon)

    PF_common.locate_item_page_by_page(log_file,tag_preview_grey)    
    PF_common.verify(log_file,tag_preview_grey)
    hover(tag_preview_grey)

    PF_common.verify(log_file,tag_previw_grey_tooltip)
    mouseMove(Location(1000,120))    
    click(tag_preview_grey)
    sleep(5)

    PF_common.verify(log_file,tag_preview_topbar)

    PF_common.verify(log_file,tag_preview_selection)
    sleep(1)
    PF_common.verify(log_file,tag_preview_selection)
    click(tag_preview_selection)

    PF_common.verify(log_file,tag_preview_choice)
    click(tag_preview_choiceclick)
    sleep(3)
    click(fix_icon)

    PF_common.verify(log_file,tag_preview_green)
    
    

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1351"


#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
      

        PF_WebApp_FB04_TagPreview_GreyToGreen_FF1351 (log_file)

        PF_common.PassCase(log_file, test_case_id)
 
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)


