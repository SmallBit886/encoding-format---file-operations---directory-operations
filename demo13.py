#with实现图片的复制

with open('logo.png','rb') as src_file:
    with open('copy2.png','wb') as target_file:
        target_file.write(src_file.read())
