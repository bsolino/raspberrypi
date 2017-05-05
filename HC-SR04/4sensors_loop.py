import RPi.GPIO as GPIO
import time

T_REFRESH = 0.05

GPIO.setmode(GPIO.BCM)

TRIG = 4

ECHO1 = 17
ECHO2 = 27
ECHO3 = 22
ECHO4 = 23

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(ECHO3, GPIO.IN)
GPIO.setup(ECHO4, GPIO.IN)


def echo_time(pin):
    cycle_start = time.time()
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    
    while GPIO.input(pin) == 0:
        pass
    m_start = time.time()

    while GPIO.input(pin) == 1:
        pass
    m_stop = time.time()
    
    t_cycle = T_REFRESH - (m_stop - cycle_start)
    if t_cycle > 0:
        time.sleep(t_cycle)

    return m_stop - m_start


time.sleep(0.1)

print('Starting measurements...')

while True:
    t1 = echo_time(ECHO1)
    t2 = echo_time(ECHO2)
    t3 = echo_time(ECHO3)
    t4 = echo_time(ECHO4)
    
    d1 = 170 * t1
    d2 = 170 * t2
    d3 = 170 * t3
    d4 = 170 * t4

    print('{: .3f}m\t{: .3f}m\t{: .3f}m\t{: .3f}m\t'.format(d1, d2, d3, d4))

GPIO.cleanup()
    
