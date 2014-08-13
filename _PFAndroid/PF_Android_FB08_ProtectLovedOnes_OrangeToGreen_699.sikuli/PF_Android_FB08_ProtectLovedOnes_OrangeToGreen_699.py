import PF_Android_common
reload(PF_Android_common)
from sikuli import *

test_case_id="PF-699"

def PF_Android_FB08_ProtectLovedOnes_OrangeToGreen_699(log_file):
    Fixes =("1407935319317.png") 
    Orange=("1407935283799.png")
    TopBar=("1407935308875.png")
    Page=("1407935422569.png")
    Green=("1407935331649.png")
    
    PF_Android_common.locateItem(log_file,Orange)
    click(Orange)
    PF_Android_common.verify (log_file,TopBar)
    PF_Android_common.verify(log_file,Page)
    click(Fixes)
    PF_Android_common.verify(log_file,Green)




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
        
        PF_Android_FB08_ProtectLovedOnes_OrangeToGreen_699(log_file)
        
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)  