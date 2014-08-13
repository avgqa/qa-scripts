import PF_Android_common
reload(PF_Android_common)
from sikuli import *




def  PF_Android_FB07_RemoveOldApps_OrangeToGreen_725 (log_file):
    
    Orange = ("1407932287594.png")
    More =("Pros.png")
    Less=("Less.png")

    TopBar =("1407932310484.png")
    Fixes =("1407932316991.png") 
    Text = ("Fb07_page.png")
    Green =("1407932340198.png")

    
    PF_Android_common.locateItem(log_file,Orange)
    PF_Android_common.verify (log_file,Orange)
    click (Orange)
    PF_Android_common.verify (log_file,More)
    click (More)
    PF_Android_common.verify (log_file,TopBar)
    PF_Android_common.verify (log_file,Less)
    click(Less)

    PF_Android_common.verify(log_file,Text)  
    PF_Android_common.verify(log_file,Fixes)
    click(Fixes)
    PF_Android_common.verify(log_file,Green)


test_case_id="PF-725"


if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_Android_common.create_log_folder(test_case_script_name,test_case_id)
        
        PF_Android_common.AppOpen (log_file)
        PF_Android_common.FB_logIn(log_file)
        
        PF_Android_FB07_RemoveOldApps_OrangeToGreen_725 (log_file)       
        
  
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)