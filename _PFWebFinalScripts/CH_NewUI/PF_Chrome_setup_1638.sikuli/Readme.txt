12.09.2013(?) - functions added from Kathy:
	     
	     protection_values(): get the percentage and number of the most private settings
             get_img_value(image,text):
			get the value from image of facebook protection level, used by the above function
            locate_item_page_by_page(img) and locate_item_line_by_line(img)


12.11.2013 - UA QA team - edited LinkedInLogIn and FacebookLogin functions to check if user is already logged into FB, LinkedIN.
Added  find_img function for imagge search.


12.13.2013 - changes from Kathy: 

	     Facebook login: line136: added facebook image to identify facebook section.
	     
	     LinkedInlogin: added locate linkedIn section image using locate_item_page_by_page.

12.16.2013 - UA QA team:
	     PassCase function added - line 359
	     load_browser_with_url -line 278 - edited, not stable now. We will modify it in future.
	     (Not stable because could not detect CH instance that is already active, but run Ch in max. with --start-maximized param.) 

12.16.2013 - Ron M: 
	     Merged in changes needed for Framework integration. The these scripts will be run automatically from a Framework that will open the VM, launch the scripts and post
	     to TestLink. These scripts will be run from a share drive accessible to the VM's Added check for the Program Files x86 folder for CH if its not there it will use the 	     	     regular Program Files. Appending the --start-maximized param after the check. 
	
	     Note: all global variables are named with the prefix _ as a convention. 


12.16.2013 - Kathy Li: 
	
	     improved load_browser_with_url(), fixed a bug in LinkedInLogin()
	     imporved InstallExtension(), somehow some lines was commented out and was broken

12.16.2013 - Kathy Li: 
			      
		modified GoogleLogin(logfile): skip login if it's already logged in.

		added: locate_google_section(logfile)

12.18.2013 - UA QA team:

		added functions for locating Tracking and Websites sections(lines 133 and 140): locate_tracking_section(logfile), locate_websites_section(logfile)(those functions were needed for
		1322 test case automation).
		As example was taken locate_google_section(logfile) function.
	     					
12.18.2013 -  Kathy Li:
		modified locate google_section, locate_tracking_section and locate_website_section(logfile):
		locate the first image by page down, and the second image line by line. The two images used should be same all the time.

		we shoudn't use the last fix item of tracking or websites section to locate the section, 2 reasons: 
		1. these functions will be used other places, and the status could be different
		2. when the last item on the bottom of the browser, when hover over, bottom part of the hover image maynot be shown completely

12.19.2013 - UA QA team:
		added new verify_exactly function on line 352. because in some cases we need 99% matching(for example in LinkedIn section)
		edited Facebook protection section function 

12.19.2013 - Kathy Li:
		Added locate_linkedIn_section(logfile) function, changed test 358 and 1374, 1375, 1329 using locate_item_line_by_line(logfile, img) instead of useing 
		find_img(img), reason: no logfile, and not stable.

12.20.2013 - Ron M:
		Added the cleanTestScript method. This is required since when running through the command line the path to the current script has scriptname.py (the .py extension)
		running in the IDE does not. So, the log file was being created under another directory not the Sikuli directory.
		
12.20.2013 - Kathy Li:
		added ClearBrowsingData to InstallExtension function since only InstallExtension needs it.
		changed login function that if there is history logging data exists, take it, only enter password.

12.23.2013 - Kathy Li:
		added FailTestCase(logfile, test_case_id) function. Main function exception will be, please use it for the new scripts.


    except FindFailed, f:
        msg =  "Find Failed Exception: %s " % f
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)
        
    except Exception, e:
        msg =  "Exception detected: %s " % e
        PF_common.write_log(log_file,msg)        
        PF_common.FailTestCase(log_file, test_case_id)

12.27.2013 - Kathy Li:
        added write tested link to logfile in PassCass and FailTestCase functions, so it will be clear what url is tested.
        improved get protection level value function, it name is: get_protection_value(logfile)
	added recording time for installation, open browser and login to tracking time and test cycle. so we can see performance for each phase.

12.29.2013 - Kathy Li:
	Protection level function is improved and name is changed to: get_protection_level(logfile)
	added write_log_with_screenshot: screenshot will be taken when log is written, for tracking issues convenience
	FacebookLogin: added ok button for Chrome setup when login facebook after removed account from family, it will ask special permission after login.
	added screenshot for locate_item_line_by_line(logfile), locate_item_page_by_page(logfile)

12.31.2013 -- Kathy Li:
	improved locate tracking section and websites section by using key.END and Key.PAGE_UP, instead of looking for images. faster.

01.14.2014 -- Kathy Li:
	added function verify_continue_with_similarity(logfile,image,similarity), reason: we need high similarity in PF_Chrome_setup 
	because the grey bang and orange bang is same in sikuli.
	change readme to wordpad, format: Office XML document. please use the other readme for better readability.

01.23.2014: Kathy

                added similiarity 0.90 to PF_icon image in InstallExtension(logfile), 

                added skip tutorial pages code if it's not showing(it's showing 50/50).

                Added “maybe later” to FB login, linkedinLogin, google login, installExtension, because if the account is first time after install, or reset, this page will show.

                changed locate_tracking _seciont(logfile): locate image page by page, then locate another image line by line

                added reset_account(logfile)
                
                improved locate_websites_section(logfile), same change as locate_tracking_section(logfile)

                Chrome clear browsing data: changed to clear two items, clear cache and clear autofill.

                Added screenshot for FailTestcase(logfile, test_id) and PassCase(logfile, test_id) 


