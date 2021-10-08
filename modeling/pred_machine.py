import os
import time
import schedule
import sqlite3
import pandas as pd
import numpy as np
import tensorflow as tf
from fbprophet import Prophet
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Conv1D, Lambda
from tensorflow.keras.losses import Huber
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

os.environ['TF_CPP_MIN_LEVEL'] = '2'

class Prediction:
    def load_data(self, stock_name):
        conn = sqlite3.connect('./stock.db')
        c = conn.cursor()
        stock_df = pd.read_sql('SELECT * FROM {}'.format(stock_name), con=conn)
        c.close()
        return stock_df

    def windowed_dataset(self, series, window_size, batch_size, shuffle):
        series = tf.expand_dims(series, axis=-1)
        ds = tf.data.Dataset.from_tensor_slices(series)
        ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
        ds = ds.flat_map(lambda w: w.batch(window_size + 1))
        if shuffle:
            ds = ds.shuffle(1000)
        ds = ds.map(lambda w: (w[:-1], w[-1]))
        return ds.batch(batch_size).prefetch(1)

    def pred_machine(self, stock_name_list):
        predic = Prediction()
        global merged_data

        merged_data = pd.DataFrame()

        for stock_name in stock_name_list:

            data = predic.load_data(stock_name)

            data['nasdaq'] = data['nasdaq'].str.replace(',', '').astype(float)
            data['sp'] = data['sp'].str.replace(',', '').astype(float)
            data['exchangerate'] = data['exchangerate'].str.replace(',', '').astype(float)
            data.replace('-', np.nan, inplace=True)
            data.fillna(method='ffill', inplace=True)

            scaler = MinMaxScaler()
            scale_cols = list(data.columns[1:])
            scaled = scaler.fit_transform(data[scale_cols])
            df = pd.DataFrame(scaled, columns=scale_cols)
            x_train, x_test, y_train, y_test = train_test_split(df.drop('y', 1), df['y'], test_size=0.2, random_state=0, shuffle=False)

            WINDOW_SIZE=120
            BATCH_SIZE=32

            train_data = predic.windowed_dataset(y_train, WINDOW_SIZE, BATCH_SIZE, True)
            test_data = predic.windowed_dataset(y_test, WINDOW_SIZE, BATCH_SIZE, False)

            model = Sequential([
              Conv1D(filters=32, kernel_size=5,
                    padding="causal",
                    activation="relu",
                    input_shape=[WINDOW_SIZE, 1]),
              LSTM(16, activation='tanh'),
              Dense(16, activation="relu"),
              Dense(1),
            ])

            loss = Huber()
            optimizer = Adam(0.0005)
            model.compile(loss=Huber(), optimizer=optimizer, metrics=['mse'])

            earlystopping = EarlyStopping(monitor='val_loss', patience=100, mode='min')
            filename = os.path.join('tmp', 'ckeckpointer.ckpt')
            checkpoint = ModelCheckpoint(filename,
                                      save_weights_only=True,
                                      save_best_only=True,
                                      monitor='val_loss',
                                      verbose=1)

            history = model.fit(train_data,
                              validation_data=(test_data),
                              epochs=500,
                              callbacks=[checkpoint, earlystopping])

            for i in range(10):
                merge_data = pd.DataFrame()
                for col in data:
                    if col != 'date' and col != 'y':
                        data_copy = data[['date', col, 'date']].copy()
                        data_copy.columns = ['ds', 'y', 'date']
                        data_copy = data_copy.set_index('date')

                        prophet = Prophet(seasonality_mode='multiplicative',
                                          yearly_seasonality=True,
                                          weekly_seasonality=True, daily_seasonality=True,
                                          changepoint_prior_scale=0.5)
                        prophet.fit(data_copy)

                        future_data = prophet.make_future_dataframe(periods=1, freq='d')
                        forecast_data = prophet.predict(future_data)
                        forecast_copy = pd.DataFrame(forecast_data[['ds', 'yhat']].tail(1))
                        forecast_copy.columns = ['date', col]

                        merge_data[col] = forecast_copy[col]
                merge_data['date'] = forecast_copy['date']
                df_row = pd.concat([data, merge_data])

                pred_scaled = scaler.fit_transform(df_row[scale_cols])
                pred_df = pd.DataFrame(pred_scaled, columns=scale_cols)
                p_x_train, p_x_test, p_y_train, p_y_test = train_test_split(pred_df.drop('y', 1), pred_df['y'], test_size=0.2, random_state=0, shuffle=False)
                WINDOW_SIZE=120
                BATCH_SIZE=32

                pred_train = predic.windowed_dataset(p_y_train, WINDOW_SIZE, BATCH_SIZE, True)
                pred_test = predic.windowed_dataset(p_y_test, WINDOW_SIZE, BATCH_SIZE, False)

                pred = model.predict(pred_test)
                pred_df.iloc[-1]['y'] = pred[-1]

                data = scaler.inverse_transform(pred_df)
                data = pd.DataFrame(data, columns=scale_cols)
                data['date'] = df_row['date']
                data = data[['date', 'volume', 'per', 'pbr', 'institution', 'corp', 'retail', 'foreign', 'atr',
                   'nasdaq', 'sp', 'cboe', 'exchangerate', 'futures2y', 'futures10y',
                   'y']]

            merged_data[stock_name] = data.iloc[-11:, -1]

# pred_machine()
# schedule.every().hour.do(pred_machine)
# schedule.every().day.at("6:00").do(pred_machine)
#
# while True:
#     schedule.run_pending()
#     print(data)
#     time.sleep(3600)
