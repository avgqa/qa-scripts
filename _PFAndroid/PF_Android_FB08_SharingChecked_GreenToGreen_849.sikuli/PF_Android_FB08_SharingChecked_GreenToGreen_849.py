import PF_Android_common
reload(PF_Android_common)
from sikuli import *

test_case_id="PF-849"

def PF_Android_FB08_SharingChecked_GreenToGreen_849():
    Fixes =("1407935400604.png") 

    TopBar=("1407935379086.png")
    Page=("1407935414387.png")
    Green=("1407935358003.png")
    PF_Android_common.locateItem(log_file,Green)
    click(Green)
    PF_Android_common.verify (log_file,TopBar)
    PF_Android_common.verify(log_file,Page)
    click(Fixes)
    PF_Android_common.verify(log_file,Green)




if __name__ == "__main__":
    
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_Android_common.create_log_folder(test_case_script_name,test_case_id)

        PF_Android_common.AppOpen (log_file)
        sleep(5)
        PF_Android_common.FB_logIn(log_file)
        sleep(5)
        
        PF_Android_FB08_SharingChecked_GreenToGreen_849()
        
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)  