import PF_common_FF as PF_common
reload(PF_common)

def PF_WebApp_TW03_NotFindableByEmailAddress_GreenToGray_2387(log_file):

    Findable_green=("1400849978839.png")
    Findable_green_hover=("1400850001947.png")
    top_bar=("1400850022603.png")
    Findable_settings=("1400850069843.png")
    Findable_Changes=("1400850093315.png")
    save=("1400843325516.png")
    save_account=("1400844282826.png")
    Findable_select=("1400850143169.png")
    fix_icon=("1400843438662.png")
    Findable_gray=("1400850174843.png")

    
    PF_common.locate_item_page_by_page(log_file,Findable_green)
    PF_common.verify(log_file,Findable_green)
    hover(Findable_green)


    PF_common.verify(log_file,Findable_green_hover)
    mouseMove(Location(1000,120))
    click(Findable_green)
   
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

    PF_common.verify(log_file,Findable_select)
    click(fix_icon)
    mouseMove(Location(1000,120))
    PF_common.verify(log_file,Findable_gray)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-2387"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.TwitterLogIn(log_file)
        
        PF_WebApp_TW03_NotFindableByEmailAddress_GreenToGray_2387(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)