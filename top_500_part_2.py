def top_500_list(excel_file):
    import pandas
    from collections import defaultdict

    excel_list = [
        excel_file,
    ]

    top_500_tickers = []

    for excel_file in excel_list:
        slickcharts_df = pandas.read_excel(excel_file, sheet_name = 0)

        tickers = slickcharts_df['Symbol']

        ticker_list = []

        for ticker in tickers:
            ticker_list.append(ticker)
        top_500_tickers = ticker_list[0:500]
    
    return top_500_tickers

