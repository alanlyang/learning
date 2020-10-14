/**
 * 使用LocalStorage存储数据
 * 1、函数
 * 2、对象
 * 需要向外暴露一个还是多个功能，一个的话使用函数，两个的话使用对象
 */

//  export用于对外暴露信息

const TODOS_KEY = "todos_key"

export default {
    saveTodos(todos){
        window.localStorage.setItem(TODOS_KEY, JSON.stringify(todos))
    },
    readTodos() {
        return JSON.parse(window.localStorage.getItem(TODOS_KEY) || "[]")
    }
}
