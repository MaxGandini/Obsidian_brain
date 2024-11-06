from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Cargar dataset
X, y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)

# Dividir el conjunto de datos en 80% para entrenamiento y 20% para prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=144
)

# Entrenar el modelo con los datos de entrenamiento
model = LogisticRegression(max_iter=5_000)
model.fit(X_train, y_train)

# Evaluar el modelo en los datos de prueba
print("Precisión del modelo:", model.score(X_test, y_test))
