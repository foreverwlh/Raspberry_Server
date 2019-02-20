from socket import *   #导入socket模块
import sys         
import time
from car import *      #导入car.py文件
def run_raspberry():
	commands ={'forward':Car.forward,'back': Car.back, 'stop': Car.stop,'left': Car.left,'right': Car.right}    #定义一个字典{字符串：方法}，键是唯一的，值可以是任何类型对象
	HOST ='192.168.1.123'    #定义服务器端地址
	PORT = 8888              #定义服务器端端口
	s= socket(AF_INET, SOCK_STREAM)    #创建socket套接字，AF_INET表示基于网络的，SOCK_STREAM表示面向连接的流套接字
	s.bind((HOST, PORT))            #将服务器端地址端口绑定到套接字上
	s.listen(1)                     #将套接字变为被动的可连接的套接字，参数为监听时可接入的最大连接数
	print ('raspberry pi is listening on port 8888')
	while 1:
	    conn, addr = s.accept()       #被动接受TCP客户端连接，一直等待直到连接到达（无连接时阻塞在这里），conn是返回的客户端套接字，addr是客户端地址
	    print ('Connected by:', addr)
	    while 1:
	            command= conn.recv(1024).replace('\n','')   #replace(old,new),该方法是将字符串中的old字符串用new字符串代替；recv（接收最大字符数）
	            if not command or command not in commands:break    # not 逻辑非，or 逻辑或   not in  成员运算符，如果在指定的序列中没有找到值返回true，这里的意思是如果没有接受到数据，活着数据与commands不匹配，则跳出循环
	            commands[command]()   # commands[command]() ==> 值() ==>  调用方法，本句意思是若字符串匹配，调用字典里作为值的方法
	    conn.close()     #退出循环之后，关闭客户端套接字
	    
if __name__ == '__main__':   #这句话的意思是如果直接执行该py文件，则执行run_raspberry函数，如果该py文件是作为模块导入，则不执行该函数
	run_raspberry()

