import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn.objects as so
from sklearn.cluster import KMeans
# Datos de ejemplo: puntos en un espacio 2D
scales = [1,1]  # ¿[mm, km]?

rng = np.random.default_rng(0)
N = 30

df = pd.DataFrame(
    {
        "x": scales[0] * rng.normal([0, 1, 0, 1], 0.05, size=[N, 4]).ravel(),
        "y": scales[1] * rng.normal([0, 0, 1, 1], 0.05, size=[N, 4]).ravel(),
    }
)

# Inicializar el modelo K-means con 2 clusters
kmeans = KMeans(n_clusters=4)

# Ajustar el modelo a los datos
kmeans.fit(df)

# Predecir los clusters de los puntos
df["cluster"] = kmeans.predict(df)

# Agregar los centros de los clusters
df = df.join(
    df["cluster"]
    .map(lambda x: kmeans.cluster_centers_[x])
    .apply(lambda x: pd.Series(x, index=["x_cluster", "y_cluster"]))
)

# Mostramos el DataFrame

# Graficar los puntos y los centros de los clusters
(
    so.Plot(df, color="cluster")
    .scale(color=so.Nominal())
    .add(so.Dots(), x="x", y="y")
    .add(
        so.Dot(marker="x", stroke=2, pointsize=10), 
        x="x_cluster",
        y="y_cluster",
        label="Centro del cluster",
    )
)

plt.show()
