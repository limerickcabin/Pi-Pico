from machine import Pin, PWM, Timer
import time

#global so callback and main can use it
ledpin=Pin(25, Pin.OUT)

#when the timer fires, turn off the led
def offcallback(param):
    ledpin.value(0)

def main():
    pwm0=PWM(Pin(0))
    freq=fmin=15000
    fstep=500
    fmax=25000
    sweepms=2000 #length of time in ms to sweep fmin to fmax
    dwellms=int(sweepms/((fmax-fmin)/fstep))
    print(dwellms)
    
    while 1:
        pwm0.freq(freq)
        pwm0.duty_u16(2**15)
        freq+=fstep
        if (freq>fmax) or (freq<fmin):
            #hit a limit - go the other way
            fstep=-fstep
            #turn on the led and set a timer to turn it off
            ledpin.value(1) #on
            tim2=Timer(period=100, mode=Timer.ONE_SHOT, callback=offcallback)
        time.sleep_ms(dwellms)
    #forever

main()

