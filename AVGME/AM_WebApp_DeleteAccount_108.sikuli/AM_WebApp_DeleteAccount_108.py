import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-108"

def AM_WebApp_DeleteAccount_108(log_file):
    
    Lock=("1405341978064.png")
    GmailAcc=("1405341461409.png")
    SingIn=("1405342025101.png")
    LoggedIn=("1405342419796.png")
    Trash=("1405343738103.png")
    Delete=("1405344487806.png")
    AM_common.load_browser_with_url("https://accounts.google.com//")
    wait(4)
    AM_common.verify(log_file,Lock)
    AM_common.verify(log_file,SingIn)
    click(SingIn)
    wait(3)
    AM_common.verify(log_file,LoggedIn)
    click(AM_common.redicon)
    wait(3)
    hover(GmailAcc)    
    AM_common.verify(log_file,Trash)
    click(Trash)
    AM_common.verify(log_file,Delete)
    click(Delete)
    wait(1)


    
    
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=AM_common.create_log_folder(test_case_script_name, test_case_id)
        #AM_common.ClearBrowsingData()
        AM_common.InstallExtention(log_file)
        AM_common.AppOpen(log_file)
        AM_common.LoginTOApp(log_file)
        AM_common.AddNewAccount(log_file)
        AM_WebApp_DeleteAccount_108(log_file)
        
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