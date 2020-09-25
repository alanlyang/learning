## 核心概念
### container 布局容器
    Bootstrap 需要为页面内容和栅格系统包裹一个 .container 容器，
    - ,container 类用于固定宽度并支持响应式布局的容器
    - .container-fluid 用于 100% 宽度，占据全部视口(viewport)的容器

### 栅格系统
    通过一系列的行(row) 和 列（columnn）的组合来床架你也面布局
    工作原理：
        1、行(row)必须包含在.container（固定宽度）或 .container-fluid中， 方便aligment和padding
        2、通过(row) 在水平方向创建一组 列（column
        3、内容应当放置于列内，并且，只有列可以作为行的子元素
        4、通过为列(column)设置padding属性，从而创建咧欲裂之间的间隔。通过.row元素设置负值margin从而抵消调为.container元素设置的padding。
        5、栅格中的列是通过指定1到12的值来表示其跨越的方位。例如col-xs-4
        6、如果一 row 中包含了的列(column)大于12，则多余的列所在元素将被作为一个整体另起一行排列。
    相关css类
        1、col-sm-offset-* 会将元素的一个列的左外边距margin, 增加*列，范围为1-11

### 表单
    - 1、单独的表单空间会被自动赋予一些 全局样式，所有设置了.form-control类的input, textarea 和 select 元素 豆浆被 默认设置 宽度属性为width: 100%
    - 2、将label和前面提到的控件包裹在.form-group中可以获取最好的排列。
    - 3、通过为表单添加 .form-horizontal类，并联合使用预置的栅格类，可以将label标签和控件组水平并排布局。这样做将会改变.form-group行为，使其表现为栅格系统种的row
    - 4、.form-control表示为input元素添加表单控件

