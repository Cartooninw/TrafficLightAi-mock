#import random
#import time
#import threading
#
#def Tester(ttest):
#    while True:
#    ttest += 1
#    return ttest
#
#test = Tester(0)
#print(test)
#wait(2)
#print(test)
#
#import concurrent.futures
#import time
#import threading
#
## A global variable to keep track of the test value
#ttest = 0
#running = True  # Flag to control the loop
#test =0 
#def Tester():
#    global ttest, running , test
#    while running:
#        ttest += 1
#        ttest += test
#        time.sleep(1)  # Sleep to slow down the incrementing
#
## Create and start the thread
#test_thread = threading.Thread(target=Tester )
#test_thread.start()
#
## Wait for 2 seconds
#print(ttest)
#test += 2
#time.sleep(4)
## Print the current value of ttest
#
#print(ttest)
#
## Stop the thread
#running = False  # Set the flag to False to stop the loop
#test_thread.join()  # Wait for the thread to finish
#import time
#def foo(bar):
#    while True:
#        bar += 1
#        time.sleep(1)
#    return bar
#
#with concurrent.futures.ThreadPoolExecutor() as executor:
#    future = executor.submit(foo, 0)
#    return_value = future.result()
#    print(return_value)
#    time.sleep(2)







#test_variable = threading.Event()
#
#A = 0
#def test_function(recive ):
#    global A
#    while not recive.is_set():
#        #print(recive)
#        A += 1
#        print(A)
#        time.sleep(1)
#def onStop(test):
#    global A
#    while not test.is_set():
#        time.sleep(1)
#        if A >= 5 :
#            #print("test")
#            test.set()
#        else:
#            A += 2
#            #print(test)
#t1 = threading.Thread(target=test_function,args=(test_variable,))
#t2 = threading.Thread(target=onStop,args=(test_variable,))
#
#t1.start()
#t2.start()
#
#t1.join()
#t2.join()
#
#print("Done")
#randomtest = random.choice([A for A in range (0,3)])
#tset = {"test":"pass"}
#pass1  = iter(tset.items())
#pass1 , pass2 = next(iter(tset.items()))
#pass1,pass2 = (next1 ,next2) for next1,next2 in tset.items()
#print( list(pass1))
#def teset (test2 = 0):
#    print(test2)
#teset('a')
#def Create_Traffic(para1):
#    para1 = []
#    return para1
#print(Create_Traffic("A").append("Test"))
#lister = ["a"]
#if lister:
#    print("is not empty")
#else:
#    print("is empty")


#A = [0] 
#B = [1]
#
#if A[0] and A[0] :
#    print("A")
#
#if B[0] :
#    print("B")
import threading
import time
op = threading.Event()
def testerfunction(recive):
    while not op.is_set():
        #recive.append(1)
        recive[0] += 1
        time.sleep(1)
test1, test2, test3,test4 = 0 , [0] ,0 ,[]
thred = threading.Thread(target=testerfunction , args=(test2,))

thred.start()
#thred.join()
while True:
    print(test2)
