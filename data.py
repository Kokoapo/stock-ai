import yfinance as yf
from utils import get_candle_by_index, calculate_tecnical_indicators
    
def get_data_network1(ticker='USDBRL=X', interval='5m'):
    df = yf.download(
        tickers=ticker,
        period='1d',
        interval=interval,
        prepost=True
    )

    if len(df) < 50:
        print(f'Dados Insuficientes! ${len(df)}')
        return None
    
    previous_candle = get_candle_by_index(df, -2)
    current_candle = get_candle_by_index(df, -1)
    tecnical_indicators = calculate_tecnical_indicators(df)

    return { 'previous': previous_candle, 'current': current_candle, 'ti': tecnical_indicators }

data = get_data_network1()