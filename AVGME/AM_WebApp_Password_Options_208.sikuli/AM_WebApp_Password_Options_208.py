import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-208"

def AM_WebApp_Password_Options_208(log_file):
    Item=("1405944405181.png")
    Settings=("1405931254641.png")

    Password=("1405686257803.png")
    Eye=("1405946826104.png")
    Copy=("1405946866355.png")
    Hiden=("1405946909913.png")
    Shown=("1405946927772.png")


    click(AM_common.redicon)
    wait(4)
    AM_common.verify(log_file,Item)
    hover(Item)
    click(Settings)
    AM_common.verify(log_file,Hiden)
    AM_common.verify(log_file,Eye)
    click(Eye)
    AM_common.verify(log_file,Shown)
    AM_common.verify(log_file,Copy)
    click(Copy)
    data=Env.getClipboard()  
    Password="US!pf.avg"
    if data == Password:
        AM_common.write_log(log_file,"Password was copied correcty----------"+str(data))
    else:
        AM_common.write_log(log_file,"Password was copied incorrecty----------"+str(data))
        
    




    
    
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

        
        AM_WebApp_Password_Options_208(log_file)
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