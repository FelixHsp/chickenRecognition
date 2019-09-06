import os
from PIL import Image

#图片重命名
# dirname_read="/Users/felix/2019/训练/青脚麻鸡/"
# dirname_write="/Users/felix/2019/训练/青脚麻鸡2/"
# names=os.listdir(dirname_read)
# count=0
# for name in names:
#     img=Image.open(dirname_read+name)
#     name=name.split(".")
#     if name[-1] == "png":
#         name[-1] = "jpg"
#         name = str.join(".", name)
#         name = '2_'+name
#         r,g,b,a=img.split()
#         img=Image.merge("RGB",(r,g,b))
#         to_save_path = dirname_write + name
#         img.save(to_save_path)
#         count+=1
#         print(to_save_path, "------conut：",count)
#     else:
#         continue

#图片改为100*100
# def convertjpg(jpgfile,outdir,width=100,height=100):
#     img = Image.open('/Users/felix/2019/训练/qingjiaoma/'+jpgfile)
#     try:
#         new_img = img.resize((width, height), Image.BILINEAR)
#         new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
#     except Exception as e:
#         print(e)
# for jpgfile in os.listdir('/Users/felix/2019/训练/qingjiaoma/'):
#     print(jpgfile)
#     convertjpg(jpgfile, "./qingjiaoma")

