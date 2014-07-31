import PF_common
reload(PF_common)

    
def PF_WebApp_GL_InGoogleAds_MostPrivateToAllow_1350(log_file):
    allowed=("gray.png")
    green_hover=("1387204934792.png")
    green_click=("green_click.png")
    top_bar=("top_bar.png")
    fix_button=("Fixes.png")
    turn_on=("check-box.png")
    check_box_checked=("checked.png")
    save_button=("save.png")
    most_private=("green.png")


    PF_common.verify(log_file,most_private)
    hover(most_private)
    PF_common.verify(log_file, green_hover)
    sleep(1)
    click(green_click)
    sleep(5)
    PF_common.verify(log_file, top_bar)  
    PF_common.verify(log_file,turn_on)
    click(turn_on)
    sleep(1)
    click(save_button)
    sleep(2)
    PF_common.verify(log_file,check_box_checked)    
    click(fix_button)
    sleep(5)
    PF_common.verify(log_file, allowed)
    
test_case_id="PF-1350"
#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)
        PF_common.GoogleLogin(log_file)
        

        PF_WebApp_GL_InGoogleAds_MostPrivateToAllow_1350(log_file)

        PF_common.PassCase(log_file, test_case_id)

     
               
    except FindFailed, f:
        print "before f"
        msg =  "Find Failed Exception: %s " % f

        PF_common.write_log(log_file,msg)  
        print "after f"
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        print "exception"
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)


         