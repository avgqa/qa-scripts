import PF_common_FF as PF_common
reload(PF_common)


    
def PF_WebApp_FB04_TagPreview_GreenToGrey_FF271(log_file):
       
    tag_preview_selection=("enabled.png")
    fix_icon=("Fixes.png")
    tag_preview_grey=("grey-1.png")
    tag_preview_choice2=("choice.png")
    tag_preview_choice2click=("disabled.png")
    tag_preview_green=("Green-1.png")
    tag_preview_tooltip=("green_hover.png")
    tag_preview_topbar=("Top_bar.png")

    

    #verify the above images 
    #print str(fix_icon)

    PF_common.locate_item_page_by_page(log_file, tag_preview_green)   
    PF_common.verify(log_file,tag_preview_green)
    hover(tag_preview_green)

    PF_common.verify(log_file,tag_preview_tooltip)
    mouseMove(Location(1000,120))   
    click(tag_preview_green)
    sleep(2)
     
    PF_common.verify(log_file, tag_preview_topbar)

    PF_common.verify(log_file,tag_preview_selection)
    click(tag_preview_selection)

    PF_common.verify(log_file,tag_preview_choice2)
    click(tag_preview_choice2click)

    click(fix_icon)
    sleep(2)
    PF_common.verify(log_file,tag_preview_grey)


    

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-271"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
       

        PF_WebApp_FB04_TagPreview_GreenToGrey_FF271(log_file)

        PF_common.PassCase(log_file, test_case_id)
       
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)