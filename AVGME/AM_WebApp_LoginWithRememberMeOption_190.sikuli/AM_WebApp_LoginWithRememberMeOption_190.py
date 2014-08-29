import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-190"

def AM_WebApp_LoginWithRememberMeOption_190(log_file):
    

    
    login=("1405340124887.png")
    password=("1405340138333.png")
    masterpassword=("1404903010906.png")
    
    loggedin=("1404910191023.png")
    RememberMe=("1405673763490.png")
    HelloThere=("1406540282252.png")
    
    #type("m", KEY_CTRL)
    print("LoginTOApp")
    AM_common.load_browser_with_url("http://www.google.com/")
    sleep(6)
    click(AM_common.redicon)
    sleep(6)
    
    if exists(loggedin):
        AM_common.write_log(log_file,"You are alredy logged into AVG Me") 
        click(loggedin)
    if exists(RememberMe):
        AM_common.verify(log_file,RememberMe)
        click(RememberMe)    
    if exists(login):
        AM_common.verify(log_file,login)
        click(login)
        sleep(2)
        type("michael.scott.avg@gmail.com")
    if exists(password):
        AM_common.verify(log_file,password)
        click(password)
        sleep(2)
        type("US!pf.avg")
        sleep(2)
        type(Key.ENTER)
    if exists(masterpassword):
        AM_common.verify(log_file,masterpassword)
        click(masterpassword)
        sleep(2)
        type("US!pf.avg")
        sleep(2)
        type(Key.ENTER)
    sleep(2)
    AM_common.write_log_with_screenshot(log_file,"See Screenshot:")
    AM_common.verify(log_file,HelloThere)
    type(Key.ESC)
    AM_common.write_log(log_file,"You are succesfully logged in") 
             
    
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=AM_common.create_log_folder(test_case_script_name, test_case_id)

        AM_common.InstallExtention(log_file)
        AM_common.AppOpen(log_file)
        AM_common.LogOut(log_file)

        AM_WebApp_LoginWithRememberMeOption_190(log_file)
        
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