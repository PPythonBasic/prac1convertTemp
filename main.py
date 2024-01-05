"""
เขียนโปรแกรม รับอุณหภูมิที่เป็น เซลเซียส (Celsius) เข้ามา ทำการแปลงเป็นฟาเรนไฮต์ (Fahrenheit)
และแสดงผลออกมา โดยใช้สูตร


สูตรการแปลง
F = (C * 9/5) + 32
"""


## รับข้อมูลจากผู้ใช้งาน
temp = float(input("Enter your Temp (Celsius) : "))


## แปลงอุณหภูมิ
F = (temp * 9 / 5) + 32


## แสดงผล
print("temp", temp, "Celsius convert to", F, "Fahrenheit")

# temp 15.60 C convert to temp 60.08 F
