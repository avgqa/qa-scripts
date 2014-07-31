import PF_common_FF as PF_common
reload(PF_common)




def PF_WebApp_FB05_App_Access_On_OrangeToGreen_1342(log_file):
    
    
    apps_access_orange=("orange.png")
    apps_access_orange_mouseover=("orange_hover.png")
    top_bar=("top_bar.png")
    fixes_icon=("fixes.png")
    settings=("settings.png")
    apps_access_gray=("gray.png")
       

    #verify the above images 
    #print str(top_bar)
    PF_common.locate_item_page_by_page(log_file,apps_access_orange)
    PF_common.verify(log_file,apps_access_orange)
    hover(apps_access_orange)

    PF_common.verify(log_file,apps_access_orange_mouseover)
    mouseMove(Location(1000,120))
    click(apps_access_orange)    
    sleep(2)
    
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,settings)    

    click(fixes_icon)
    sleep(2)
    PF_common.verify(log_file,apps_access_gray)


PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1342"        
#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
        PF_WebApp_FB05_App_Access_On_OrangeToGreen_1342(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)