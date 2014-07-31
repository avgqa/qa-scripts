import PF_common_FF as PF_common
reload(PF_common)

#variables
PrivacyFix_link = PF_common._PF_link
test_case_id="PF-255"

def PF_WebApp_FB07_CrowdControl_OrangeToGreen_FF_255(log_file):
    
    orange=("orange.png")
    hover_orange=("orange_hover.png")
    okay=(Pattern("okay.png").similar(0.91))
    crowdcontrol=("top_bar.png")
    
    
    fixes=("fixes.png")
    green=("green.png")
    hover_green=("green_hover.png")

    
    
    PF_common.locate_item_page_by_page(log_file,orange)
    PF_common.verify(log_file,orange)
    hover(orange)

    PF_common.verify(log_file,hover_orange)
    mouseMove(Location(1000,120))
    click(orange)    
    sleep(5)

    while exists(okay):
        click(okay)
        sleep(5)
                
        
    PF_common.verify(log_file,crowdcontrol)
    click(fixes)
    PF_common.verify(log_file,green)
    hover(green)
    PF_common.verify(log_file,hover_green)  
    

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)  
        

        PF_WebApp_FB07_CrowdControl_OrangeToGreen_FF_255(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
        
 