import pandas as pd 
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn.objects as so

grandparent_dir= Path(__file__).parents[4]

data_path = grandparent_dir / "datasets" / "Wholesale_customers_data.csv"

data = pd.read_csv(data_path)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler

transformer = ColumnTransformer(
    [
        (
            "number",
            MinMaxScaler(),
            ["Channel","Region","Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]
        )
    ],
    remainder="passthrough",
    #verbose_feature_names_out=True,
)

df= pd.DataFrame(transformer.fit_transform(data), columns=transformer.get_feature_names_out())

from sklearn.cluster import KMeans

kmeans_ = KMeans(n_clusters=3)

kmeans = kmeans_.fit(df)

df["cluster"] = kmeans.predict(df)

# Get cluster labels and cluster centers
labels = kmeans.labels_
centers = kmeans.cluster_centers_

#sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
#plt.title("Correlation Heatmap of Transformed Data")
#sns.pairplot(df[['number__Fresh', 'number__Milk', 'number__Grocery','number__Frozen']])  # Select columns of interest

# Add the cluster centers to the dataframe
df = df.join(
    df['cluster'].map(lambda x: kmeans.cluster_centers_[x])
    .apply(lambda x: pd.Series(x, index=[f"x_cluster_{i}" for i in range(kmeans.cluster_centers_.shape[1])]))
)

# Graficar los puntos y los centros de los clusters
# (
#     so.Plot(df, color="cluster")
#     .scale(color=so.Nominal())
#     .add(so.Dots(), x="x", y="y")
#     .add(
#         so.Dot(marker="x", stroke=2, pointsize=10),
#         x="x_cluster",
#         y="y_cluster",
#         label="Centro del cluster",
#     ).show()
# )
# Plot the cluster centers
# plt.scatter(df['x_cluster_1'], df['x_cluster_2'], marker='x', color='red', s=100, label='Cluster Centers')
# plt.scatter(df['number__Grocery'], df['number__Detergents_Paper'], marker='x', color='red', s=100, label='Cluster Centers')


plt.figure(figsize=(10, 6))

# sns.pairplot(transformed_df[['Fresh', 'Milk', 'Grocery']])  # Select columns of interest
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('KMeans Clusters and Cluster Centers')
plt.legend()
plt.show()
