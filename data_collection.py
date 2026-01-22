import pandas as pd
import yfinance as yf

TICKERS = ["AAPL", "AMZN", "KR", "ACI", "JBLU", "SPY"]
START_DATE = "2023-06-01"
END_DATE = "2025-01-15"
OUT_CSV = "prices_close_or_adjclose.csv"

def pick_price_panel(df: pd.DataFrame) -> pd.DataFrame:
    """
    yfinance can return:
      - MultiIndex columns: ('Adj Close','AAPL') etc.
      - SingleIndex columns (rare)
    This function chooses 'Adj Close' if present, otherwise 'Close'.
    """

    # If no data came back at all:
    if df is None or df.empty:
        raise ValueError("No data returned from yfinance. Check tickers/internet/date range.")

    # Case 1: MultiIndex columns (most common)
    if isinstance(df.columns, pd.MultiIndex):
        top_level = df.columns.get_level_values(0).unique().tolist()
        print("Top-level columns returned:", top_level)

        field = "Adj Close" if "Adj Close" in top_level else "Close" if "Close" in top_level else None
        if field is None:
            raise KeyError(f"Neither 'Adj Close' nor 'Close' found. Available: {top_level}")

        panel = df[field].copy()
        panel.index.name = "Date"
        return panel

    # Case 2: Single-level columns (fallback)
    print("Columns returned:", df.columns.tolist())
    if "Adj Close" in df.columns:
        panel = df[["Adj Close"]].copy()
        panel.columns = ["PRICE"]
    elif "Close" in df.columns:
        panel = df[["Close"]].copy()
        panel.columns = ["PRICE"]
    else:
        raise KeyError(f"No 'Adj Close' or 'Close' column found. Columns: {df.columns.tolist()}")

    panel.index.name = "Date"
    return panel

def main():
    df = yf.download(
        TICKERS,
        start=START_DATE,
        end=END_DATE,
        progress=False,
        group_by="column"  # tends to standardize output
    )

    prices = pick_price_panel(df)

    # Drop rows where all tickers are missing (non-trading days etc.)
    prices = prices.dropna(how="all")

    prices.to_csv(OUT_CSV)
    print(f"Saved: {OUT_CSV}")

if __name__ == "__main__":
    main()

