## 项目介绍

一个将已有静态文件转换为 pdf 的例子.

例子有: 自带的目录, 页眉, 页脚, 水印图片

### 使用

- 系统中安装 wkhtmltopdf `brew install wkhtmltopdf`
- 运行 app.py 即可, 生成的 pdf 在 out/ 中

## 代码与常见问题

### 目录

  自动根据 `h 标签` 生成目录

### 中文乱码

  由于 pdf 是实时渲染, 需要生成时的系统中自带相应的中文字体, 为了确保生产环境和开发环境保持一致, 
  可以在代码仓库中存储字体文件, 并使用 `@font-face`, 具体实现在 `static/css/main.css:@font-face`.

### 水印图片

  一个 html 可能会代表成多个 pdf 页面, 因此需要一些特殊处理. 原理是设置一张与 pdf 单页大小相同的透明背景的图片,
  然后利用 css `repeat-y` 实现背景, 详细说明如下:

  1. 图片必须是透明背景, 如果是白底的水印图可通过 `util.change_opacity` 将白底转为透明色.
  2. 然后用 `util.build_watermark` 生成一张水印图.
  3. static/css/main.css 中在 body 中设置 repeat-y 相关的背景样式, min-height 与生成的水印图片大小相同.