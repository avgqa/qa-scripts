import PF_common_FF as PF_common
reload(PF_common)

def PF_WebApp_TW01_PhotosTaggable_GreyToGreen_2377(log_file):

    PhotosTaggable_grey=("1400839500359.png")
    PhotosTaggable_hover=("1400839535542.png")
    top_bar=("1400839569740.png")
    PhotosTaggable_settings=("1400839637281.png")
    PhotosTaggable_Changes=("1400839707964.png")
    save=("1400839756774.png")
    save_account=("1400840289267.png")
        
    PhotosTaggable_DoNot=("1400840572053.png")
    fix_icon=("1400839874197.png")
    PhotosNotTaggable_green=("1400839963588.png")

    PF_common.locate_item_page_by_page(log_file,PhotosTaggable_grey)
    PF_common.verify(log_file,PhotosTaggable_grey)
    hover(PhotosTaggable_grey)


    PF_common.verify(log_file,PhotosTaggable_hover)
    mouseMove(Location(1000,120))
    click(PhotosTaggable_grey)
   
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,PhotosTaggable_settings)
    sleep(1)
    click(Pattern(PhotosTaggable_Changes).similar(0.95))
    sleep(3)
    PF_common.locate_item_page_by_page(log_file,save)
    click(save)
    sleep(2)
    click(save_account)
    type("US!pf.avg")
    type(Key.ENTER)
    sleep(5)

    PF_common.verify(log_file,PhotosTaggable_DoNot)
    click(fix_icon)
    mouseMove(Location(1000,120))
    PF_common.verify(log_file,PhotosNotTaggable_green)

PrivacyFix_link = PF_common._PF_link
test_case_id="PF-2377"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.TwitterLogIn(log_file)
        
        PF_WebApp_TW01_PhotosTaggable_GreyToGreen_2377(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)