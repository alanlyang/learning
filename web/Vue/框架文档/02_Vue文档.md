### 创建vue项目
    - npm insatll -g vue-cli
    - vue init webpack vue_demo
       init后提供了六种模板名称
        - cd vue_demo
        - npm install
        - npm run dev
        - 访问 localhost:8080

### 打包
    npm run build 生成打包文件dist

### 发布1： 使用静态服务器 工具包
    npm install  -g serve
    serve dist
    访问localhost:5000 

### 发布2： 使用动态服务器tomcat  （apache）
    修改配置 webpack.prod.conf.js
    output: {
        publicPath: '/xxx/' 打包的文件夹名称
    }

    重新打包
    npm run build

    修改dist文件夹为项目名称 ： xxx
    将xxx拷贝到运行的tomcat的webapps目录下
    访问: http://localhost:8080/xxx

### EsUnit 
    - 代码规范检验组件, 和python的PEP8类似
    - 本质上是一个规则池


### 组件间通讯
    Vue主要有以下几种组件间的通讯方式
    组件通信其实就是组件间的数据传递
    - props/$emit
    - $parent / $children及ref
    - $emit/ $on
    - vuex
    - $attrs/ $listeners
    - provide / inject

    使用原则：
        - 1、当项目较大时，通常选用vuex
        - 2、应当有节制的使用$parent和$children，他们的主要目的是作为访问组件的应急方法
        - 3、推荐使用Props和events实现父子组件间通讯
        - 4、如果仅传递数据，可以用$attrs/$listeners
        - 5、如果不仅仅传递数据，还做中间处理，建议使用vuex


## 插件Vuex
    - vuex 应用的核心是store(仓库)
    - store基本上就是一个容器，其中包含大部分的状态state.
    - Vuex和全局对象的区别
      - 1、vuex的状态存储是响应式的，当Vue组件从store种读取状态时，若 store中的状态发生变化，那么相应的组件也会得到高效更新
      - 2、不能直接修改store中的状态，改变store的唯一途径就是显式的调用commiit mutation

## 插件编辑器
    vue2-editor 是一个富文本编辑器，主要用来进行文章的编辑
    mavenEditor/vue-markdown 是markdown编辑器