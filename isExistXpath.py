'''
셀레니움에서 사용하며
함수에 아규먼트는 접속한 브라우저 드라이버 xpath 딜레이등이며
xpath가 일정시간동안 확인후 없으면 false 있으면 true를 반환함.
'''
def isExistXpath(driver,xpath, implicitly_wait_time=0, old_wait=25):
    driver.implicitly_wait(implicitly_wait_time)
    try:
        driver.find_element(By.XPATH, xpath)
    except Exception:
        return False
    finally:
            driver.implicitly_wait(old_wait)
    return True
