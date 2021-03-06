from sikuli import *
import PF_common
reload(PF_common)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1377"

    
def PF_WebApp_FB02_FaceMatchingOn_GreyToGreen_1377(log_file):
   
    FaceMatchingOn_grey=("FaceMatchingOn_grey.png")
    FaceMatchingOn_hover=("FaceMatchingOn_hover.png")
    top_bar=("top_bar.png")
    FaceMatchingOn_settings=("FaceMatchingOn_settings.png")
    FaceMatchingOn_Changes=("FaceMatchingOn_Changes.png")
    
    FaceMatchingOn_NoOne=("FaceMatchingOn_NoOne.png")
    
    fix_icon=("fix_icon.png")
    FaceMatchingOff_green=("FaceMatchingOff_green.png")
    
 
    mouseMove(Location(1000,120))
    
    PF_common.verify(log_file,FaceMatchingOn_grey)
    hover(FaceMatchingOn_grey)
    sleep(1)
    PF_common.verify(log_file,FaceMatchingOn_hover)
    sleep(1)
    click(Pattern(FaceMatchingOn_hover).similar(0.50).targetOffset(0,-5))
   
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,FaceMatchingOn_settings)
    sleep(1)
    click(FaceMatchingOn_settings)
    sleep(1)
    click(FaceMatchingOn_Changes)

    PF_common.verify(log_file,FaceMatchingOn_NoOne)
    click(fix_icon)
    PF_common.verify(log_file,FaceMatchingOff_green)


#Function_call
if __name__ == "__main__":  
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
        PF_WebApp_FB02_FaceMatchingOn_GreyToGreen_1377(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)


