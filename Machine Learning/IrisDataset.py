
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

iris = load_iris()
# print(iris.data)
# print(iris.target)
# print(iris.target_names)

# print(iris.data.shape)
# print(iris.target.shape)

# import KNN (K nearest neighbors)

knn = KNeighborsClassifier(n_neighbors=1)
x = iris.data
y = iris.target
print("X target =" + str(x))
print("Y Shape =" + str(y))
knn.fit(x, y)
# print(knn.predict([[5.1,3.5,1.4,0.2]]))
# print(knn.predict([[5.9,3.0,5.1,1.8]]))

# Training happens here
# separate data into train and test groups

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=60)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
knn.fit(x_train, y_train)
prediction = knn.predict(x_test)
print("prediction = " + str(prediction) + " size " + str(len(prediction)))
print("y_test = " + str(y_test) + " size " + str(len(y_test)))


performance = metrics.accuracy_score(y_test, prediction)
print(performance)

k_values = {}
k = 1

while k < 25:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    prediction = knn.predict(x_test)
    performance = metrics.accuracy_score(y_test, prediction)
    k_values[k] = round(performance, 4)
    k += 1

print(k_values)

plt.plot(list(k_values.keys()), list(k_values.values()))
plt.xlabel('values of k')
plt.ylabel('performance')
plt.show()


logreg = LogisticRegression()
logreg.fit(x_train,y_train)
prediction_logreg = logreg.predict(x_test)
performance_logreg = metrics.accuracy_score(y_test,prediction_logreg)
print("performance_logreg = " + str(performance_logreg))
