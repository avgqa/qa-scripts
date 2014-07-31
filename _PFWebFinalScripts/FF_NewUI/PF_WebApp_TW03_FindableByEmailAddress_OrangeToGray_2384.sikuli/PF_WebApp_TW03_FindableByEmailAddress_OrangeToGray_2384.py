import PF_common_FF as PF_common
reload(PF_common)

def PF_WebApp_TW03_FindableByEmailAddress_OrangeToGray_2384(log_file):
    Findable_orange=("1400848440727.png")
    Findable_orange_hover=("1400848473055.png")
    top_bar=("1400848490238.png")
    Findable_settings=("1400848530284.png")
    fix_icon=("1400833112992.png")
    Findable_gray=("1400848569838.png")



    PF_common.locate_item_page_by_page(log_file,Findable_orange)
    PF_common.verify(log_file,Findable_orange)
    hover(Findable_orange)

    PF_common.verify(log_file,Findable_orange_hover)
    mouseMove(Location(1000,120))
    click(Findable_orange)    
    sleep(2)
    
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,Findable_settings)    

    click(fix_icon)
    sleep(2)
    PF_common.verify(log_file,Findable_gray)
         
    
PrivacyFix_link = PF_common._PF_link
test_case_id="PF-2384"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.TwitterLogIn(log_file)
        
        PF_WebApp_TW03_FindableByEmailAddress_OrangeToGray_2384(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)