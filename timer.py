print 'PyTimer'
print
import time
import winsound as w

def parent():
    print
    h = input('Enter hrs: ')
    m = input('Enter min: ')
    s = input('Enter sec: ')
    msg = raw_input('Enter any message: ')
    freq = raw_input('Enter freqency: ')
    print
    totalSec = (h*3600) + (m*60) + s

    def timer(totalSec, msg, freq):
        
        tempHold = 0
        msgHold = msg
        freqHold = freq
        try:
            
            for i in range(totalSec):
                tempHold = totalSec - i
                a = tempHold
                b = a/3600
                c = a - 3600*b
                d = c/60
                e = c - 60*d
                print b, ':', d, ':', e
                time.sleep(1)
        

            if msg <> '':
                print msg
            else:
                print 'OVER!!'
            for j in range(2):

                if freq <> '':
                    
                    w.Beep(int(freq), 200)
                else:
                    for i in [1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111]:
                        w.Beep(i, 200)
        
        except KeyboardInterrupt:
            ask = raw_input('c to continue, r to restart timer: ').upper()

            if ask == 'R':
                parent()
            elif ask == 'C':
                
                timer(tempHold, msgHold, freqHold)
        parent()        
    timer(totalSec, msg, freq)
    
parent()
