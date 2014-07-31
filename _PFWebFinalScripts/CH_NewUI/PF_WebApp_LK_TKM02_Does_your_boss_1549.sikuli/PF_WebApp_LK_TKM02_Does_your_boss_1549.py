import PF_common
reload(PF_common)



#Function declaration:
def your_boss(log_file):  
    your_boss_know = ("1404724660183.png")
    your_boss_know_hover = ("1404724668699.png")
    hover_orange = ("1404724696079.png")
    hover_gray=("1404724830322.png")
    hover_green=("1404724875799.png")
    lk_page = ("1404724738309.png")
    top_bar = ("1404724731894.png")
    
    PF_common.verify(log_file, your_boss_know)
    hover(your_boss_know)
    PF_common.verify(log_file,your_boss_know_hover)
    if exists(Pattern(hover_orange).similar(0.99)):
        PF_common.verify_exactly(log_file, hover_orange)
        click(your_boss_know_hover)
    elif exists(Pattern(hover_gray).similar(0.99)):
        PF_common.verify_exactly(log_file, hover_gray)
        click(your_boss_know_hover)
    else:
        PF_common.verify_exactly(log_file, hover_green)
        click(your_boss_know_hover)
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,lk_page)
    
test_case_id="PF-1549"    
#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)  
        
        PF_common.InstallExtension(log_file)
        PF_common.LinkedInLogIn(log_file)
        
        your_boss(log_file)
        PF_common.PassCase(log_file, test_case_id)
    
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)