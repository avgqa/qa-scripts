import PF_common_FF as PF_common
reload(PF_common)


    
def PF_WebApp_FB05_App_Access_On_GreenToGrey_1344(log_file):
    
    apps_access_gray=("gray.png")
    app_access_green=("green-1.png")
    apps_access_green_mouseover=("green_hover.png")

    top_bar=("top_bar.png")
    fixes_icon=("fixes.png")
    checkbox=("checkbox.png")
    
    save=("save.png")

  
    


    #verify the above images 
    #print str(top_bar)
    PF_common.locate_item_page_by_page(log_file,app_access_green)
    PF_common.verify(log_file,app_access_green)
    hover(app_access_green)

    PF_common.verify(log_file,apps_access_green_mouseover)
    mouseMove(Location(1000,120))
    click(app_access_green)    
    sleep(2)

    PF_common.verify(log_file, top_bar)
    i=0
    while exists(checkbox) and i<3:
        click(checkbox)
        sleep(5)
        i+=1
    click(save)
    sleep(2)
    click(fixes_icon)
    sleep(1) 
    
    PF_common.verify(log_file,apps_access_gray)
    
    
#Variables:
PrivacyFix_link = PF_common._PF_link
test_case_id="PF-1344"

#Function_call
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)

        PF_common.InstallExtension(log_file)
        PF_common.FacebookLogin(log_file)
        

        PF_WebApp_FB05_App_Access_On_GreenToGrey_1344(log_file)
        PF_common.PassCase(log_file, test_case_id) 
        
                         
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)  


