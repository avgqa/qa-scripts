import PF_common
reload(PF_common)


def TKM01(log_file): 
    eye=("1404721851413.png")
    hover_eye=("1404721862744.png")
    top_bar=("1404721889081.png")
    lk_page=("1404721903711.png")
   
    hover_orange=("1404723456475.png")
    hover_gray=("1404721936914.png")
    hover_green=("1404721982040.png")
    PF_common.verify(log_file, eye)
    hover(eye)
    PF_common.verify(log_file,hover_eye)
    if exists(Pattern(hover_orange).similar(0.99)):
        PF_common.verify_exactly(log_file, hover_orange)
        click(hover_eye)
    elif exists(Pattern(hover_gray).similar(0.99)):
        PF_common.verify_exactly(log_file, hover_gray)
        click(hover_eye)
    else:
        PF_common.verify_exactly(log_file, hover_green)
        click(hover_eye)
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,lk_page)
    
    
    
test_case_id="PF-1548"
#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)
        
        PF_common.InstallExtension(log_file)        
        PF_common.LinkedInLogIn(log_file)
        
        TKM01(log_file)
        PF_common.PassCase(log_file, test_case_id)
        
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
