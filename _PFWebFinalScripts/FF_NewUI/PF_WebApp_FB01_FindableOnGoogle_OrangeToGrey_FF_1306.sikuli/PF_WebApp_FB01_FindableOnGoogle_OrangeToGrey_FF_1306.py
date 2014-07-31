import PF_common_FF as PF_common
reload(PF_common)


    
def PF_WebApp_FB01_FindableOnGoogle_OrangeToGrey_FF1306(log_file):
    
        
    findable_on_google_orange=("orange.png")
    findable_on_google_tooltip=("orange_hover.png")
    findable_on_google_selection=("settings.png")
    
    fix_icon=("Fixes.png")

    findable_on_google_grey=("gray.png")
    findable_on_google_topbar=("1391002554576.png")
    

    #verify the above images 
    #print str(fix_icon)
    PF_common.locate_item_page_by_page(log_file,findable_on_google_orange)
    PF_common.verify(log_file,findable_on_google_orange)
    hover(findable_on_google_orange)

    PF_common.verify(log_file,findable_on_google_tooltip)
    mouseMove(Location(1000,120))
    click(findable_on_google_orange)


    PF_common.verify(log_file,findable_on_google_topbar)
 
    PF_common.verify(log_file,findable_on_google_selection)
    
    PF_common.verify(log_file,fix_icon)
    click(fix_icon)

    
    PF_common.verify(log_file,findable_on_google_grey)
  
   
PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1306"


#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        PF_WebApp_FB01_FindableOnGoogle_OrangeToGrey_FF1306(log_file)
        PF_common.PassCase(log_file, test_case_id)

    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)


