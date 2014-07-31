import PF_common_FF
reload(PF_common_FF)


   
def PF_WebApp_FB01_FindableOnGoogle_GreyToGreen_FF1331(log_file):
    
    findable_on_google_selection=("1397117036626.png")
    
    findable_on_google_checkbox=("1397117240567.png")
    
    fix_icon=("1387460386340.png")
    findable_on_google_grey=("1400241967433.png")
 #   findable_on_google_tooltipclick=("1400241985715.png")
    findable_on_google_tooltip=("1390307607481.png")
    findable_on_google_choice=("1397117076125.png")
    
    findable_on_google_choiceclick=("1397117082207.png")
    
    findable_on_google_green=("1400244886104.png")
    findable_on_google_topbar=("1391002644977.png")


    PF_common_FF.locate_item_page_by_page(log_file,findable_on_google_grey)
    PF_common_FF.verify(log_file,findable_on_google_grey)
    hover(findable_on_google_grey)
    
    PF_common_FF.verify(log_file,findable_on_google_tooltip)
    mouseMove(Location(1000,120))
    click(findable_on_google_grey)


    PF_common_FF.verify(log_file,findable_on_google_topbar)


    PF_common_FF.verify(log_file,findable_on_google_selection)
    click(findable_on_google_checkbox)

    PF_common_FF.verify(log_file,findable_on_google_choice)
    click(findable_on_google_choiceclick)
    sleep(3)
    click(fix_icon)
    sleep(3)
    PF_common_FF.verify(log_file,findable_on_google_green)

       
    
    
PrivacyFix_link = PF_common_FF._PF_link
test_case_id="PF-1331"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common_FF.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common_FF.InstallExtension(log_file)
        PF_common_FF.FacebookLogin(log_file)
        

        PF_WebApp_FB01_FindableOnGoogle_GreyToGreen_FF1331(log_file)

        PF_common_FF.PassCase(log_file, test_case_id)

     
               
    except FindFailed, f:
        print "before f"
        msg =  "Find Failed Exception: %s " % f

        PF_common_FF.write_log(log_file,msg)  
        print "after f"
        PF_common_FF.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        print "exception"
        PF_common_FF.write_log(log_file,msg)        
        PF_common_FF.FailTestCase(log_file, test_case_id)



