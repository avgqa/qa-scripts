import PF_Android_common
reload(PF_Android_common)
from sikuli import *




def  PF_Android_FB07_RemoveOldApps_OrangeToGreen_725 ():
    
    Orange = ("1394021665590.png")
    More =("1394021677017.png")
    Less=("1394021687122.png")
    Percentage=("1394021694327.png")
    TopBar =("1394021701297.png")
    Fixes =("1394021707915.png") 
    Text = ("1394021732054.png")
    Green =("1394021753599.png")

    
    PF_Android_common.locateItem(log_file,Orange)
    PF_Android_common.verify (log_file,Orange)
    click (Orange)
    sleep(2)

    PF_Android_common.verify (log_file,More)
    sleep(1)
    click (More)

    PF_Android_common.verify (log_file,TopBar)

    PF_Android_common.verify (log_file,Less)
    sleep(1)
    click(Less)

    PF_Android_common.verify (log_file,Percentage)

    PF_Android_common.verify(log_file,Text)  
  
    PF_Android_common.verify(log_file,Fixes)
    click(Fixes)
    sleep(2)
    PF_Android_common.verify(log_file,Green)


test_case_id="PF-1994"


if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_Android_common.create_log_folder(test_case_script_name,test_case_id)
        
        PF_Android_common.AppOpen (log_file)
        PF_Android_common.FB_logIn(log_file)
        
        PF_Android_FB07_RemoveOldApps_OrangeToGreen_725 ()       
        
  
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)