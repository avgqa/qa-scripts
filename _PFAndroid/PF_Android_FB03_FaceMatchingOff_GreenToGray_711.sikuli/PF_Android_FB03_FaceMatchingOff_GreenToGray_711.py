import PF_Android_common
reload(PF_Android_common)
from sikuli import *


def PF_Android_FB03_FaceMatchingOff_GreenToGray_711 (log_file):
    FB_03_Green=("green.png")
    ProssAndCons=("more.png")
    Less=("less.png")
    TopBar=("topbar.png")    
    Fixes=("back.png")
    Friends=("friends.png")
    FriendsChecked=("friendsChecked.png")
    FB_03_Gray=("grey.png")
    
    
    
    PF_Android_common.LocateOnTop(log_file,FB_03_Green)
    PF_Android_common.verify (log_file,FB_03_Green)
    click(FB_03_Green)
    PF_Android_common.verify (log_file,ProssAndCons)
    click(ProssAndCons)
    PF_Android_common.verify (log_file,TopBar)
    PF_Android_common.verify (log_file,Less)
    click(Less)
    PF_Android_common.verify (log_file,Friends)
    click (Friends)            
    PF_Android_common.verify (log_file,FriendsChecked)
    PF_Android_common.verify (log_file,Fixes)
    click(Fixes)
    PF_Android_common.verify (log_file,FB_03_Gray)


    


test_case_id="PF-711"


if __name__ == "__main__":
    log_file=""       
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_Android_common.create_log_folder(test_case_script_name,test_case_id)

        PF_Android_common.AppOpen (log_file)
        PF_Android_common.FB_logIn(log_file)
        PF_Android_FB03_FaceMatchingOff_GreenToGray_711 (log_file)
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)    