import PF_Android_common
reload(PF_Android_common)
from sikuli import *


def PF_Android_06_CloseOldSessions_OrangeToGreen_722 (log_file):
    old_sessions_orange=("1407931556269.png")
    more=("Pros.png")
    less=("Less.png")
    top_bar=("1407931600675.png")
    active_sessions=("FB06_session.png")
    fixes=("1407931608107.png")
    old_sessions_green=("1407931652326.png")


    PF_Android_common.locateItem(log_file, old_sessions_orange)
    PF_Android_common.verify (log_file,old_sessions_orange)
    click (old_sessions_orange)   
    PF_Android_common.verify (log_file,more)
    click(more)
    PF_Android_common.verify (log_file,top_bar)
    PF_Android_common.verify (log_file,less)
    click(less)
    PF_Android_common.verify (log_file,active_sessions)
    click(fixes)
    PF_Android_common.verify (log_file,old_sessions_green)
    


test_case_id="PF-722"


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
        PF_Android_06_CloseOldSessions_OrangeToGreen_722 (log_file)
          
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)