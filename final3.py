from gpiozero import DistanceSensor, LED
from signal import pause
from time import sleep
import Adafruit_CharLCD as LCD
ledg = LED(16)
ledb = LED(21)
ledr = LED(20)
ultrasonic = DistanceSensor(echo =17, trigger=4)
lcd_rs=26
lcd_en=19
lcd_d4=13
lcd_d5=6
lcd_d6=5
lcd_d7=11
lcd_backlight=20
lcd_columns=16
lcd_rows=2
lcd=LCD.Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows,lcd_backlight)


while True:
    print("STOP")
    lcd.message("STOP")
    ledr.on()
    ultrasonic.wait_for_in_range()
    print("Scanning...")
    lcd.clear()
    lcd.message("Scanning...")
    ledr.off()
    ledb.on()
    sleep(4)
    ledb.off()
    lcd.clear()
    print("Pass detected go ahead")
    lcd.message("Pass detected\n Go Ahead")
    ledg.on()
    sleep(5)
    ultrasonic.wait_for_out_of_range()
    ledg.off()
    ledb.off()
    ledr.on()
    lcd.clear()

