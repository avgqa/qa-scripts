import PF_Android_common
reload(PF_Android_common)
from sikuli import *


def PF_Android_FB07_AppsChecked_GreenToGreen_1781 (log_file):
    Green=("1407932382775.png")
    ProsAndCons=("ProsAndCons.png")
    Less=("Less.png")

    Page=("1407932405668.png")
    Fixes=("1407932393158.png")
    PF_Android_common.locateItem (log_file,Green)
    click(Green)
    PF_Android_common.verify (log_file,ProsAndCons)
    click(ProsAndCons)

    PF_Android_common.verify (log_file,Page)
    PF_Android_common.verify (log_file,Less)
    click(Less)
    PF_Android_common.verify (log_file,Fixes)
    click(Fixes)
    PF_Android_common.verify (log_file,Green)    




test_case_id="PF-1781"    

if __name__ == "__main__":
    log_file=""
    
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_Android_common.create_log_folder(test_case_script_name,test_case_id)

        PF_Android_common.AppOpen (log_file)
        PF_Android_common.FB_logIn(log_file)
        PF_Android_FB07_AppsChecked_GreenToGreen_1781 (log_file)
       
        
        
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)            