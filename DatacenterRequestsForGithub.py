#datacenter replacement requests automated
#this is a script that takes two dictionaries as arguments
#and passes their values to the fill_form function, which then uses the driver to find html elements
#once they are found it sends particular values using the key value pairs in the dictionary
#It also clicks the necessary buttons to continue on with the webform

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

chromedriver = 'C:/Users/*****/AppData/Local/Programs/Python/Python37/chromer/chromedriver'

#below marked out code is used for testing so that once the form is filled you can exit out of the empty form so it is last saved
#driver = webdriver.Chrome(chromedriver)
#driver.get("https://missouri.qualtrics.com/jfe/form/SV_3FdExyaUNZRkJhP?Q_JFE=qdg")

#list of variables for hypervisor team that will remain the same per cluster add
info = {'name': 'Colin', 'email': '****', 'phone': '****',
        'dept': '*****', 'charge': '*****', 'signer': '*****',
        'manufacturer': 'Dell', 'model': '*****', 'OS': 'Esxi',
        'OpDate': '06/07/2019', 'descript': 'hosting vms', 'delivery_date': '06/05/2019',
        'height': '5.13', 'width': '17.08', 'depth': '31.96',
        'weight': '110.01', 'electric': '1100 W', 'ethernet': '*'} #uncertain about the current charge code and signer

#list of variables to change from form to form
changeit = {'machine': '*****', 'serial': '******',
            'IP': '*******', 'cabinet': '******'}



def fill_form(info, changeit):
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://*******')

    driver.implicitly_wait(10)
    
    name_field = driver.find_element_by_name("QR~QID1~TEXT").send_keys(info['name']) #driver function to find element and then prob inherited function to send keys
    driver.implicitly_wait(1)

    email_field = driver.find_element_by_name("QR~QID2~TEXT").send_keys(info['email'])
    driver.implicitly_wait(1)

    phone_field = driver.find_element_by_name("QR~QID3~TEXT").send_keys(info['phone'])
    driver.implicitly_wait(1)

    dept_field = driver.find_element_by_name("QR~QID4~TEXT").send_keys(info['dept'])
    driver.implicitly_wait(1)

    #in case I need to scroll in the future:
    #target = driver.find_element_by_name('QR~QID5') 
    #driver.execute_script("arguments[0].scrollIntoView();", target) 

    locale_field = driver.find_element_by_id("QID5-1-label").click()

    charge_field = driver.find_element_by_name("QR~QID6~TEXT").send_keys(info['charge'])
    driver.implicitly_wait(1)

    signer_field = driver.find_element_by_name("QR~QID7~TEXT").send_keys(info['signer'])
    driver.implicitly_wait(1)

    pageonesubmit_field = driver.find_element_by_name("NextButton").click()
    driver.implicitly_wait(10)

    machine_field = driver.find_element_by_name("QR~QID8~TEXT").send_keys(changeit['machine'])
    driver.implicitly_wait(30)

    machine_alias = driver.find_element_by_name("QR~QID9~TEXT").send_keys('no alias')
    driver.implicitly_wait(1)

    serial_number = driver.find_element_by_name("QR~QID11~TEXT").send_keys(changeit['serial'])
    driver.implicitly_wait(1)

    manufacturer = driver.find_element_by_name("QR~QID12~TEXT").send_keys(info['manufacturer'])
    driver.implicitly_wait(1)

    model = driver.find_element_by_name("QR~QID13~TEXT").send_keys(info['model'])
    driver.implicitly_wait(1)

    OS = driver.find_element_by_name("QR~QID14~TEXT").send_keys(info['OS'])
    driver.implicitly_wait(1)

    IP = driver.find_element_by_name("QR~QID15~TEXT").send_keys(changeit['IP'])
    driver.implicitly_wait(1)

    OpDate = driver.find_element_by_name("QR~QID16~TEXT").send_keys(info['OpDate'])
    driver.implicitly_wait(1)

    descript = driver.find_element_by_name("QR~QID17~TEXT").send_keys(info['descript'])
    driver.implicitly_wait(1)

    shipping_field = driver.find_element_by_id("QID18-1-label").click()
    driver.implicitly_wait(1)

    pagetwosubmit_field = driver.find_element_by_name("NextButton").click()
    driver.implicitly_wait(10)

    delivery_date = driver.find_element_by_name("QR~QID19~TEXT").send_keys(info['delivery_date'])
    driver.implicitly_wait(2)

    height = driver.find_element_by_name("QR~QID20~TEXT").send_keys(info['height'])
    driver.implicitly_wait(2)

    width = driver.find_element_by_name("QR~QID21~TEXT").send_keys(info['width'])
    driver.implicitly_wait(1)

    depth = driver.find_element_by_name("QR~QID22~TEXT").send_keys(info['depth'])
    driver.implicitly_wait(1)

    weight = driver.find_element_by_name("QR~QID23~TEXT").send_keys(info['weight'])
    driver.implicitly_wait(1)

    electric = driver.find_element_by_name("QR~QID28~TEXT").send_keys(info['electric'])
    driver.implicitly_wait(1)

    building = driver.find_element_by_id("QID24-1-label").click()
    driver.implicitly_wait(1)
    
    cabinet = driver.find_element_by_name("QR~QID25~TEXT").send_keys(changeit['cabinet'])
    driver.implicitly_wait(1)

    rackmount = driver.find_element_by_id("QID26-1-label").click()
    driver.implicitly_wait(1)

    ethernet = driver.find_element_by_name("QR~QID27~TEXT").send_keys(info['ethernet'])
    driver.implicitly_wait(2)

    redundant = driver.find_element_by_id("QID29-1-label").click()
    driver.implicitly_wait(2)

    needcables = driver.find_element_by_id("QID30-2-label").click()
    driver.implicitly_wait(2)

    pagethreesubmit_field = driver.find_element_by_name("NextButton").click()
    driver.implicitly_wait(60)

    nameagain = driver.find_element_by_name("QR~QID31~TEXT").send_keys(info['name'])
    driver.implicitly_wait(60)

    secondname = driver.find_element_by_name("QR~QID39~TEXT").send_keys('*****')
    driver.implicitly_wait(60)

    pagefoursubmit_field = driver.find_element_by_id("NextButton").click()
    driver.implicitly_wait(10)
    
fill_form(info, changeit)

