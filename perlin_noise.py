from kiwi import Kiwi
import time

if __name__ == '__main__':
    count = 0
    kiwi = Kiwi(51, 57)

    
    kiwi.print_board()
    

    while True:
        count += 1
        if (count % 30 == 0):
            kiwi.smooth()

        kiwi.sharpen(0.0025)
        kiwi.grain(0.01)
        kiwi.print_board()
        time.sleep(0.1)
    
