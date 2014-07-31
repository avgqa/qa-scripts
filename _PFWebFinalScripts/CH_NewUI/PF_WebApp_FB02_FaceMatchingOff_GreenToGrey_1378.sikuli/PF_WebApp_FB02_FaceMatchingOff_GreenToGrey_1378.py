from sikuli import *
import PF_common
reload(PF_common)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1378"
    
def PF_WebApp_FB02_FaceMatchingOff_GreenToGrey_1378(log_file):
    
    face_matching_off_green=("face_matching_off_green.png")
    face_matching_off_hover=("face_matching_off_hover.png")
    
    face_matching_off=("face_matching_off.png")
    top_bar=("top_bar.png")
    none_click=("none_click.png")
    
    none_hihglited=("none_hihglited.png")
    friends_click=("1400759914976.png")
    fixes_icon=("fixes_icon.png")
    face_matching_on_grey=("face_matching_on_grey.png")

    
    mouseMove(Location(1000,120))
    
    PF_common.verify(log_file,face_matching_off_green)
    sleep(1)
    hover(face_matching_off_green)
    PF_common.verify(log_file,face_matching_off_hover)
    click(face_matching_off)

    PF_common.verify(log_file,top_bar)
    sleep(1)
    click(none_click)

    sleep(3)
    click(friends_click)
    sleep(3)
    click(fixes_icon)

    PF_common.verify(log_file,face_matching_on_grey)

#Function_call
if __name__ == "__main__":
    log_file = ""
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