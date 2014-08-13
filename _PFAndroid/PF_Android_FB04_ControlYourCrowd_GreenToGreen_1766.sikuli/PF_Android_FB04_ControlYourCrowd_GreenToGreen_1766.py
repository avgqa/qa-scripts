import PF_Android_common
reload(PF_Android_common)
from sikuli import *


def PF_Android_FB04_ControlYourCrowd_GreenToGreen_1766 (log_file):
    FB_04_Green=("green.png")

    TopBar=("1407915908425.png")
    SaveList=("FB04_saveButton.png")
    SecondPage=("1407916479447.png")
    Back=("1407916026960.png")
    Fixes=("1407915937182.png")
    loading=("FB04_load.png")
    PF_Android_common.locateItem(log_file,FB_04_Green)
    PF_Android_common.verify (log_file,FB_04_Green)
    click(FB_04_Green)

    while exists(loading):
        sleep(5)
    PF_Android_common.verify (log_file,TopBar)
    PF_Android_common.verify (log_file,SaveList)
    click(SaveList)
    sleep(10)
    PF_Android_common.verify (log_file,SecondPage)
    click(Back)     
    while exists(loading):
        sleep(5)
    PF_Android_common.verify (log_file,TopBar)  
    PF_Android_common.verify (log_file,SaveList)
    click(SaveList)
    sleep(10)
    PF_Android_common.verify (log_file,SecondPage)
    PF_Android_common.verify (log_file,Fixes)
    click(Fixes)
    PF_Android_common.verify (log_file,FB_04_Green)


    


test_case_id="PF-1766"


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
        PF_Android_FB04_ControlYourCrowd_GreenToGreen_1766 (log_file)
       
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)    