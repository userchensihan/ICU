from PIL import Image,ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES=True#是否加载截断的图像文件
#Whether or not to load truncated image files.
Image.MAX_IMAGE_PIXELS=None
#To protect against potential DOS attacks caused by decompression bombs Pillow will issue a if the number of pixels in an image is over a certain limit MAX_IMAGE_PIXELS=None
#为了防止由解压缩炸弹引起的潜在DOS攻击,如果图像超过特定限制MAX_IMAGE_PIXELS,Pillow将发出DecompressionBombWaring
from PIL.ExifTags import TAGS
import sys
import os
import exiftool
q=['.jpeg','.png','.jpg']
p=['.mp4','.wav','.avi','.mov','.wmv']
def GPSInfo(jpg):
    f=Image.open(jpg)#打开并标识给定的图像文件
    #Opens and Identifies the given image file
    g=f._getexif().items()#_getexif从图像中获取EXIF数据,结果是一个EXIF对象
    #Gets EXIF data from the image returns an exif object
    #The format returned by Pillow 3.0 has been abandoned
    #Pillow 3.0返回的格式已被放弃
    u={}
    for l,k in g:
        u[TAGS.get(l)]=k
    #
    h=u['GPSInfo']
    n=float(h[2][0])+float(h[2][1])/60+float(h[2][2])/3600
    s=float(h[4][0])+float(h[4][1])/60+float(h[4][2])/3600
    print(f"{n}\t{s}\t{u['DateTimeOriginal']}\t{jpg}")
    #DateTimeOriginal is the time the image was created.
    #DateTimeOriginal是创建映像的时间
    f.close()
    #如果可以,关闭文件指针
    #Closes the file pointer,if possible
if __name__=="__main__":
    for u in os.listdir(path=os.getcwd()):
        #getcwd返回表示当前工作目录的字符串
        #return a string representing the current working directory
        #listdir返回一个包含由path指定目录中条目名称组成的列表,该列表按任意顺序排列,并且不包含特殊条目'.'和'..'
        #return a list containing the names of the entries in the directory given by path The list is in arbitray order,and does not include the '.' or '..'
        m=os.path.splitext(u)[1].lower()
        #将路径名称path拆分为(root,ext),使得root+ext==path,并且扩展名ext为空或以句点打头并最多只包含一个句点
        #split the pathname into a pair (root,ext) such that root+ext==path,and the extension,ext,is empty or begin with a period and contains at most one period
        
        if m in q:
            try:
                GPSInfo(u)
            except AttributeError:
                pass
        elif m in p:
            try:
                c=exiftool.ExifToolHelper().get_metadata(u)
                #return all metadata for the given files
                #返回给定文件的所有元数据
                print(f"{c[0]['Composite:GPSPosition']}\t{u}")
            except KeyError:
                pass
