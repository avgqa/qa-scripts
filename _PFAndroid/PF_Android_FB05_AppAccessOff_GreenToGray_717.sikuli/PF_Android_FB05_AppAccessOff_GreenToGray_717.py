import PF_Android_common
reload(PF_Android_common)
from sikuli import *


def PF_Android_05_AppAccessOff_GreenToGray_717(log_file):
    
    Page=("topbar.png")
    Apps=("Fb05_apps.png")
    Percentage=("FB05_percentage.png")
    More=("FB05_pros.png")
    Add_info=("more.png")
    Less=("Fb05_less.png")

    Fixes=("1407921036752.png")
    Gray=("Grey.png")
    Uncheck=("Fb05_uncheck.png")

    Green=("1407921000208.png")
    Check1=("Fb05_check1.png")
    Check2=("Fb05_check2.png")
    PF_Android_common.locateItem(log_file, Green)
    PF_Android_common.verify(log_file, Green)
    click(Green)
    PF_Android_common.verify(log_file, Page)
    click(More)
    PF_Android_common.verify(log_file, Add_info)
    click(Less)
    PF_Android_common.verify(log_file, More)

    PF_Android_common.verify(log_file, Apps)
    click(Check1)
    sleep(2)
    click(Check2)
    PF_Android_common.verify(log_file, Uncheck)
    click(Fixes)
    PF_Android_common.verify(log_file, Gray)
       

test_case_id="PF-717"


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
        
        PF_Android_05_AppAccessOff_GreenToGray_717(log_file)
        
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)