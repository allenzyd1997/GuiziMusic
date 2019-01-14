export default {
    second2: 0, // 当前歌曲播放到多少毫秒
    gdtimer: '', // 歌词滚动的定时器
    height: 20, // 每一行歌词的高度
    obj: {}, // 解析歌词后的对象
    obj2: {}, // 备份obj
    // 字符串转换成秒
    parse2 (stri) {
      var arr = stri.split(':')
      var num = 0
      num = parseInt(arr[0]) * 60 + parseFloat(arr[1])
      return num
    },
    // 解析歌词
    parse (str) {
      var arr1 = []
      var arr2 = []
      this.obj = {
        time: [],
        content: []
      }
      this.obj2 = {
        time: [],
        content: []
      }
      arr1 = str.split('[')
      arr1.forEach((value, index) => {
        if (index > 0) {
          arr2 = arr2.concat(value.split(']'))
        }
      })
      arr2.forEach((value, index) => {
        if (index % 2 === 0) {
          this.obj.time.push(this.parse2(value))
          this.obj2.time.push(this.parse2(value))
        } else {
          this.obj.content.push(value)
          this.obj2.content.push(value)
        }
      })
    },
    // 将歌词添加到 P 标签中
    addcontent (conp) {
      this.obj.content.forEach((value, index) => {
        conp.innerHTML = conp.innerHTML + value + '<br>'
      })
    },
    // 实现歌词滚动
    gundong (conp) {
      this.gdtimer = setInterval(() => {
        var myaudio = document.querySelector('#main-audio')
        // console.log(myaudio.currentTime)
        this.second2 = myaudio.currentTime
        // this.second2 = this.second2 + 10
        if (this.second2 >= this.obj2.time[0]) {
          // 删除time数组中已经过的时间
          this.obj2.time.shift()
          console.log(this.second2, this)
          // 获取 p标签的top值
          var top = window.getComputedStyle(conp).top
          this.startMove(conp, {
            top: parseInt(top) - this.height
          })
        }
        if (this.obj2.time.length <= 0) {
          this.second2 = 0
          this.lyticsEnd(conp)
          // clearInterval(this.gdtimer)
        }
      }, 50)
    },
    // 暂停歌词
    pause () {
      if (this.gdtimer !== '') {
        clearInterval(this.gdtimer)
        // console.log(this.obj)
      }
    },
    // 歌曲放完,重置该对象
    lyticsEnd (conp) {
      this.pause()
      conp.innerHTML = ''
      conp.style.top = this.height + 'px' // 大坑。单位必须带
      this.obj = {}
      this.obj2 = {}
      this.second2 = 0
      console.log('重置该对象成功', this)
    },
    // 运动函数
    startMove (obj, json, fnEnd) {
      var that = this
      clearInterval(obj.timer)// 先清除之前的定时器
      obj.timer = setInterval(function () {
        var bStop = true// 假设所有的值都到了
        for (var attr in json) { // 遍历json属性
          var cur = (attr === 'opacity') ? Math.round(parseFloat(that.getStyle(obj, attr)) * 100) : parseInt(that.getStyle(obj, attr))// 对opacity 特殊处理
          var speed = (json[attr] - cur) / 6
          speed = speed > 0 ? Math.ceil(speed) : Math.floor(speed) // speed 数字转化，防止不能到达目标的bug
          if (cur !== json[attr]) bStop = false// 如果没有达到目标值，则bStop设为false;
          if (attr === 'opacity') {
            obj.style.filter = 'alpha(opacity=' + (cur + speed) + ')'
            obj.style.opacity = (cur + speed) / 100
          } else {
            obj.style[attr] = cur + speed + 'px'
          }
        }
        if (bStop) {
          clearInterval(obj.timer)
          if (fnEnd) fnEnd() // 执行回调函数
        }
      }, 30)
    },
    getStyle (obj, name) {
      return obj.currentStyle ? obj.currentStyle[name] : window.getComputedStyle(obj, null)[name]
      // 浏览器兼容性处理，注意getComputedStyle为只读属性
    },
    getByClass (oParent, sClass) {
      var aEle = oParent.getElementsByTagName('*')
      var aResult = []
      var re = new RegExp('\\b' + sClass + '\\b', 'i')
      for (var i = 0; i < aEle.length; i++) {
        if (re.test(aEle[i].className)) aResult.push(aEle[i])
      }
      return aResult
    }
  }

  