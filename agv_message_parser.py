import re
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import row
import pandas as pd

# 예시 메시지
message = "Alice: 10, 11, 112 | Bob: 15, 15, 10 | Carol: 20"

# 메시지 파싱 함수
def parse_message(message):
    data = re.findall(r'(\w+):\s*((?:\d+(?:,\s*)?)+)', message)
    parsed_data = []
    for name, values_str in data:
        values = [int(v) for v in values_str.split(',')]
        parsed_data.append((name.strip(), values))
    return parsed_data

if __name__ == '__main__':
    parsed_data = parse_message(message)
    print(parsed_data[1][1])
    print(len(parsed_data))
