import random
import time
random.seed(time.time())
start_time = time.time()
a = []
for i in range(10000):
    a.append(random.randint(1, 1000))


end_time = time.time()
print("---%s seconds ---" % (end_time - start_time))
