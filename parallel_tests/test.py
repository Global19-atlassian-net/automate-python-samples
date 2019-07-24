from selenium import webdriver
import os, sys, json

try:
    json_name = sys.argv[1]
    counter_val = sys.argv[2]
except IndexError:
    print('Json name and counter val must be passed as first and second argument, respectively, from the comamnd line')
    sys.exit(1)

USERNAME = os.environ.get ('robblackburn2') or sys.argv[2]
BROWSERSTACK_ACCESS_KEY = os.environ.get ('J9jypeH3Zyn9sqVLy9oG') or sys.argv[3]

with open(json_name, "r") as f:
    obj = json.loads(f.read())

instance_caps = obj[int(counter_val)]
print("Test %s started" % (counter_val))

#------------------------------------------------------#
# Mention any other capabilities required in the test
caps = {}
caps["browserstack.debug"] = "true"
caps["build"] = "parallel tests"

#------------------------------------------------------#

caps = {**caps, **instance_caps}

#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE

driver = webdriver.Remote(
    command_executor='http://robblackburn2:J9jypeH3Zyn9sqVLy9oG@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://www.qa.orcid.org")
if not "ORCID" in driver.title:
    raise Exception("Unable to load orcid page!")
driver.implicitly_wait(100)
try: driver.find_element_by_id("home-blog-list")
except:
    print ("Unable to load blog")

try: driver.find_element_by_class("menu")
except:
    print ("Unable to load menu")
driver.quit()


#------------------------------------------------------#
