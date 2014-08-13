import PF_Android_common
reload(PF_Android_common)
from sikuli import *




def PF_Android_FB05_AppAccessOn_GreyToGreen_716(log_file):
    Page=("FB05_page.png")
    Apps=("FB05_apps.png")
    Percentage=("FB05_peracentage.png")
    More=("FB05_pros.png")
    Add_info=("1407920913249.png")
    Less=("FB05_less.png")

    Fixes=("fixes.png")
    Grey=("1407920969123.png")
    Uncheck=("Fb05_uncheck.png")
    Hometown=("FB05_navigate.png")
    My_app=("FB05_navigate_down.png")
    Green=("1407920988684.png")
    PF_Android_common.locateItem(log_file, Grey)
    PF_Android_common.verify(log_file, Grey)
    click(Grey)
    PF_Android_common.verify(log_file, Page)
    click(More)
    PF_Android_common.verify(log_file, Add_info)
    click(Less)
    PF_Android_common.verify(log_file, More)

    PF_Android_common.locateItemWebPage(log_file, Apps)
    while exists(Uncheck):
        click(Uncheck)
        sleep(2)
    PF_Android_common.locateItem (log_file, Hometown)
    PF_Android_common.verify(log_file, Hometown)
    while exists(Uncheck):
        click(Uncheck)
        sleep(2)
    PF_Android_common.locateItem(log_file, My_app)
    PF_Android_common.verify(log_file, My_app)
    while exists(Uncheck):
        click(Uncheck)
        sleep(2)
    if not exists(Uncheck):
        click(Fixes)
        PF_Android_common.verify(log_file, Green)        
                
                 
test_case_id="PF-716"


if __name__ == "__main__":
    log_file=""
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_Android_common.create_log_folder(test_case_script_name,test_case_id)
        
        PF_Android_common.AppOpen (log_file)
        sleep(5)
        PF_Android_common.FB_logIn(log_file)
        sleep(5)
        PF_Android_FB05_AppAccessOn_GreyToGreen_716(log_file)
        
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)