import threading
import RPi.GPIO as GPIO
import time

class Info:
	@staticmethod     #被staticmethod修饰符修饰表示该方法是一个静态方法，可以被类直接调用
	def p(message):
		print 'Info: '+message    # '+'表示将两个对象相加

class Wheel:     #这个类产生的对象是单个轮子
	pins ={'a':[31,33],'b':[35,37]}
	def __init__(self,name):   #self参数可以理解为指代类的一个实例，__init__是python里面一个特殊的方法，用于在创建类的实例时去初始化该对象，不需要专门调用
		self.name = name
		self.pin = Wheel.pins[self.name]
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin[0],GPIO.OUT)
		GPIO.setup(self.pin[1],GPIO.OUT)
		self.stop()
	def st(self):
		print 'ss'
	def forward(self):
		Info.p('wheel ' + self.name + ' is forwarding')
		GPIO.output(self.pin[0],GPIO.HIGH)
		GPIO.output(self.pin[1],GPIO.LOW)
	def stop(self):
		GPIO.output(self.pin[0],False)
		GPIO.output(self.pin[1],False)
	def back(self):
		Info.p('wheel ' +self.name + ' is backing')
		GPIO.output(self.pin[0],False)
		GPIO.output(self.pin[1],True)
				
class Car:      #这个类表示的对象是小车
	wheel=[Wheel('a'),Wheel('b')] 
	@staticmethod
	def init():
		GPIO.setmode(GPIO.BOARD)
		Info.p('initialize the smart car ....')		
		Info.p('Smart car is ready to fly!')
	@staticmethod
	def forward():
		Info.p('go straight forward')
		for wheel in Car.wheel:    #列表的遍历
			wheel.forward()
	@staticmethod
	def left():       #左轮停止，右轮前进
		Info.p('turn left ')
        Car.wheel[0].stop()
		Car.wheel[1].forward()

	@staticmethod
	def right():      #左轮前进，右轮停止
		Info.p('turn right ')
		Car.wheel[0].forward()	
		Car.wheel[1].stop()
	
	@staticmethod
	def back():       #两个轮子后退
		Info.p('go straight back')
		for wheel in Car.wheel:
			wheel.back()
	@staticmethod
	def stop():
		Info.p('try to stop the car ...')
		for wheel in Car.wheel:
			wheel.stop()	
if __name__ =='__main__':
	print '....'
	
