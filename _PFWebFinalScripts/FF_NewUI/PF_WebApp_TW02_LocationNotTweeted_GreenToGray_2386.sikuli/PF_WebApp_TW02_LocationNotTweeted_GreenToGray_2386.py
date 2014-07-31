import PF_common_FF as PF_common
reload(PF_common)

def PF_WebApp_TW02_LocationNotTweeted_GreenToGray_2386(log_file):

    Location_green=("1400846639482.png")
    Location_green_hover=("1400846657665.png")
    top_bar=("1400846677757.png")
    Location_settings=("1400846699360.png")
    Location_Changes=("1400846735792.png")
    save=("1400843325516.png")
    save_account=("1400844282826.png")
    Location_select=("1400846806242.png")
    fix_icon=("1400843438662.png")
    Location_gray=("1400846839616.png")

    
    PF_common.locate_item_page_by_page(log_file,Location_green)
    PF_common.verify(log_file,Location_green)
    hover(Location_green)


    PF_common.verify(log_file,Location_green_hover)
    mouseMove(Location(1000,120))
    click(Location_green)
   
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,Location_settings)
    sleep(1)
    click(Pattern(Location_Changes).similar(0.95))
    sleep(3)
    PF_common.locate_item_page_by_page(log_file,save)
    click(save)
    sleep(2)
    click(save_account)
    type("US!pf.avg")
    type(Key.ENTER)
    sleep(5)

    PF_common.verify(log_file,Location_select)
    click(fix_icon)
    mouseMove(Location(1000,120))
    PF_common.verify(log_file,Location_gray)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-2386"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.TwitterLogIn(log_file)
        
        PF_WebApp_TW02_LocationNotTweeted_GreenToGray_2386(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)