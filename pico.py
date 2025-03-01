import time
import machine
#from machine import ADC, Pin
#vsys is presented to ADC pin 29 through a 3:1 divider
divider=3
vcc=3.3
vsysPin=29
adcV=machine.ADC(machine.Pin(vsysPin))
adcT=machine.ADC(4)

#get a bunch of samples of Vsys
samples=[]
total=0
loops=8000
then=time.ticks_us()
for i in range(loops):
    input=adcV.read_u16()
    total+=input
    samples.append(input/16) #convert u16 to ADC counts
elapsed=time.ticks_us()-then
average=total/loops

#stdev of samples (stdev.s)
sumsquares=0
xbar=sum(samples)/len(samples)
for X in samples:
    sumsquares+=(X-xbar)**2
stdev=(sumsquares/(len(samples)-1))**0.5

#internal temperature
aT16=adcT.read_u16()
t=27-(aT16/(2**16)*vcc-0.706)/0.001721 #4.9.5 of RP2040 Datasheet

print(str(loops)+" adc samples in "+str(elapsed)+" us")
print('{:.0f}'.format(1000000/elapsed*loops)+" samples per second")
print('{:.3f}'.format(average/(2**16)*vcc*divider)+" Vsys volts")
print('{:.0f}'.format(machine.freq()/1000000)+" MHz clock")
print('{:.3f}'.format(aT16/(2**16)*vcc)+" temp adc volt")
print('{:.1f}'.format(t)+" C")
print('{:.1f}'.format(t*9/5+32)+" F")
print('{:.1f}'.format(stdev)+" stdev.s of Vsys")
