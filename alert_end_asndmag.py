'''
경고창 닫기
경고창이 았을경우 그 경고창 메세지를 저장하여 반환함
경고창이 없을경우 noalert를 반환
수정해야할사항:경고창이 없을경우가 에러남...
'''

def alert_end_asndmag(driver):
  if EC.alert_is_present():
      msg1 = driver.switch_to.alert.text
      driver.switch_to.alert.accept()
  else:
      msg1 = "noalert"
      driver.switch_to.parent_frame()
  if msg1 !="noalert" : tele_sand_msg(msg1)
  return msg1
