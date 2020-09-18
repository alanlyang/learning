## plt.savefig()
    - 用来保存图片到本地文件
    - 参数：
      - fname： 文件名
      - dpi： 以每英寸点数表示分辨率
      - bbox_inches: bbox英寸，只保留图形的给定部分
      - padding_indches: 当bbox_inches紧时，数字周围的天冲凉


## plt.imshow()
    - 热图形式(heatmap), 通过色差、亮度来展示数据的差异
    - 参数：
      - X： 图像数据，接受数组形式
      - cmap: 将标量数据映射到色彩图，默认为rc : image.cmap
      - norm: 如果使用scalar data， 则会进行[0, 1]的数值缩放
      - aspect: 控制轴的纵横比
        - equal: 确保宽高比为1：1，像素为正方形
        - auto： 更改图像宽高比以匹配轴的宽高比，通常将导致非方形像素
      - interpolation: 是否使用插值方法
      - alpha: 透明值， 0-1之间
      - origin: （0，0）坐标的位置
        - upper: 左上角： 通常用于矩阵和图像
        - lower: 左下角
  
## plt.imsave()
    - 用于保存图像，通过修改out_path的后缀名，可以修改图片类型
    - plt.imsave(path, image)