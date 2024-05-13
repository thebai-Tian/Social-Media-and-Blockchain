import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam


# 数据加载
data = pd.read_csv('/path_to_your_file.csv')  # 修改为你的文件路径

# 时间特征处理
data['CreatedAt'] = pd.to_datetime(data['CreatedAt'], unit='s')
data['hour'] = data['CreatedAt'].dt.hour
data['day_of_week'] = data['CreatedAt'].dt.dayofweek

# 类别特征处理
sentiment_ohe = OneHotEncoder()
sentiments = sentiment_ohe.fit_transform(data[['Sentiment']]).toarray()
sentiment_columns = sentiment_ohe.get_feature_names(['Sentiment'])
sentiment_df = pd.DataFrame(sentiments, columns=sentiment_columns)

# 合并处理过的特征
data = pd.concat([data, sentiment_df], axis=1)

# 丢弃原始的类别特征和时间戳
data.drop(['CreatedAt', 'Sentiment'], axis=1, inplace=True)

# 目标变量和特征分离
X = data.drop('price', axis=1)
y = data['price']

# 数据规范化
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
y = np.array(y).reshape(-1, 1)
y_scaled = scaler.fit_transform(y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# 为LSTM调整数据形状
X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

# 创建模型
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(1))

# 编译模型
model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=2)
