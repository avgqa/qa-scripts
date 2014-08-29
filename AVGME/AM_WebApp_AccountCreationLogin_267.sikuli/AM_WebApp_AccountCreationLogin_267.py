import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-267"

def AM_WebApp_AccountCreationLogin_267(log_file):
    Item=("1406289655807.png")
    Settings=("1406291257710.png")

    Email=(Pattern("1406290215010.png").targetOffset(-2,18))
    Password=(Pattern("1406290240488.png").targetOffset(7,22))

    Topbar=("1406288911113.png")
    Never=("1406289312290.png")
    NotNow=("1406289369609.png")
    LogIn=("1406288988206.png")
    Dropdown=("1406289052724.png")
    LogOut=("1406289083491.png")
    NoAccounts=("1406290095137.png")
    Close=("1406290616730.png")
    Stored=("1406290696951.png")
    AM_common.load_browser_with_url("https://facebook.com")
    wait(5)
    if exists (Dropdown):
        click(Dropdown)
        click(LogOut)
    
    
    click(Email)
    type("a", KEY_CTRL)  
    type("michael.scott.avg@gmail.com")
    click(Password)
    type("a", KEY_CTRL)  
    type("US!pf.avg")
    click(LogIn)
    AM_common.verify(log_file,Topbar)
    click(NotNow)                                      
    click(AM_common.redicon)
    wait(4)
    AM_common.verify(log_file,NoAccounts)
    AM_common.load_browser_with_url("https://facebook.com")
    wait(5)
    if exists (Dropdown):
        click(Dropdown)
        click(LogOut)    
    click(Email)
    type("a", KEY_CTRL)  
    type("michael.scott.avg@gmail.com")
    click(Password)
    type("a", KEY_CTRL)  
    type("US!pf.avg")
    click(LogIn)
    AM_common.verify(log_file,Topbar)
    click(Close)                                      
    click(AM_common.redicon)
    wait(4)
    AM_common.verify(log_file,Item)
    hover(Item)
    click(Settings)
    AM_common.verify(log_file,Stored)







    
    
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=AM_common.create_log_folder(test_case_script_name, test_case_id)

        AM_common.InstallExtention(log_file)
        AM_common.LoginTOApp(log_file)
        AM_common.delItem(log_file)
        AM_WebApp_AccountCreationLogin_267(log_file)

        

        AM_common.delItem(log_file)
        
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