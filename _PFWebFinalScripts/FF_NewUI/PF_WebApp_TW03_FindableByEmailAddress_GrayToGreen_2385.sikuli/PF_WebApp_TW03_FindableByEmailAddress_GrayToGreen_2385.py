import PF_common_FF as PF_common
reload(PF_common)

def PF_WebApp_TW03_FindableByEmailAddress_GrayToGreen_2385(log_file):

    Findable_gray=("1400849215246.png")
    Findable_gray_hover=("1400849235718.png")
    top_bar=("1400849254835.png")
    Findable_settings=("1400849279878.png")
    Findable_Changes=("1400849305722.png")
    save=("1400839756774.png")
    save_account=("1400840289267.png")
        
    Findable_uncheck=("1400849357407.png")
    fix_icon=("1400839874197.png")
    Findable_green=("1400849391311.png")

    PF_common.locate_item_page_by_page(log_file,Findable_gray)
    PF_common.verify(log_file,Findable_gray)
    hover(Findable_gray)


    PF_common.verify(log_file,Findable_gray_hover)
    mouseMove(Location(1000,120))
    click(Findable_gray)
   
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,Findable_settings)
    sleep(1)
    click(Pattern(Findable_Changes).similar(0.95))
    sleep(3)
    PF_common.locate_item_page_by_page(log_file,save)
    click(save)
    sleep(2)
    click(save_account)
    type("US!pf.avg")
    type(Key.ENTER)
    sleep(5)

    PF_common.verify(log_file,Findable_uncheck)
    click(fix_icon)
    mouseMove(Location(1000,120))
    PF_common.verify(log_file,Findable_green)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-2385"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.TwitterLogIn(log_file)
        
        PF_WebApp_TW03_FindableByEmailAddress_GrayToGreen_2385(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)