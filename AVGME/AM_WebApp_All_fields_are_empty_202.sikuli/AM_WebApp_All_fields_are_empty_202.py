import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-202"




def AM_WebApp_All_fields_are_empty_202(log_file):

    GmailAcc=("1405341461409.png")
    AddNew=("1404913650255.png")
    Name=("1405685022627.png")
    Address=("1405685728068.png")
    Username=("1405686157656.png")
    Password1=("1405686257803.png")
    Passowrd=("1405338004216.png")
    SaveChanges=("1404914048588.png")
    SaveChangesGrey=("1405683391812.png")
    Stored=( "1404914110969.png")
    Advanced=("1405341526448.png")
    Speed=("1405341545558.png")
    Item=("1405585496047.png")
    Trash=("1405343738103.png")
    Delete=("1405587762833.png")

    #verify(logfile,redicon)
    click(AM_common.redicon)
    wait(4)
    delItem(log_file)
    AM_common.verify(log_file,AddNew)
    click(AddNew)
    click(Name)
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    AM_common.verify(log_file,SaveChangesGrey)
    click(SaveChangesGrey)    
    wait(3)
    AM_common.write_log(log_file,"Accout was not created")

    AM_common.verify(log_file,Name)
    click(Name)
    type("michael.scott.avg@gmail.com")
    wait(3)
    AM_common.verify(log_file,SaveChanges)
    click(SaveChanges)    
    wait(3)
    AM_common.verify(log_file,Stored)
    AM_common.write_log(log_file,"Accout was created")
    delItem(log_file)
    AM_common.verify(log_file,AddNew)
    click(AddNew)
    
    AM_common.verify(log_file,Address)
    click(Address)
    type("michael.scott.avg@gmail.com")
    wait(3)
    AM_common.verify(log_file,SaveChanges)
    click(SaveChanges)    
    wait(3)
    AM_common.verify(log_file,Stored)
    AM_common.write_log(log_file,"Accout was created")
    delItem(log_file)
    AM_common.verify(log_file,AddNew)
    click(AddNew)

    AM_common.verify(log_file,Username)
    click(Username)
    type("michael.scott.avg@gmail.com")
    wait(3)
    AM_common.verify(log_file,SaveChanges)
    click(SaveChanges)    
    wait(3)
    AM_common.verify(log_file,Stored)
    AM_common.write_log(log_file,"Accout was created")
    delItem(log_file)
    AM_common.verify(log_file,AddNew)
    click(AddNew)

    AM_common.verify(log_file,Password1)
    click(Password1)
    type("michael.scott.avg@gmail.com")
    wait(3)
    AM_common.verify(log_file,SaveChanges)
    click(SaveChanges)    
    wait(3)
    AM_common.verify(log_file,Stored)
    AM_common.write_log(log_file,"Accout was created")
    delItem(log_file)





def delItem(log_file):   
    Item=("1405585496047.png")
    Trash=("1405343738103.png")
    Delete=("1405587762833.png")
    while exists(Item):
        AM_common.verify(log_file,Item)
        hover(Item)    
        AM_common.verify(log_file,Trash)
        click(Trash)
        AM_common.verify(log_file,Delete)
        click(Delete)
        wait(2)
    
#Function_call
if __name__ == "__main__":
    log_file = ""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=AM_common.create_log_folder(test_case_script_name, test_case_id)

        #AM_common.InstallExtention(log_file)

        AM_common.LoginTOApp(log_file)
        AM_WebApp_All_fields_are_empty_202(log_file)
        
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