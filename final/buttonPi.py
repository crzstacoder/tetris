import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


GPIO.setup(2,GPIO.IN)
GPIO.setup(3,GPIO.IN)
GPIO.setup(4,GPIO.IN)
GPIO.setup(5,GPIO.IN)


class key_check():
    def __init__(self,key):
        self.key = key
        self.state = 0
        self.value = 0
    def key_value(self):
        self.value +=  GPIO.input(self.key)
        #print(self.value)
        if self.value > 10:
            self.value = 0
            return True
        else:
            return False



#GPIO.add_event_detect(2, GPIO.FALLING, callback=callback, bouncetime=1000)
#GPIO.add_event_detect(3, GPIO.FALLING, callback=callback, bouncetime=1000)
# key_a = key_check(2)
# key_b = key_check(3)
# key_c = key_check(4)
# key_d = key_check(5)
# try:
#     while(1):
#         time.sleep(0.01) 
#         if key_a.key_value() == True:
#             print("a")
#         if key_b.key_value() == True:
#             print("b")
#         if key_c.key_value() == True:
#             print("c")
#         if key_d.key_value() == True:
#             print("c")
# finally:
#     GPIO.cleanup()
