import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-205"

def AM_WebApp_AdvancedSettingsRequireMasterPassword_245(log_file):
    Item=("1405944405181.png")
    Settings=("1405931254641.png")

    SaveChanges=("1404914048588.png")
    Advanced=("1406106236678.png")
    
    MasterPassword=("1406116262277.png")
    Off=(Pattern("1406116279941.png").targetOffset(-24,7))
    On=("1406116306182.png")
    LoggedIn=("1406107325401.png")
    Password=("1406119297973.png")
    PasswordHower=("1406119327250.png")
    Topbar=("1406119349411.png")
    TopbarClick=(Pattern("1406119349411.png").targetOffset(34,-11))
    GoToSite=("1406119686573.png")
    click(AM_common.redicon)
    wait(4)
    AM_common.verify(log_file,Item)
    hover(Item)
    click(Settings)
    AM_common.verify(log_file,Advanced)
    click(Advanced)
    AM_common.verify(log_file,MasterPassword)
    click(Off)
    AM_common.verify(log_file,On)
    AM_common.verify(log_file,SaveChanges)
    click(SaveChanges)
    AM_common.verify(log_file,Item)
    hover(Item)
    click(GoToSite)
    click(Password)
    AM_common.verify(log_file,PasswordHower)
    click(PasswordHower)
    AM_common.verify(log_file,Topbar)
    click(TopbarClick)
    type("US!pf.avg")
    
    
    

    
    
    


    
    
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
        AM_common.AddNewAccount(log_file)

        
        AM_WebApp_AdvancedSettingsRequireMasterPassword_245(log_file)
        #AM_common.delItem(log_file)
        
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