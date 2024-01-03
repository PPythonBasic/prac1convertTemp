"""
เขียนโปรแกรม รับอุณหภูมิที่เป็น เซลเซียส (Celsius) เข้ามา ทำการแปลงเป็นฟาเรนไฮต์ (Fahrenheit)
และแสดงผลออกมา โดยใช้สูตร


สูตรการแปลง
F = (C * 9/5) + 32
"""


## รับข้อมูลจากผู้ใช้งาน
temp = float(input("Enter your Temp (Celsius) : "))




## แปลงอุณหภูมิ
temp = (temp * 9/5) + 32


## แสดงผล
print("Fahrenheit is ",round(temp,2))