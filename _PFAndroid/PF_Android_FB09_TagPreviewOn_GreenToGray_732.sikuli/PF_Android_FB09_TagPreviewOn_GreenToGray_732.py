import PF_Android_common
reload(PF_Android_common)
from sikuli import *

test_case_id="732"

def PF_Android_FB09_TagPreviewOn_GreenToGray_732(log_file):
    ProssAndCons =("Pros.png")
    Less=("Less.png")
    Fixes =("1407935909677.png") 

    Gray=("1407935944065.png")
    Green=("1407935890605.png")
    Click=("FB09_On.png")
    Clicked=("FB09_Off.png")
    TopBar=("1407935900580.png")

    sleep(3)
    PF_Android_common.locateItem (log_file,Green)
    click(Green)
    PF_Android_common.verify (log_file,ProssAndCons)
    click (ProssAndCons)       
    PF_Android_common.verify (log_file,TopBar)
    PF_Android_common.verify (log_file,Less)
    click(Less)

    click(Click)
    PF_Android_common.verify(log_file,Clicked)   
    PF_Android_common.verify(log_file,Fixes)
    click(Fixes)
    PF_Android_common.verify(log_file,Gray)

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
        
        PF_Android_FB09_TagPreviewOn_GreenToGray_732(log_file)
        
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)    
        
        