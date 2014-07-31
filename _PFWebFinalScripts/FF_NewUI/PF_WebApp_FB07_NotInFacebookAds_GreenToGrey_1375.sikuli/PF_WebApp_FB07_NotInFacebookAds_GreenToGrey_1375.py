import PF_common_FF as PF_common
reload(PF_common)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1375"
    

def PF_WebApp_FB06_NotInFacebookAds_GreenToGrey_1375(log_file):

    
    facebook_ads_green=("green.png")
    facebook_ads_green_hover=("green_hover.png")

    top_bar=("top_bar.png")
    settings_window=("settings.png")
    friends=("friends.png")
    save_changes=("save.png")
    fix_icon=("Fixes.png")
    
    in_facebook_ads_grey=("gray.png")

    PF_common.locate_item_page_by_page(log_file,facebook_ads_green)
    PF_common.verify(log_file,facebook_ads_green)
    hover(facebook_ads_green)

    PF_common.verify(log_file,facebook_ads_green_hover)
    mouseMove(Location(1000,120))
    click(facebook_ads_green)    
    sleep(2)
    
    PF_common.verify(log_file,top_bar)
    click(settings_window)
    sleep(1)
    click(friends)
    sleep(1)
    click(save_changes)
    sleep(1)
    click(fix_icon)      

  
    PF_common.verify(log_file, in_facebook_ads_grey)

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        
        PF_WebApp_FB06_NotInFacebookAds_GreenToGrey_1375(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)