def get_candle_by_index(df, index):
    return {
        'open': df['Open'].iloc[index].item(),
        'high': df['High'].iloc[index].item(),
        'low': df['Low'].iloc[index].item(),
        'close': df['Close'].iloc[index].item(),
        'volume': df['Volume'].iloc[index].item(),
        'timestamp': df.index[index],
    }

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain/loss
    return 100 - (100 / (1 + rs))

def calculate_macd(prices, fast=12, slow=26, signal=9):
    ema_fast = prices.ewm(span=fast).mean()
    ema_slow = prices.ewm(span=slow).mean()

    macd = ema_fast - ema_slow
    macd_signal = macd.ewm(span=signal).mean()
    macd_histogram = macd - macd_signal
    return macd, macd_signal, macd_histogram

def calculate_bollinger_bands(prices, period=20, std_dev=2):
    sma = prices.rolling(window=period).mean()
    std = prices.rolling(window=period).std()

    upper_band = sma + (std * std_dev)
    lower_band = sma - (std * std_dev)

    return upper_band, lower_band

def calculate_tecnical_indicators(df):
    rsi = calculate_rsi(df['Close'])
    rsi = rsi.iloc[-1].item()

    macd, macd_signal, macd_histogram = calculate_macd(df['Close'])
    macd = macd.iloc[-1].item()
    macd_signal = macd_signal.iloc[-1].item()
    macd_histogram = macd_histogram.iloc[-1].item()

    upper_band, lower_band = calculate_bollinger_bands(df['Close'])
    upper_band = upper_band.iloc[-1].item()
    lower_band = lower_band.ilob[-1].item()

    return {
        'rsi': rsi, 
        'macd': macd, 
        'signal': macd_signal,
        'histogram': macd_histogram,
        'upper': upper_band,
        'lower': lower_band 
    }