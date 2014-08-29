import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-211"

def AM_WebApp_CancelChanges_211(log_file):
    Item=("1405944405181.png")
    Settings=("1405931254641.png")
    Name=("1405685022627.png")
    Address=("1405932566382.png")
    Username=("1405686157656.png")
    Password=("1405686257803.png")

    SaveChanges=("1406286008964.png")


    Notes=("1405942929057.png")
    UI=("1406286475166.png")

    click(AM_common.redicon)
    wait(4)
    AM_common.verify(log_file,Item)
    hover(Item)
    click(Settings)
    AM_common.verify(log_file,Name)
    click(Name)
    wait(1)
    type("a", KEY_CTRL)  
    wait(1)
    type("Name edited")
    wait(3)


    AM_common.verify(log_file,Address)
    click(Address)
    wait(1)
    type("a", KEY_CTRL)  
    wait(1)
    type("address@edited.com")
    wait(3)
    
    AM_common.verify(log_file,Username)
    click(Username)
    wait(1)
    type("a", KEY_CTRL)  
    wait(1)
    type("Username edited")
    wait(3)
    
    AM_common.verify(log_file,Notes)
    click(Notes)
    wait(1)
    type("a", KEY_CTRL)  
    wait(1)
    type("Notes Edited")
    wait(3)
    AM_common.verify(log_file,SaveChanges)
    click(SaveChanges)    
    AM_common.verify(log_file,Item)
    hover(Item)
    click(Settings)
    AM_common.verify(log_file,UI)





    
    
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

        
        AM_WebApp_CancelChanges_211(log_file)
      #  AM_common.delItem(log_file)
        
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