import PF_common
reload(PF_common)


#Function declaration:
def your_competition(log_file):
#local variables declaration:  
    
    hover_orange=("1404725932566.png")
    hover_gray=("1404726030725.png")
    hover_green=("1404726069759.png")
    can_our_competition = ("1404725942954.png")
    can_our_competition_hover = ("1404725952912.png")
    top_bar = ("1404725977038.png")
    lk_page= ("1404726015066.png")
    
   
    PF_common.verify(log_file, can_our_competition)
    hover(can_our_competition)
    PF_common.verify(log_file, can_our_competition_hover)
    if exists(Pattern(hover_orange).similar(0.99)):
        PF_common.verify_exactly(log_file, hover_orange)
        click(can_our_competition_hover)
    elif exists(Pattern(hover_gray).similar(0.99)):
        PF_common.verify_exactly(log_file, hover_gray)
        click(can_our_competition_hover)
    else:
        PF_common.verify_exactly(log_file, hover_green)
        click(can_our_competition_hover)
    PF_common.verify(log_file,top_bar)
    PF_common.verify(log_file,lk_page)

test_case_id="PF-1551"    
#Function_call
if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_common.create_log_folder(test_case_script_name, test_case_id)    

        PF_common.InstallExtension(log_file)
        PF_common.LinkedInLogIn(log_file)
        
        your_competition(log_file)
        PF_common.PassCase(log_file, test_case_id)
    
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)