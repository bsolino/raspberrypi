import RPi.GPIO as GPIO
import time

T_REFRESH = 0.1

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 17

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.1)

print('Starting measurements...')

while True:
    cycle_start = time.time()
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass
    m_start = time.time()

    while GPIO.input(ECHO) == 1:
        pass
    m_stop = time.time()

    t = m_stop - m_start
    d = 170 * t

    print(str(d) + 'm')
    t_cycle = T_REFRESH - (m_stop - cycle_start)
    if t_cycle > 0:
        time.sleep(t_cycle)
    
