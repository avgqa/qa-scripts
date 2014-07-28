import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-247"

def AM_WebApp_LaunchWebsiteWithoutAutologin_247(log_file):
    Item=("1405944405181.png")
    Settings=("1406205001197.png")


    Password=("1406205193768.png")
    Master=("1406205247006.png")



    click(AM_common.redicon)
    wait(4)
    AM_common.verify(log_file,Item)
    hover(Item)
    click(Settings)
    AM_common.verify(log_file,Password)
    doubleClick(Password)
    AM_common.verify(log_file,Master)
    





    
    
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

        
        AM_WebApp_LaunchWebsiteWithoutAutologin_247(log_file)
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