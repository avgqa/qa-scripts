
import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-191"

def AM_WebApp_GeneratingPasswordWithDefVal_191(log_file):
    
    Lock=("1405341978064.png")
    Generate=("1405421033479.png")
    UI=("1405421160509.png")
    
    GenNew=("1405421957688.png")
    Ultra=("1405421305246.png")
    
    click(AM_common.redicon)
    wait(3)
    if exists(Generate):
        click(Generate)
        
 
    AM_common.verify(log_file,UI)
    wait(1)
    #AM_common.verify(log_file,GenNew)
    click(GenNew)
    AM_common.verify(log_file,Ultra)
    doubleClick(Ultra)
    type("a", KeyModifier.CTRL)
    wait(1)
    type("c", KeyModifier.CTRL)
    wait(2)
    data=Env.getClipboard()

    print(data)
    AM_common.write_log(log_file,"Generated pasword is"+data) 


    
    
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=AM_common.create_log_folder(test_case_script_name, test_case_id)

        AM_common.InstallExtention(log_file)
        AM_common.AppOpen(log_file)
        AM_common.LoginTOApp(log_file)

        AM_WebApp_GeneratingPasswordWithDefVal_191(log_file)
        
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