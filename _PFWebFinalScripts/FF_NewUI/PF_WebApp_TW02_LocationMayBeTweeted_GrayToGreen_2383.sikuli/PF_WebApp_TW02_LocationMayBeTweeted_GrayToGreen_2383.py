import PF_common_FF as PF_common
reload(PF_common)

def PF_WebApp_TW02_LocationMayBeTweeted_GrayToGreen_2383(log_file):

    Location_gray=("1400845816269.png")
    Location_gray_hover=("1400839535542.png")
    top_bar=("1400845895130.png")
    Location_settings=("1400845918937.png")
    Location_Changes=("1400845948342.png")
    save=("1400839756774.png")
    save_account=("1400840289267.png")
        
    Location_uncheck=("1400846017774.png")
    fix_icon=("1400839874197.png")
    Location_green=("1400846066919.png")

    PF_common.locate_item_page_by_page(log_file,Location_gray)
    PF_common.verify(log_file,Location_gray)
    hover(Location_gray)


    PF_common.verify(log_file,Location_gray_hover)
    mouseMove(Location(1000,120))
    click(Location_gray)
   
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

    PF_common.verify(log_file,Location_uncheck)
    click(fix_icon)
    mouseMove(Location(1000,120))
    PF_common.verify(log_file,Location_green)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-2383"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.TwitterLogIn(log_file)
        
        PF_WebApp_TW02_LocationMayBeTweeted_GrayToGreen_2383(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)