# 上传照片
- 上传照片和输入文字信息一样，都是通过HTML的<form>实现
- 区别在于：
  - `request.form['name']`获得文字信息，`request.files['name']`获得文档
  - <form>的enctype属性改为multipart/form-data，即：`<form action="/" method="post" enctype="multipart/form-data">`。
  - enctype属性规定在发送到服务器之前应该如何对表单数据进行编码，其中默认的选项为`application/x-www-form-urlencoded`，意思是`在发送前编码所有字符`。修改为`multipart/form-data`，意思是`不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。`

## 实现过程
### 加enctype标签
- 首先，如前所述，在template里<form>标签加上`enctype="multipart/form-data"`属性
  - 刚开始试的时候以为文字和照片需要用不同的enctype属性，折腾了半天，后来发现原来直接都用`enctype="multipart/form-data"`就可以

### 限制上传文件类型
- 参考flask[官方文档](flask.pocoo.org/docs/0.10/patterns/fileuploads/)，增加函数`allowed_file`，从文件名判断上传的文件是否为限定的文件类型
- 这里将文件类型限定为`['png', 'jpg', 'jpeg', 'gif']`

### 获取照片，存到本地
- 获取照片用`request.files['name']`，其中`name`是template里面<input>标签里面name属性对应的值
- 判断是否为正确的图片格式（'png', 'jpg', 'jpeg', 'gif'）
- 用secure_filename来防止filename里面存在相对路径，如`filename = "../../../../home/username/.bashrc"`，这样的文件就可能可以改变服务器的某些文档。用`secure_filename('../../../../home/username/.bashrc')`，返回的文件名为`'home_username_.bashrc'`
- UPLOAD_FOLDER设定图片在本地存储的位置，下一步修改为存到七牛的云存储上面。

## 下一步……
- 照片大小是否要限定？
  - 限定为多少？
  - 还是不限定，上传后服务器后台处理为较小的大小？
- 图片格式错误时的提示怎么设定
- 存储到七牛
  - 实名认证才可以用开发者模式……


## Reference
- flask.pocoo.org/docs/0.10/patterns/fileuploads/
- http://www.w3school.com.cn/tags/att_form_enctype.asp