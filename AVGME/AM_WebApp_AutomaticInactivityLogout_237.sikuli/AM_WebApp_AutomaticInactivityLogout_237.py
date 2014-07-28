import time
import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-237"

def AM_WebApp_AutomaticInactivityLogout_237(log_file):

    Settings=("1406016963345.png")

 
    Menu=("1406188430641.png")
    DropDown=("1406188462499.png")
    DropdownList=("1406188517598.png")
    TwoMinutes=("1406189870150.png")
    ChangeBlue=("1406189004633.png")
    Logout=("1406194261082.png")
    Never=("1406194321701.png")

    AM_common.AppOpen(log_file)
    wait(4)
    if exists(Settings):
        click( Settings)
    AM_common.verify(log_file,Menu)
    AM_common.verify(log_file,DropDown)   
    click(DropDown)
    AM_common.verify_continue(log_file,DropdownList)
    click(TwoMinutes)
    AM_common.verify(log_file,ChangeBlue)
    click(ChangeBlue)
    wait(1)
    click("1406193619387.png")
    
    t0 = time.time()
    wait(200)
    
    AM_common.AppOpen(log_file)
    wait(4)
    if exists(Settings):
        click( Settings)
    AM_common.verify(log_file,Logout)   
    
    print time.time() - t0, "seconds process time"
    AM_common.LoginTOApp(log_file)
    AM_common.AppOpen(log_file)
    wait(4)
    if exists(Settings):
        click( Settings)
    AM_common.verify(log_file,Menu)
    AM_common.verify(log_file,DropDown)   
    click(DropDown)
    #AM_common.verify_continue(log_file,DropdownList)
    click(Never)
    AM_common.verify(log_file,ChangeBlue)
    click(ChangeBlue)

        
    


    
    


    
    
    
        
    
    
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=AM_common.create_log_folder(test_case_script_name, test_case_id)

        AM_common.InstallExtention(log_file)
        AM_common.LoginTOApp(log_file)


        
        AM_WebApp_AutomaticInactivityLogout_237(log_file)

        
        AM_common.PassCase(log_file, test_case_id)

    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        AM_common.write_log(log_file,msg)        
        AM_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        print "exception"
        AM_common.write_log(log_file,msg)        
        AM_common.FailTestCase(log_file, test_case_id)