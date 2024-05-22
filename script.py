import pandas as pd
import yfinance as yf
from adtk.detector import ThresholdAD
from adtk.data import validate_series
from adtk.visualization import plot

# Load and prepare the data
data = pd.read_csv("datasets/temp.csv")
data['Date'] = pd.to_datetime(data['Date'])
data = data.set_index("Date")
data = data["Mean"]

# Validate the series
data = validate_series(data)

# Define and use the threshold anomaly detector
threshold_detector = ThresholdAD(low=0.5, high=0.75)
anomalies = threshold_detector.detect(data)

# Print the anomalies
print(anomalies)

# Optionally, plot the anomalies
plot(data, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_color='red', anomaly_tag="marker")
