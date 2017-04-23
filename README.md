# RainbowChart20170423

------RainbowChart.py------
RainbowChart(DATA, String='DATA')
入力データはPandas.DataFrame型で時系列データの必要性
代表的な周期性を仮定してトレンドをグラフ化
DATA：時系列データ（DataFrame）
String：系列名，グラフの保存ファイル名，デフォルトは「DATA」
返り値としてデータを返す
RainbowChart2(DATA, String='DATA')
上記関数のサブプロットバージョン
全データと直近1年のグラフを描画
RainbowChart_shift(DATA, String='DATA')
代表的な周期性を仮定してデータ末尾を揃えてトレンドをグラフ化
DATA：時系列データ（DataFrame）
String：系列名，グラフの保存ファイル名，デフォルトは「DATA」
返り値としてデータを返す
RainbowChart2_shift(DATA, String='DATA')
上記関数のサブプロットバージョン
全データと直近1年のグラフを描画
