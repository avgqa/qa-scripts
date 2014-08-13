import PF_Android_common
reload(PF_Android_common)
from sikuli import *
test_case_id="PF-1762"

def PF_Android_FB04_ControlYourCrowd_OrangeToGreen_1762 (log_file):
    FB_04_Orange=("orange.png")
    Percentage=("Fb04_percentage.png")
    TopBar=("FB04_topbar.png")
    Fixes=("FB04_fixes.png")
    FB_04_Green=("1407914989806.png")
    Ok=("Ok.png")
    PF_Android_common.locateItem(log_file,FB_04_Orange)
    PF_Android_common.verify (log_file,FB_04_Orange)
    click(FB_04_Orange)
    sleep(4)
    if exists(Ok):
        click(Ok)
        wait(2)
    if exists(Ok):
        click(Ok)
    PF_Android_common.verify (log_file,TopBar)
    PF_Android_common.verify (log_file,Fixes)
    click(Fixes)
    PF_Android_common.verify (log_file,FB_04_Green)
    

if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_Android_common.create_log_folder(test_case_script_name,test_case_id)

        PF_Android_common.AppOpen (log_file)
        sleep(5)
        PF_Android_common.FB_logIn(log_file)
        sleep(5)
        
        PF_Android_FB04_ControlYourCrowd_OrangeToGreen_1762 (log_file)
       
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)    