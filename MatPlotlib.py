# The program evaluates your performance of typing speed
# The program will plot a graph.


import matplotlib.pyplot as plt
import time as t
times = []
mistakes = 0
print("this program will validate your typing speed")
input("press to continue")

while len(times) <5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start
    times.append(time_elapsed)
    if (word.lower()!="programming"):
        mistakes +=1

print("you have made " + str(mistakes) + "mistake(s).")
t.sleep(3)
x = [1,2,3,4,5]
y = times
legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel("time in seconds")
plt.xlabel("Attempts")
plt.title("word evolution")
plt.plot(x,y)
plt.show()

x= [1,2,3,4]
y= [100,200,1100,1800]

plt.plot(x,y)
plt.show()

