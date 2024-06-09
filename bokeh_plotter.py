from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from random import randrange
import numpy as np

# 초기 데이터 생성
num_points = 100
data = {'x': np.linspace(0, 10, num_points)}
data.update({f'y_{i}': np.random.rand(num_points) for i in range(14)})  # 14가지 종류의 랜덤 데이터
source = ColumnDataSource(data=data)

# 그래프 생성
plot = figure()
lines = []
for i in range(14):
    line = plot.line(x='x', y=f'y_{i}', source=source)
    lines.append(line)

# 새 데이터를 생성하고 업데이트하는 함수
def update():
    new_data = {'x': np.linspace(0, 10, num_points)}
    new_data.update({f'y_{i}': np.random.rand(num_points) for i in range(14)})
    source.data = new_data

# 주기적으로 그래프를 업데이트하는 함수 등록
curdoc().add_periodic_callback(update, 1000)  # 1초마다 업데이트

# Bokeh 애플리케이션 실행
curdoc().add_root(plot)

# Bokeh 서버 실행
if __name__ == '__main__':
    from bokeh.server.server import Server
    from tornado.ioloop import IOLoop

    server = Server({'/': curdoc()}, io_loop=IOLoop(), port=5000)
    server.start()
    IOLoop().start()
