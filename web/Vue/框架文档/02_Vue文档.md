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

## localStorage
    可以用来进行本地数据存数，也就是存成文件
    存储的数据将会保存在浏览器的会话中.
    localStorage类似于SessionStorage,区别在于存储在LocalStorage的数据可以长期进行保存,而当页面会话结束时，sessionStorage的数据会被清除
    无论LocalStorage还是SessionStorage，他们都存在于特定的页面协议中

    LocalStorage中的键值对总是以字符串的形式存储
    支持的方法为:
     setItem(): 增加一个数据项目
     getItem()： 获取一个数据项目
     removeItem()： 删除一个数据项目
     clear()： 清除所有的数据项目

     查看可以在检查工具---> application ---> storage ---> localStorage中查看

## 自定义事件
    事件有两个动作，一个是绑定，一个是触发
    使用v-on 绑定自定义事件
    使用v-emit 监听自定义事件

    也可以
        使用 $on(eventname)监听事件, 但是一般上我们都使用 @eventName的形式绑定监听
        使用 $emit(eventName, optionalPayload)触发事件
    
    注意，使用@或者自定义方法的形式主要用于父子组件之间的通信
    子孙之间的通信还是要靠方法的传递

## vm.$refs 和 ref
    $refs里包含所有注册过的子组件
    ref 用来给元素或者子组件注册引用信息

## 消息的订阅与发布
    npm  install --save pubsub-js

    绑定事件监听 === 订阅消息
    触发事件 === 发布消息

    发送消息， Pubsub.publish(名称，参数)
    订阅消息, Pubsub.subscribe(名称， 函数)
    取消订阅, Pubsub.unsubscribe(名称)

    订阅和发布的好处就是对于组件通信的位置没有任何要求,可以是父子，也可以是祖先

## Vue进行ajax请求
    需要使用到两个库
    一个是非官方的库，叫vue-resource], 用于 vue 1.x , 现在已经很少用了
    一个是官方推荐的库， 叫 axios

    Vue使用插件需要进行声明
    Vue.use(VueResource), 一旦声明使用插件, vm会给vm对象和组件对象添加一个$http属性
    该属性具有 Get 和 Post两个方法

    axios 在哪里使用就在哪里引入

## v-for
    v-for 支持接受第二个参数 index, index特指当前项的索引
    在使用v-for时，必须为每个对象附加一个唯一的key, 用来帮助vue唯一追踪当前数据的状态