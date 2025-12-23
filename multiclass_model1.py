import pandas as pd

df = pd.read_csv(r"C:\Users\BIT\Desktop\GitHub\AgriAid\DATA\crop_yield_weather.csv")
jharkhand_crops = [
    "Rice", "Wheat", "Maize", "Arhar", "Urad", "Moong", "Gram",
    "Mustard", "Niger", "Til", "Sesame", "Groundnut"
]

filtered_df = df[df['Crop'].isin(jharkhand_crops)]
selected_columns = [
    'Soil_Type', 'Rainfall_mm', 'Temperature_Celsius', 'Weather_Condition', 'Crop'
]
model_df = filtered_df[selected_columns].copy()


# Encoding catagorical data
from sklearn.preprocessing import LabelEncoder

soil_encoder = LabelEncoder()
weather_encoder = LabelEncoder()
crop_encoder = LabelEncoder()

model_df['Soil_Type'] = soil_encoder.fit_transform(model_df['Soil_Type'])
model_df['Weather_Condition'] = weather_encoder.fit_transform(model_df['Weather_Condition'])
model_df['Crop'] = crop_encoder.fit_transform(model_df['Crop'])


# Splitting the dataset
from sklearn.model_selection import train_test_split
X = model_df.drop('Crop', axis=1)
y = model_df['Crop']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# Training XGBoost Model
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

model = XGBClassifier(
    tree_method='gpu_hist',  
    n_estimators=300,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)


# Model Evaluation
print("Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=crop_encoder.classes_))


# Confusion Matrix
disp = ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, display_labels=crop_encoder.classes_, cmap='Greens', xticks_rotation=90)
plt.title("Confusion Matrix - Jharkhand Crop Prediction (GPU Model)")
plt.tight_layout()
plt.savefig("Cmatrix_multiclass_model1.png", dpi=300)
plt.show()


# Feature Importance
plt.figure(figsize=(8,5))
plt.bar(X.columns, model.feature_importances_, color='teal')
plt.title("Feature Importance - Jharkhand Crop Prediction")
plt.ylabel("Importance Score")
plt.xlabel("Feature")
plt.show()
