import PF_Android_common
reload(PF_Android_common)
from sikuli import *

test_case_id="PF-1765"

def PF_Android_FB02_InFacebookAds_GrayToGreen_1765(log_file):
    ProssAndCons =("more-1.png")
    Less=("less-1.png")
    Fixes =("Fixes.png") 
    Percentage=("percent.png")
    Notification=("notification.png")
    Click=("click.png")
  
    noOneChecked=("noOne.png")
    
    TopBar=("Topbart.png")
    Gray=("gray.png")
    Green=("Green.png")

    PF_Android_common.locateItem(log_file,Gray)
    PF_Android_common.verify (log_file,Gray)
    click(Gray)
   # PF_Android_common.verify (log_file,Notification)
    PF_Android_common.verify (log_file,ProssAndCons)
    click (ProssAndCons)       
    PF_Android_common.verify (log_file,TopBar)
    PF_Android_common.verify (log_file,Less)
    click(Less)

    PF_Android_common.locateItem (log_file,Click)
    click (Click)
    PF_Android_common.verify(log_file,noOneChecked)
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
        PF_Android_common.FB_logIn(log_file)   
        PF_Android_FB02_InFacebookAds_GrayToGreen_1765(log_file)     
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)    
    