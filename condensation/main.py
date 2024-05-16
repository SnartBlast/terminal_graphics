
from moisture import Moisture
import time

if __name__ == '__main__':
    print('starting!')

   
    moisture = Moisture()

    
    while True:
        moisture.print_board()
        for i in range(50):
           moisture.insert_droplet() 
        moisture.iterate_board()
        moisture.dry_board() 
        time.sleep(0.1)


