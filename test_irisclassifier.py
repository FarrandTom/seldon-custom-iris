from IrisClassifier import IrisClassifier

X = {
    "data": {
	"names": ["Sepal length","Sepal width","Petal length", "Petal Width"],
	"ndarray": [
	    [6.8,  2.8,  4.8,  1.4],
	    [6.0,  3.4,  4.5,  1.6]
	]
    }
}

result = IrisClassifier().predict(X['data']['ndarray'], X['data']['names'])
print(result)