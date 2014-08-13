import PF_Android_common
reload(PF_Android_common)
from sikuli import *

test_case_id="729"

def PF_Android_FB09_TagPreviewOff_GrayToGreen_729(log_file):
    ProssAndCons =("Pros.png")
    Less=("Less.png")
    Fixes =("1407935819816.png") 

    Gray=("1407935810698.png")
    Green=("1407935870426.png")
    Click=("FB09_On.png")
    Clicked=("FB09_Off.png")
    TopBar=("1407935835729.png")

    sleep(3)
    PF_Android_common.locateItem (log_file,Gray)
    click(Gray)
    PF_Android_common.verify (log_file,ProssAndCons)
    click (ProssAndCons)       
    PF_Android_common.verify (log_file,TopBar)
    PF_Android_common.verify (log_file,Less)
    click(Less)
    PF_Android_common.verify(log_file,Clicked)   
    click(Clicked)
    PF_Android_common.verify(log_file,Click)   
    PF_Android_common.verify(log_file,Fixes)
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
        
        PF_Android_FB09_TagPreviewOff_GrayToGreen_729(log_file)
        
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)    
        
        