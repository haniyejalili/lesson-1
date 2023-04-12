secend_time = 0 
hour = float(input("Please enter hour 0_23:"))
minute = float(input("please enter minute 0_59 :"))
second = float(input("please enter second 0_59:"))
secend_time = hour * 3600
secend_time = ( minute * 60) + secend_time
secend_time = second + secend_time
print(secend_time)

