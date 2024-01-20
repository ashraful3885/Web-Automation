from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Assuming the website URL is https://www.lazada.com/en/
BASE_URL = "https://www.lazada.com/en/"

@given("the Lazada website is open")
def step_open_website(context):
    context.driver = webdriver.Chrome()  # You can use any other WebDriver here
    context.driver.maximize_window()
    context.driver.get(BASE_URL)

# Step definition for closing the browser
@then("I close the browser")
def step_close_browser(context):
    context.driver.quit()

@when('I click on the "Home" nav element')
def step_click_home_nav(context):
    home_nav_element = context.driver.find_element(By.XPATH, "//div[@id='first']//ul[@class='nav navbar-nav semi-bold text-right']//li[1]")
    home_nav_element.click()
    # Adding a short sleep to allow the home page to load
    time.sleep(5)

@then("I should see the Lazada home page")
def step_should_see_home_page(context):
    title_element = context.driver.find_element(By.CSS_SELECTOR, "div[id='fist-title'] span:nth-child(1)")
    title_text = title_element.text
    expected_title = "ECOMMERCE IS CHANGING"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"



@when('I click on the "About" dropdown')
def step_click_about_dropdown(context):
    about_dropdown = context.driver.find_element(By.XPATH, "//div[@id='first']//ul[@class='nav navbar-nav semi-bold text-right']//li[2]")
    about_dropdown.click()
    # Adding a short sleep to allow the options to appear
    time.sleep(5)

@then("I should see the about options:")
def step_should_see_options(context):
    options = [row[0] for row in context.table]
    option_xpath = {
        "About Lazada": "//a[normalize-space()='About Lazada']",
        "Intellectual Property Rights Protection": "//div[@id='first']//a[2]",
        "Lazada Covid-19 Response": "//div[@id='first']//a[3]",
        "Lazada Foundation": "//div[@id='first']//a[4]",
    }

    for option in options:
        option_element = context.driver.find_element(By.XPATH, option_xpath[option])
        assert option_element.is_displayed(), f"Option '{option}' is not displayed"

@when('I click on the "About Lazada" option')
def step_click_about_lazada_option(context):
    about_lazada_option = context.driver.find_element(By.XPATH, "//a[normalize-space()='About Lazada']")
    about_lazada_option.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "SETTING THE PACE"')
def step_should_see_about_lazada_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "#fist-title")
    title_text = title_element.text
    expected_title = "SETTING THE PACE"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Intellectual Property Rights Protection" option')
def step_click_intellectual_property_option(context):
    intellectual_property_option = context.driver.find_element(By.XPATH, "//div[@id='first']//a[2]")
    intellectual_property_option.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "LAZADA INTELLECTUAL"')
def step_should_see_intellectual_property_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)")
    title_text = title_element.text
    expected_title = "LAZADA INTELLECTUAL"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Lazada Covid-19 Response" option')
def step_click_covid_response_option(context):
    covid_response_option = context.driver.find_element(By.XPATH, "//div[@id='first']//a[3]")
    covid_response_option.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "LAZADA\'S COVID-19 RESPONSE"')
def step_should_see_covid_response_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-blue.pl-2.pr-3.section-title.mb-5")
    title_text = title_element.text
    expected_title = "LAZADA'S COVID-19 RESPONSE"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Lazada Foundation" option')
def step_click_foundation_option(context):
    foundation_option = context.driver.find_element(By.XPATH, "//div[@id='first']//a[4]")
    foundation_option.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "Securing Southeast Asia’s digital future for youths"')
def step_should_see_foundation_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
    title_text = title_element.text
    expected_title = "Securing Southeast Asia’s digital future for youths"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"


@when('I click on the "Press & Media" option')
def step_click_press_media_option(context):
    press_media_option = context.driver.find_element(By.XPATH, "//div[@id='first']//ul[@class='nav navbar-nav semi-bold text-right']//li[3]")
    press_media_option.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
@then('I should see the page with title "PRESS RELEASES"')
def step_should_see_press_media_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "PRESS RELEASES"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on next option')
def step_click_next(context):
    next = context.driver.find_element(By.XPATH, "//span[@class='carousel-control-next-icon carousel-control-next-icon-blue']")
    next.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
@then('I should see the next page of "PRESS RELEASES"')
def step_should_see_next_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".job-text-xl")
    title_text = title_element.text
    expected_title = "2022"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on previous option')
def step_click_previous(context):
    previous = context.driver.find_element(By.XPATH, "//span[@class='carousel-control-prev-icon']")
    previous.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the previous page of "PRESS RELEASES"')
def step_should_see_previous_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
    title_text = title_element.text
    expected_title = "2023"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"



@when('I click on the "Careers" dropdown')
def step_click_careers_dropdown(context):
    careers_dropdown = context.driver.find_element(By.XPATH, "//div[@id='first']//ul[@class='nav navbar-nav semi-bold text-right']//li[4]")
    careers_dropdown.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the careers options:')
def step_should_see_careers_options(context):
    options = [row[0] for row in context.table]
    option_xpath = {
        "Our jobs": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[2]/li[4]/div[1]/a[1]",
        "Graduates & Interns": "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[2]/li[4]/div[1]/a[2]",
    }

    for option in options:
        option_element = context.driver.find_element(By.XPATH, option_xpath[option])
        assert option_element.is_displayed(), f"Option '{option}' is not displayed"

@when('I click on the "Our Jobs" option')
def step_click_our_jobs_option(context):
    our_jobs_option = context.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[2]/li[4]/div[1]/a[1]")  # Replace with the actual XPath
    our_jobs_option.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "BUILD YOUR FUTURE WITH LAZADA"')
def step_should_see_our_jobs_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "#fist-title")
    title_text = title_element.text
    expected_title = "BUILD YOUR FUTURE WITH LAZADA"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Commercial" category')
def step_click_commercial_category(context):
    commercial_category = context.driver.find_element(By.XPATH, "//p[normalize-space()='Commercial']")
    commercial_category.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "COMMERCIAL"')
def step_should_see_commercial_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "COMMERCIAL"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "See jobs list"')
def step_click_job_list(context):
    job_list = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    job_list.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@when('I click on the "Go Back from Job List" link')
def step_click_job_list_go_back_link(context):
    job_list_go_back_link = context.driver.find_element(By.XPATH, "//a[@id='job-search-go-back-btn']")
    job_list_go_back_link.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@when('I click on the "Go Back" link')
def step_click_go_back_link(context):
    go_back_link = context.driver.find_element(By.XPATH, "//a[@class='go-back']")
    go_back_link.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@when('I click on the "Marketing" category')
def step_click_marketing_category(context):
    marketing_category = context.driver.find_element(By.XPATH, "//p[normalize-space()='MARKETING']")
    marketing_category.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "MARKETING"')
def step_should_see_marketing_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "MARKETING"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Technology" category')
def step_click_technology_category(context):
    technology_category = context.driver.find_element(By.XPATH, "//p[normalize-space()='Technology, AI & Product']")
    technology_category.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "TECHNOLOGY, AI & PRODUCT"')
def step_should_see_technology_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "TECHNOLOGY, AI & PRODUCT"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Security" category')
def step_click_security_category(context):
    security_category = context.driver.find_element(By.XPATH, "//p[normalize-space()='SECURITY, RISK AND ENTERPRISE INTELLIGENCE']")
    security_category.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "SECURITY, RISK AND ENTERPRISE INTELLIGENCE"')
def step_should_see_security_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "SECURITY, RISK AND ENTERPRISE INTELLIGENCE"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Supply" category')
def step_click_supply_category(context):
    supply_category = context.driver.find_element(By.XPATH, "//p[normalize-space()='Supply Chain & Logistics']")
    supply_category.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "SUPPLY CHAIN & LOGISTICS"')
def step_should_see_supply_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "SUPPLY CHAIN & LOGISTICS"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Corporate" category')
def step_click_corporate_category(context):
    corporate_category = context.driver.find_element(By.XPATH, "//p[normalize-space()='CORPORATE FUNCTION']")
    corporate_category.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "CORPORATE FUNCTION"')
def step_should_see_corporate_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "CORPORATE FUNCTION"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Customer" category')
def step_click_customer_category(context):
    customer_category = context.driver.find_element(By.XPATH, "//p[normalize-space()='Customer Care']")
    customer_category.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "CUSTOMER CARE"')
def step_should_see_customer_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "CUSTOMER CARE"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Strategy" category')
def step_click_strategy_category(context):
    strategy_category = context.driver.find_element(By.XPATH, "//p[normalize-space()='STRATEGY & MANAGEMENT']")
    strategy_category.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "STRATEGY & MANAGEMENT"')
def step_should_see_strategy_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "STRATEGY & MANAGEMENT"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"


@when('I click on the "Graduates & Interns" option')
def step_click_graduates_interns_option(context):
    graduates_interns_option = context.driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[2]/li[4]/div[1]/a[2]")  # Replace with the actual XPath
    graduates_interns_option.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "GRADUATES & INTERNSHIPS"')
def step_should_see_graduates_interns_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "#fist-title")
    title_text = title_element.text
    expected_title = "GRADUATES & INTERNSHIPS"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Graduates_job" category')
def step_click_graduates_job(context):
    graduates_job = context.driver.find_element(By.XPATH, "//a[contains(@href,'/en/careers/job-search/?section=graduate')]")
    graduates_job.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "START YOUR LAZADIAN JOURNEY"')
def step_should_see_graduates_job_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "START YOUR LAZADIAN JOURNEY"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "Internes_job" category')
def step_click_internes_job(context):
    internes_job = context.driver.find_element(By.XPATH, "//a[@class='btn bg-blue rounded-0 text-white btn-block semi-bold-18 text-center']")
    internes_job.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)


@when('I click on the "Contacts" option')
def step_click_contacts_option(context):
    contacts_option = context.driver.find_element(By.XPATH, "//div[@id='first']//ul[@class='nav navbar-nav semi-bold text-right']//li[5]")
    contacts_option.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see the page with title "CONTACTS"')
def step_should_see_contacts_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, ".grad-green.pl-2.pr-3.section-title")
    title_text = title_element.text
    expected_title = "CONTACTS"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "HQ" element')
def step_click_hq_element(context):
    hq_element = context.driver.find_element(By.XPATH, "//a[normalize-space()='HQ']")
    hq_element.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see "Lazada Group"')
def step_should_see_hq_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "div[id='HQ'] p[class='address-title']")
    title_text = title_element.text
    expected_title = "Lazada Group"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "CHINA" element')
def step_click_china_element(context):
    china_element = context.driver.find_element(By.XPATH, "//a[normalize-space()='CHINA']")
    china_element.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see "CHINA"')
def step_should_see_china_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "div[id='CHINA'] p[class='address-title']")
    title_text = title_element.text
    expected_title = "CHINA"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "INDONESIA" element')
def step_click_indonesia_element(context):
    indonesia_element = context.driver.find_element(By.XPATH, "//a[normalize-space()='INDONESIA']")
    indonesia_element.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see "Lazada Indonesia"')
def step_should_see_indonesia_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "div[id='INDONESIA'] p[class='address-title']")
    title_text = title_element.text
    expected_title = "Lazada Indonesia"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "MALAYSIA" element')
def step_click_malaysia_element(context):
    malaysia_element = context.driver.find_element(By.XPATH, "//a[normalize-space()='MALAYSIA']")
    malaysia_element.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see "MALAYSIA"')
def step_should_see_malaysia_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "div[id='MALAYSIA'] p[class='address-title']")
    title_text = title_element.text
    expected_title = "MALAYSIA"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "SINGAPORE" element')
def step_click_singapore_element(context):
    singapore_element = context.driver.find_element(By.XPATH, "//a[normalize-space()='SINGAPORE']")
    singapore_element.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see "Lazada Singapore"')
def step_should_see_singapore_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "div[id='SINGAPORE'] p[class='address-title']")
    title_text = title_element.text
    expected_title = "Lazada Singapore"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "THAILAND" element')
def step_click_thailand_element(context):
    thailand_element = context.driver.find_element(By.XPATH, "//a[normalize-space()='THAILAND']")
    thailand_element.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see "Lazada Thailand"')
def step_should_see_thailand_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "div[id='THAILAND'] p[class='address-title']")
    title_text = title_element.text
    expected_title = "Lazada Thailand"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "THE PHILIPPINES" element')
def step_click_philippines_element(context):
    philippines_element = context.driver.find_element(By.XPATH, "//a[normalize-space()='THE PHILIPPINES']")
    philippines_element.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see "Lazada Philippines"')
def step_should_see_philippines_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "div[id='THE PHILIPPINES'] p[class='address-title']")
    title_text = title_element.text
    expected_title = "Lazada Philippines"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"

@when('I click on the "VIETNAM" element')
def step_click_vietnam_element(context):
    vietnam_element = context.driver.find_element(By.XPATH, "//a[normalize-space()='VIETNAM']")
    vietnam_element.click()
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)

@then('I should see "Lazada Vietnam"')
def step_should_see_vietnam_page(context):
    # Use time.sleep() instead of WebDriverWait
    time.sleep(5)
    title_element = context.driver.find_element(By.CSS_SELECTOR, "div[id='VIETNAM'] p[class='address-title']")
    title_text = title_element.text
    expected_title = "Lazada Vietnam"
    assert expected_title in title_text, f"Expected title: {expected_title}, Actual title: {title_text}"



