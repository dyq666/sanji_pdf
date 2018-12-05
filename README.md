## html 转 pdf 通过 wkhtmltopdf

一个简单的例子, 将已有静态文件转换为 pdf. 

例子有: 自带的目录, 页眉, 页脚, 水印图片

### 使用方式

- python 环境, `pipenv install`
- 安装 wkhtmltopdf `brew install wkhtmltopdf`
- 放一张水印图片在 static/img/watermark.png, 生成方式见下面说明
- 运行 app.py 即可, 生成的 pdf 在 out/ 中

### 其他说明 / 常见问题

- 目录问题

  wkhtmltopdf 自动根据 h 标签生成目录

- 不能在生产环境中直接安装 wkhtmltopdf

  将对应操作系统编译后的 wkhtmltopdf 二进制文件放入 out/ 中(本仓库中放的是 mac 环境下), 参考 app.py 中的注释, 增加一个配置即可.

- 生产环境中无法显示中文

  由于 pdf 是服务端渲染, 需要系统中自带相应的中文字体, 可以选择使用 `@font-face` 指定字体文件代替在环境中直接安装字体, 参考 static/css/main.css.

- control characters 问题

  具体的项目中静态文件可能是通过 lxml 库动态创建的, 在转换字符串是可能会报此错误.

  解决方案: 删除所有 control characters, `re.sub(r'[\x00-\x1f]', '', content)`. 或参考 `utils.py.print_control_chars` 查看项目中 lxml 不支持的, 将所有打印的删除.

- 水印图片

  一个 html 可能会生成多个 pdf 页面, 因此需要一些对图片特殊的处理. 简单的原理就是, 设置一张图片 (主要内容加上透明度, 其余地方为全透明), 使其大小等于 pdf 页面的大小, 利用 css repeat-y 实现背景.

  1. 拿到的图可能是白底的水印图, 可通过 utils.change_opacity 去除白底, 同时可修改其他颜色的透明度
  2. wkhtmltopdf 默认的大小为 (210mm \* 297mm), dpi 96, 同时图片大小要去除设置的 pdf 边距, 可参考 utils.build_watermark
  3. static/css/main.css 中在 body 中设置 repeat-y 相关的背景样式, min-height 与生成的水印图片大小相同.