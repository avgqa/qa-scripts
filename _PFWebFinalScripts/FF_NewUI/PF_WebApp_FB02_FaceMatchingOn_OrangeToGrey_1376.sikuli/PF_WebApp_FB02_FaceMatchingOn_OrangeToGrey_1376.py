import PF_common_FF as PF_common
reload(PF_common)
    
def PF_WebApp_FB02_FaceMatchingOn_OrangeToGrey_1376(log_file):
    
    FaceMatchingOn_orange=("orange.png")
    FaceMatchingOn_hover=("orange_hover.png")
    top_bar=("top_bar.png")
    FaceMatchingOn_settings=("settings.png")    
    fix_icon=("Fixes.png")
    FaceMatchingOn_grey=("gray.png")
    
    PF_common.locate_item_page_by_page(log_file,FaceMatchingOn_orange)
    PF_common.verify(log_file,FaceMatchingOn_orange)
    hover(FaceMatchingOn_orange)

    PF_common.verify(log_file,FaceMatchingOn_hover)
    mouseMove(Location(1000,120))
    click(FaceMatchingOn_orange)    
    sleep(2)
    
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,FaceMatchingOn_settings)    

    click(fix_icon)
    sleep(2)
    PF_common.verify(log_file,FaceMatchingOn_grey)
         
    
PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1376"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
        PF_WebApp_FB02_FaceMatchingOn_OrangeToGrey_1376(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)