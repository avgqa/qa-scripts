import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-253"

def AM_WebApp_HistoryOfGeneratedPasswords_253(log_file):
    
    Lock=("1405341978064.png")
    Generate=("1405421033479.png")
    UI=("1405421160509.png")
    
    GenNew=("1405421957688.png")
    Ultra=("1405421305246.png")
    Capitals=("1405424428886.png")
    Numbers=("1405424126158.png")
    Symbols=("1405424179475.png")
    History=("1406270214729.png")
    HistoryUI=("1406270326733.png")
    Copy=(Pattern("1406278789418.png").targetOffset(76,-11))
    Eye=("1406278789418.png")
    
    click(AM_common.redicon)
    wait(3)
    if exists(Generate):
        click(Generate)
        
    if exists(Capitals):
        click(Capitals)
    if exists(Numbers):
        click(Numbers)
    if exists(Symbols):
        click(Symbols)    
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

    AM_common.write_log(log_file,"Generated password is"+data) 
    AM_common.verify(log_file,History)
    click(History)
    AM_common.verify(log_file,HistoryUI)
    click(Copy)
    data1=Env.getClipboard()
    AM_common.write_log(log_file,"Generated password is"+data1) 
    if data1==data:
        print("password copied correctly")
    else:
        print("password copied incorrectly")
    
    


    
    
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=AM_common.create_log_folder(test_case_script_name, test_case_id)

        #AM_common.InstallExtention(log_file)
        #AM_common.AppOpen(log_file)
        AM_common.LoginTOApp(log_file)

        AM_WebApp_HistoryOfGeneratedPasswords_253(log_file)
        
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