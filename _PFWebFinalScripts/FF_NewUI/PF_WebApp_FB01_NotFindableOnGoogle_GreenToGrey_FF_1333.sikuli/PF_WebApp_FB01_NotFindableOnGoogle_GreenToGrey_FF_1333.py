import PF_common_FF as PF_common
reload(PF_common)



    
def PF_WebApp_FB01_NotFindableOnGoogle_GreenToGrey_FF1333(log_file):
    
    
    not_findable_on_google_selection=("1397117471782.png")
    
    not_findable_on_google_checkbox=("1397117479256.png")
    
    fix_icon=("1386167059528.png")

    not_findable_on_google_grey=("1400241967433.png")
    not_findable_on_google_grey_tooltip=("1389608848128.png")
    not_findable_on_google_green=("1400245107042.png")
    not_findable_on_google_tooltip=("1389608625303.png")
    not_findable_on_google_tooltipclick=("1389608639369.png")
    not_findable_on_google_topbar=("1391002661583.png")

    

    #verify the above images 
    #print str(fix_icon)

    
    PF_common.verify(log_file,not_findable_on_google_green)

    sleep(1)
    hover(not_findable_on_google_green)
    PF_common.verify(log_file,not_findable_on_google_tooltip)
    mouseMove(Location(1000,120))
    click(not_findable_on_google_green)


    PF_common.verify(log_file,not_findable_on_google_topbar)

    PF_common.verify(log_file,not_findable_on_google_selection)
    click(not_findable_on_google_checkbox)
    sleep(3)
    click(fix_icon)


    PF_common.verify(log_file,not_findable_on_google_grey)

    
PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1333"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        

        PF_WebApp_FB01_NotFindableOnGoogle_GreenToGrey_FF1333(log_file)



        PF_common.PassCase(log_file, test_case_id)

    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)