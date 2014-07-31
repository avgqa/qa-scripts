import PF_common_FF as PF_common
reload(PF_common)
    
    
def PF_WebApp_FB02_FaceMatchingOff_GreenToGrey_1378(log_file):
    
    face_matching_off_green=("green.png")
    face_matching_off_hover=("green_hover.png")
    
    #face_matching_off=("1387802685324.png")
    top_bar=("top_bar.png")
    none_click=("noOne_checked.png")
    
    friends_selected=("friends_sected.png")

    fixes_icon=("Fixes.png")
    face_matching_on_grey=("gray.png")

    
    PF_common.locate_item_page_by_page(log_file,face_matching_off_green)
    PF_common.verify(log_file,face_matching_off_green)
    hover(face_matching_off_green)


    PF_common.verify(log_file,face_matching_off_hover)
    mouseMove(Location(1000,120))
    click(face_matching_off_green)

    PF_common.verify(log_file,top_bar)
    sleep(1)
    click(none_click)
    type(Key.DOWN)
    sleep(1)
    type(" ")


    PF_common.verify(log_file,friends_selected)    
    click(fixes_icon)
    mouseMove(Location(1000,120))

    PF_common.verify(log_file,face_matching_on_grey)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1378"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
        PF_WebApp_FB02_FaceMatchingOff_GreenToGrey_1378(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)