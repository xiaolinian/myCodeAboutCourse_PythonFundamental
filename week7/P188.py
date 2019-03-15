from PIL import Image
im = Image.open("D:\documents\python_couse\week7\outfile.png")
print(im.format,im.size,im.mode)
try:
    im.save('picframe{:02d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell()+1)
        im.save('picframe{:02d}.png'.format(im.tell()))
except:
    print('处理结束')
    
