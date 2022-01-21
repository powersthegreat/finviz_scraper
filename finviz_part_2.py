import pandas
import time
from collections import defaultdict
from top_500_part_2 import top_500_list

ticker_list = top_500_list("sp500.xlsx")
ticker_list_practice = ticker_list[0:5]

empty_list = []
for i in range(0, len(ticker_list_practice)):
    empty_list.append("")

ticker_items_dict = dict(zip(ticker_list_practice, empty_list))

for ticker in ticker_list_practice:
    finviz_df = pandas.read_excel('finviz.xlsx', sheet_name = ticker)
    item_1 = finviz_df[1][1]
    ticker_items_dict[ticker] = item_1
    item_2 = finviz_df[1][2]
    item_3 = finviz_df[1][3]
    item_4 = finviz_df[1][4]
    item_5 = finviz_df[1][5]
    ticker_items_dict[ticker] = [ticker_items_dict[ticker]]
    ticker_items_dict[ticker].append(item_2)
    ticker_items_dict[ticker].append(item_3)
    ticker_items_dict[ticker].append(item_4)
    ticker_items_dict[ticker].append(item_5)
    

