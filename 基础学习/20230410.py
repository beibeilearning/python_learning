from pyecharts.charts import Line
from pyecharts import options
# pyecharts 官方文档
# https://pyecharts.org/#/zh-cn/global_options?id=toolboxopts%ef%bc%9a%e5%b7%a5%e5%85%b7%e7%ae%b1%e9%85%8d%e7%bd%ae%e9%a1%b9
line = Line()
line.add_xaxis(["China", "US", "UK"])
line.add_yaxis("GDP", [30,20,10])

line.set_global_opts(
    title_opts = options.TitleOpts(
        title = "GDP Charts",
        pos_left = "center",
        pos_bottom= "1%"
    ),
    legend_opts = options.LegendOpts(
        is_show = "True"
    ),
    toolbox_opts = options.ToolboxOpts(
        is_show = "True"
    ),
    visualmap_opts = options.VisualMapOpts(
        is_show = "True"
    )

)

line.render()
