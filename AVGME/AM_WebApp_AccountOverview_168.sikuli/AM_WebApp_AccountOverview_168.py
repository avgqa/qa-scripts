import AVGME_common as AM_common
reload(AM_common) 



test_case_id="AM-168"

def AM_WebApp_AccountOverview_168(log_file):
    Accounts=("1406027347813.png")
    FbFilled=("1406027609084.png")
    FbGrey=("1406027642065.png")
    FbHover=("1406027666607.png")
    Cancel=("1406028180682.png")
    TwitterGrey=("1406028218310.png")
    TwitterHover=("1406028257890.png")
    TwitterFilled=("1406028286723.png")
    GmailGrey=("1406028356302.png")
    GmailHover=("1406028375115.png")
    GmailFilled=("1406028395426.png")

    NewGrey=("1406028472773.png")
    NewHover=("1406028504858.png")
    NewFilled=("1406028526951.png")
    Pass=("1406029044253.png")
    
    AM_common.AppOpen(log_file)
    if exists (Accounts):
        click(Accounts)
    AM_common.verify(log_file,FbGrey)
    hover(FbGrey)
    AM_common.verify(log_file,FbHover)
    click(FbHover)
    AM_common.verify(log_file,FbFilled)
    click(Cancel)
    

    AM_common.verify(log_file,TwitterGrey)
    hover(TwitterGrey)
    AM_common.verify(log_file,TwitterHover)
    click(TwitterHover)
    AM_common.verify(log_file,TwitterFilled)
    click(Cancel)
    hover(Pass)
    
    AM_common.verify(log_file,GmailGrey)
    hover(GmailGrey)
    AM_common.verify(log_file,GmailHover)
    click(GmailHover)
    AM_common.verify(log_file,GmailFilled)
    click(Cancel)
    
    
    AM_common.verify(log_file,NewGrey)
    hover(NewGrey)
    AM_common.verify(log_file,NewHover)
    click(NewHover)
    AM_common.verify(log_file,NewFilled)
    click(Cancel)
            




    
    
    
        
    
    
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
        


        
        AM_WebApp_AccountOverview_168(log_file)

        
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