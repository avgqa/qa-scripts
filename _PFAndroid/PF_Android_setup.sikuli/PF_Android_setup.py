import PF_Android_common
reload(PF_Android_common)
from sikuli import *


test_case_id="PF-952"
Android =PF_Android_common.Android

orange1=("FB01_orange.png")
green1=("FBgreen1.png")
gray1=("FB1Grey.png")
orange2=("FB02_orange.png")
green2=("FBgreen2.png")
gray2=("FB2grey.png")
orange3=("FB03_orange.png")
green3=("FBgreen3.png")
gray3=("FBgrey3.png")
orange4=("fbOrange4.png")
orange5=("FB05_orange.png")
green5=("FBgreen5.png")
gray5=("FBgrey5.png")
orange6=("FBorange6.png")
orange7=("FBorange.png")
orange8=("FBorange8.png")

orange9=("FB09_orange.png")
green9=("FBgreen9.png")
gray9=("FBgrey9.png")
GL01_orange=("GL01_orange.png")
GL01_green=("GL01_green.png")
GL01_gray=("GL01_gray.png")
GL02_orange=("GLorange2.png")
GL03_orange=("GLorange3.png")
GL03_green=("GL3Green.png")
GL03_gray=("GL3grey.png")
Fixes=("Fixes.png")
Android ='Nexus S - 4.1.1 - API 16 - 480x800'
sim = switchApp(Android)
sim_region = sim.focusedWindow()
center = sim_region.getCenter()

def FixFirstItem (log_file):
    setting=("FB01_setting.png")
    changed=("FB01_changed.png")
    sleep(2)
    click (green1)
    sleep(2)
    PF_Android_common.verify (log_file,setting)
    click(setting)
    PF_Android_common.verify (log_file,changed)
    click (Fixes)
    PF_Android_common.verify (log_file,gray1)
    PF_Android_common.write_log_with_screenshot(log_file,"state of item 1 was changed to Gray")
    print ("state of item 1 was changed to Gray")


def FixSecondItem (log_file):
    sleep(2)
    click (green2)
    PF_Android_common.verify (log_file,"1395392730389.png")
    wheel(center, WHEEL_DOWN, 5)
    sleep(2)           
    click ("FB02_click.png")  
    PF_Android_common.verify (log_file,"FB02_clicked.png")
    click (Fixes)
    PF_Android_common.verify (log_file,gray2)
    PF_Android_common.write_log_with_screenshot(log_file,"state of item 2 was changed to Gray")
    print ("state of item 2 was changed to Gray")

def FixThirdItem (log_file):
    sleep(2)
    click (green3)

    PF_Android_common.verify (log_file,"FB03_page.png")
    click ("FB03_click.png")            
    PF_Android_common.verify (log_file,"Fb03_chacked.png")
    click (Fixes)
    PF_Android_common.verify (log_file,gray3)
    PF_Android_common.write_log_with_screenshot(log_file,"state of item 3 was changed to Gray")
    print ("state of item 3 was changed to Gray")

def FixFifthItem (log_file):
    sleep(3)
    click (green5)
    sleep(5)
    click ("FB05_click.png")  
    PF_Android_common.verify (log_file,"Fb05_CHECKED.png")
    click (Fixes)
    PF_Android_common.verify (log_file,gray5)
    PF_Android_common.write_log_with_screenshot(log_file,"state of item 5 was changed to Gray")
    print ("state of item 5 was changed to Gray")


def FixNinthItem (log_file):
    sleep(2)
    click (green9)
    PF_Android_common.verify (log_file,"FB09_click.png")
    click ("FB09_click.png")
    PF_Android_common.verify (log_file,"FB09_off.png")
    click (Fixes)
    PF_Android_common.verify (log_file,gray9)
    PF_Android_common.write_log_with_screenshot(log_file,"state of item 9 was changed to Gray")
    print ("state of item 9 was changed to Gray")   

def FixGL01 (log_file):
    sleep(2)
    click(GL01_green)
    PF_Android_common.IfPass(log_file)
    PF_Android_common.verify (log_file,"GL01_on.png")
    click("GL01_on.png")
    PF_Android_common.verify (log_file,"GL01_off.png")
    click(Fixes)
    PF_Android_common.verify (log_file,GL01_gray)
    PF_Android_common.write_log(log_file,"State of Item GL01 changed to Gray")
    print ("item GL01 status was changed")   

def FixGL03(log_file):
    save_button=("GL03_save.png")
    sleep(2)
    click(GL03_green)
    PF_Android_common.IfPass(log_file)
    PF_Android_common.verify(log_file,"GL03_page.png")
    wheel(center, WHEEL_DOWN, 25) 
    click("GL03_unchecked.png")
    sleep(2)
    click(save_button)  
    sleep(2)
    click(Fixes)
    PF_Android_common.verify(log_file,GL03_gray)
    PF_Android_common.write_log(log_file,"State of Item GL03 changed to Gray")
    print ("item GL03 status was changed")  



def value(green, orange, gray):
    if exists(Pattern(green).similar(0.90)):
        PF_Android_common.write_log(log_file,"Item in green state detected")
        PF_Android_common.verify(log_file,green) 
        return 1
    elif exists(Pattern(orange).similar(0.90)):
        PF_Android_common.write_log(log_file,"Item in orange state detected")
        PF_Android_common.verify(log_file,orange)
        return 0
    elif exists(Pattern(gray).similar(0.90)):        
        PF_Android_common.write_log(log_file,"Item in gray state detected")
        PF_Android_common.verify(log_file,gray)
        return 0
    else:
        raise Exception("Item not found")
def Android_Setup(log_file) :    
    
    PF_Android_common.FB_logIn(log_file)
    sleep(10)
    x=value(green1, orange1, gray1)
    if x==1:
        FixFirstItem (log_file)
        sleep(3)
    y=value(green2, orange2, gray2)
    if y==1:
        FixSecondItem (log_file)
        sleep(3)
    z=value(green3, orange3, gray3)
    if z==1:
        FixThirdItem (log_file)
    sleep(2)    
    wheel(center, WHEEL_DOWN, 5)
    sleep(2)
    k=value(green5, orange5, gray5)
    if k==1:
        FixFifthItem (log_file)
    wheel(center, WHEEL_DOWN, 5) 
    sleep(2)
    j=value(green9, orange9, gray9)
    if j==1:
        FixNinthItem (log_file)
    PF_Android_common.Google_logIn(log_file)
    sleep(5)
    GL01=value(GL01_green, GL01_orange, GL01_gray)
    if GL01==1:
        FixGL01 (log_file)
    GL03=value(GL03_green, GL03_orange, GL03_gray)
    if GL03==1:
        FixGL03 (log_file)
    PF_Android_common.clearCookiesOnPF(log_file, sleepTime = 6, pf_gear = None, findGear = True, pln=None)    
    sleep(5)
    PF_Android_common.FB_logIn(log_file)
    sleep(15)
    PF_Android_common.Google_logIn(log_file) 
    sleep(5)
    wheel(center, WHEEL_UP, 20)
    sleep(2)
    wheel(center, WHEEL_DOWN, 3)    
    orange01_05=[orange1,orange2,orange3,orange4,orange5,]
    orange06_09=[orange6,orange7,orange8,orange9]  
    google=[GL01_orange,GL02_orange,GL03_orange]
    for i in orange01_05:
        PF_Android_common.verify(log_file, i)
        sleep(2)
    wheel(center, WHEEL_DOWN, 5)
    for i in orange06_09:
        PF_Android_common.verify(log_file, i)
        sleep(2)    
    PF_Android_common.locateItem (log_file,"More.png")      
    for i in google:
        PF_Android_common.verify(log_file, i)
        sleep(2)


   
if __name__ == "__main__":
    try:
        script_path, test_case_script_name=os.path.split(sys.argv[0])
        test_case_script_name=test_case_script_name + ".sikuli"
        log_file=PF_Android_common.create_log_folder(test_case_script_name,test_case_id)
        PF_Android_common.AppOpen(log_file)
        sleep(10)
        Android_Setup(log_file)
        PF_Android_common.PassCase(log_file, test_case_id)
        
    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_Android_common.write_log(log_file,msg)        
        PF_Android_common.FailTestCase(log_file, test_case_id)   