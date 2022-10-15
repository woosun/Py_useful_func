#새창 닫기
'''
셀레니움 함수
열려있는 새창을 찾아 닫는다(팝업창닫기)
'''
def close_new_tabs(driver):
    closetab = 0
    tabs = driver.window_handles
    while len(tabs) != 1:
        driver.switch_to.window(tabs[1])
        if sendmsg !="" : tele_sand_msg(sendmsg)
        driver.close()
        tabs = driver.window_handles
        closetab=closetab+1
    driver.switch_to.window(tabs[0])
    return closetab
