import pickle 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def scale(n1,n2,n3,n4,n5,n6,n7):
    value = pickle.load(open('F:\Ineuron\Machine Learning\Live Class\Linear Regression\Scalar_Admission.pickle','rb'))
    return value.transform([[n1,n2,n3,n4,n5,n6,n7]])


value = scale(337.0, 118.0 , 4.0 , 4.5 , 4.5 , 9.65 , 1)
print(scale(337.0, 118.0 , 4.0 , 4.5 , 4.5 , 9.65 , 1))


def prediction(value):
    model = pickle.load(open('../admission_model.pickle','rb'))
    return model.predict(value)

print(prediction(value))