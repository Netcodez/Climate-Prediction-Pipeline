# -*- coding: utf-8 -*-
"""Predicting_Climate_in_London (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jd70zjONVSY28o-cVGgBtrE7TAoZpr_V
"""

!python --version

"""![pic.jpg](data:image/jpeg;base64,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)

As the climate changes, predicting the weather becomes ever more important for businesses. The aim of of this machine learning project is building a pipeline to predict the climate in London, England. Specifically, the model will predict mean temperature in degrees Celsius (°C).

Since the weather depends on a lot of different factors, different experiments will be run to determine what the best approach is to predict the weather. In this project, experiments will be run for different regression models predicting the mean temperature, using a combination of `sklearn` and `mlflow`.

You will be working with data stored in `london_weather.csv`, which contains the following columns:
- **date** - recorded date of measurement - (**int**)
- **cloud_cover** - cloud cover measurement in oktas - (**float**)
- **sunshine** - sunshine measurement in hours (hrs) - (**float**)
- **global_radiation** - irradiance measurement in Watt per square meter (W/m2) - (**float**)
- **max_temp** - maximum temperature recorded in degrees Celsius (°C) - (**float**)
- **mean_temp** - **target** mean temperature in degrees Celsius (°C) - (**float**)
- **min_temp** - minimum temperature recorded in degrees Celsius (°C) - (**float**)
- **precipitation** - precipitation measurement in millimeters (mm) - (**float**)
- **pressure** - pressure measurement in Pascals (Pa) - (**float**)
- **snow_depth** - snow depth measurement in centimeters (cm) - (**float**)
"""

from google.colab import drive
drive.mount('/content/drive')

# Run this cell to install mlflow
!pip install -q mlflow

# Run this cell to import the modules you require
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

mlflow.__version__

#load data
data = pd.read_csv('/content/drive/MyDrive/london_weather.csv')
df = data.copy()

df.head()

#Determine the column names, data types, number of non-null vales
df.info()

"""## Data Cleaning"""

df['date'] = pd.to_datetime(df['date'], format="%Y%m%d")

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

"""## EDA"""

# @title Distribution of Cloud Cover
df['cloud_cover'].plot(kind='hist', bins=20, title='Cloud Cover')
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title Distribution of Sunshine

df['sunshine'].plot(kind='hist', bins=20, title='Sunshine')
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title Distribution of Global Radiation

df['global_radiation'].plot(kind='hist', bins=20, title='Global Radiation')
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title Distribution of Maximum Temperature

df['max_temp'].plot(kind='hist', bins=20, title='Maximum Temperature')
plt.gca().spines[['top', 'right',]].set_visible(False)

#  @title Scatterplot of Global Radiation vs Sunshine
df.plot(kind='scatter', x='sunshine', y='global_radiation', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title Scatterplot of Maximum Temperature vs Global Radiation
df.plot(kind='scatter', x='global_radiation', y='max_temp', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title Scatterplot of Mean Temperature vs Maximum Temperature
df.plot(kind='scatter', x='max_temp', y='mean_temp', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

#visualize "mean_temp" versus "year" and "month"
fig, axs = plt.subplots(1,2, figsize=(10,6))
sns.lineplot(data=df, x='month', y='mean_temp', ax=axs[0])
axs[0].set_title('Mean Monthly Temperatures')

sns.lineplot(data=df, x='year', y='mean_temp', ax=axs[1])
axs[1].set_title('Mean Yearly Temperatures')

plt.tight_layout()
plt.show()

#view correlation between features
corr_matrix = df.corr()
fig, axes = plt.subplots(2,1, figsize=(10,10))

sns.heatmap(corr_matrix[['mean_temp']], ax=axes[0])
axes[0].set_title('Correlation of Features and Mean Temperature')

sns.heatmap(corr_matrix, ax=axes[1])
axes[1].set_title('Correlation of all Features')

"""### Feature Selection
- Select features that are strongly correlated with mean temperature
"""

rel_features = corr_matrix[corr_matrix['mean_temp'] > 0.5].columns

#select relevant features
selected_df = df[rel_features]

#drop rows with missing values in the target variable
selected_df.dropna(subset=['mean_temp'], inplace=True)

"""## Data Preprocessing

- Splitting data into train and test sets
- Handling missing values
- Data Normalisation
"""

#split data
X = selected_df
y = X.pop('mean_temp')
X_train, X_test, y_train, y_test =  train_test_split(X ,y, test_size=0.3, random_state=42)

#pipeline for data preprocessing
preprocess_df = make_pipeline(SimpleImputer(), StandardScaler())

#preprocess training and test set
newX_train = preprocess_df.fit_transform(X_train.drop(columns=['date','year','day']))
newX_test = preprocess_df.transform(X_test.drop(columns=['date','year', 'day']))

"""### Model Tracking and Training

### Model Logging and evaluating with MLflow
"""

mlflow.set_experiment('London Temperature')

for idx, depth in enumerate([1,5,10,20]):
    run_name = f"run_{idx}"

    with mlflow.start_run():
        #Train models
        lr = LinearRegression()
        lr.fit(newX_train,y_train)

        dt = DecisionTreeRegressor(max_depth=depth)
        dt.fit(newX_train, y_train)


        rf = RandomForestRegressor(max_depth=depth)
        rf.fit(newX_train, y_train)


        #calculate RMSE
        mlflow.log_metric("lr_rmse", mean_squared_error(y_test, lr.predict(newX_test),squared=False))
        mlflow.log_metric("dt_rmse", mean_squared_error(y_test, dt.predict(newX_test), squared=False))
        mlflow.log_metric("rf_rmse", mean_squared_error(y_test, rf.predict(newX_test), squared=False))

        # Log the trained model as an artifact
        mlflow.sklearn.log_model(lr, "lr_model", registered_model_name="lrtemp")
        mlflow.sklearn.log_model(dt, "dt_model", registered_model_name="dttemp")
        mlflow.sklearn.log_model(rf, "rf_model", registered_model_name="rftemp")

"""### Searching logged results"""

experiment_results = mlflow.search_runs()
experiment_results

"""## Model Evaluation
- The Random Regressor gives the best result with RMSE of 0.861
"""

# Sort the DataFrame by the metrics columns in ascending order
df_sorted_dt_rmse = experiment_results.sort_values(by='metrics.dt_rmse')
df_sorted_rf_rmse = experiment_results.sort_values(by='metrics.rf_rmse')
df_sorted_lr_rmse = experiment_results.sort_values(by='metrics.lr_rmse')

# Get the best model for each metric
best_model_dt_rmse = df_sorted_dt_rmse.iloc[0]
best_model_rf_rmse = df_sorted_rf_rmse.iloc[0]
best_model_lr_rmse = df_sorted_lr_rmse.iloc[0]

print("Best model based on Decision regressor model:")
print(best_model_dt_rmse['metrics.dt_rmse'])

print("\nBest model based on Random Forest regressor model:")
print(best_model_rf_rmse['metrics.rf_rmse'])

print("\nBest model based on Linear regression model:")
print(best_model_lr_rmse['metrics.lr_rmse'])

#View the random regressor model
client = mlflow.MlflowClient()
dt_filter_string = "name = 'rftemp'"

# Search for Random Forest Regressor Models
print(client.search_registered_models(filter_string=dt_filter_string))

"""### Load Best Model"""

#best model run id
best_model_run_id = best_model_rf_rmse['run_id']

#best model uri
best_model_arti_uri = best_model_rf_rmse['artifact_uri']

#full uri path
best_model_uri  = f'{best_model_arti_uri}/rf_model'

model = mlflow.sklearn.load_model(best_model_uri)
#model = mlflow.pyfunc.load_model(f"runs:/{best_model_run_id}/rf_model")

"""#### Best model version"""

#Get best model version
model_name = "rftemp"

version = client.search_model_versions(f"name='{model_name}'")
[model for model in version if model.run_id == best_model_run_id]

"""#### Parameters of the best model"""

#Get parameters ofm the best model
params = model.get_params()
params

#Dataframe of best Model Parameters
params_df = pd.DataFrame(params.items(), columns=['Parameter', 'Value'])
params_df

"""## Transition Model to Testing and Production Stages

- Random Regressor Model version 3 moved to Production stage
"""

# Transition version 3 of Insurance model to testing stage
client.transition_model_version_stage(name="rftemp", version=3,
        stage="Staging"
    )

# Transition Model to Production
client.transition_model_version_stage(name="rftemp", version=3, stage="Production")

"""###Load Producton Model"""

# Load the Production stage of the Random regressor model
prod_model = mlflow.sklearn.load_model("models:/rftemp/Production")

"""## Testing Production Model

- Production Model has accuracy of 97.7%
"""

prod_model.score(newX_test, y_test)