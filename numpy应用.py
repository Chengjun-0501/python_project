from PIL import Image
import numpy as np
import os

def image_Open(path:str):   #读取图片，指定参数类型为str
    __image_read = Image.open(path)   #打开图片
    __image_tf = np.array(__image_read)   #转换为三维数组
    return __image_tf

def image_ShowResolution(image):   #显示图片分辨率，指定参数类型为ndarray
    try:
        print(f'该图片分辨率为 {image.shape[1]}X{image.shape[0]}\r\n')
        return
    except AttributeError:
        pass

def image_Turn(image):   #翻转图片，指定参数类型为ndarray
    try:
        print('以下为可选的图片翻转方式:')
        print('\t\t1.上下翻转')
        print('\t\t2.左右翻转')
        print('\t\t3.对向翻转')
        chose = int(input('请输入想要进行的操作【输入对应的数字即可】:'))
        if chose == 1:   #上下翻转
            __image_turned = image[::-1,:,:]
            __image_show = Image.fromarray(__image_turned)   #numpy转image
            __image_show.show()
            return __image_turned
        elif chose == 2:   #左右翻转
            __image_turned = image[:,::-1,:]
            __image_show = Image.fromarray(__image_turned)
            __image_show.show()
            return __image_turned
        elif chose == 3:   #对向翻转
            __image_turned = image[::-1,::-1,:]
            __image_show = Image.fromarray(__image_turned)
            __image_show.show()
            return __image_turned
        else:
            raise Exception
    except:
        print('请输入指定的数字！\r\n')

def image_Cut(image):   #裁剪图片,指定参数类型为ndarray
    try:
        print('以下为可选的图片裁剪方式:')
        print('\t\t1.水平方向裁剪')
        print('\t\t2.垂直方向裁剪')
        __image_cut = int(input('请输入想要选择的裁剪方式【输入对应的数字即可】:'))
        if __image_cut == 1:
            print('请输入想要裁剪的区间:')
            __wight_1 = int(input('请输入左区间:'))
            __wight_2 = int(input('请输入右区间:'))
            __image_cutted = image[:, __wight_1:__wight_2, :]
            __image_show = Image.fromarray(__image_cutted)
            __image_show.show()
            return __image_cutted
        elif __image_cut == 2:
            print('请输入想要裁剪的区间:')
            __height_1 = int(input('请输入上区间:'))
            __height_2 = int(input('请输入下区间:'))
            __image_cutted = image[__height_1:__height_2,:,:]
            __image_show = Image.fromarray(__image_cutted)
            __image_show.show()
            return __image_cutted
    except:
        print('请正确输入区间！\r\n')

def image_Compress(image):   #水平方向压缩，指定参数类型为ndarray
    print('以下为可选的压缩方向:')
    print('\t\t1.水平方向压缩')
    print('\t\t2.垂直方向压缩')
    __image_compress = int(input('请输入想要选择的压缩方向【输入对应的数字即可】:'))
    if __image_compress == 1:
        image_com = int(input('请输入压缩倍数:'))
        __image_Com = image[:,::image_com,:]
        __image_show = Image.fromarray(__image_Com)
        __image_show.show()
        return __image_Com
    elif __image_compress == 2:
        image_com = int(input('请输入压缩倍数:'))
        __image_Com = image[::image_com, :, :]
        __image_show = Image.fromarray(__image_Com)
        __image_show.show()
        return __image_Com

def image_Control(self,image):   #调节图片亮度，指定参数类型为int and ndarray
    __image_Con = image * self
    __image_Con_clip = Image.fromarray(np.clip(__image_Con,None,255))   #裁剪所有超出RGB像素值的数
    __image_Con_clip.show()
    return __image_Con_clip

def image_Save(path:str,name:str,image):   #保存图片，指定参数类型为str and ndarray

    try:
        if not os.path.exists(path):  #如果该目录不存在则创建
            os.mkdir(path)
        if os.path.exists(os.path.join(path,name)):
            raise ValueError('该目录下已有同名文件！')
        d = Image.fromarray(np.uint8(image))
        d.save(os.path.join(path,name))
        # with open(os.path.join(path,name), 'w') as f:
        #     f.write(image.shape)
        print('保存成功！\r\n')
        return
    except:
        print('请正确输入路径与文件名！\r\n')

def image_SaveChose(image):   #选择是否保存图片
    while 1:
        try:
            print('是否保存该图片？请输入y/n进行选择:')
            __chose_1 = str(input())
            if __chose_1 == 'Y' or __chose_1 == 'y':
                path = str(input('请输入想要保存的路径:'))
                name = str(input('请输入想要设置的文件名'))
                image_Save(path,name,image)
                break
            elif __chose_1 == 'N' or __chose_1 == 'n':
                break
            else:
                raise ValueError
        except:
            continue

def main():
    while 1:
        print('------------------------------')
        print('功能清单:')
        print('\t\t1.显示分辨率')
        print('\t\t2.翻转图片')
        print('\t\t3.裁剪图片')
        print('\t\t4.压缩图片')
        # print('\t\t5.调节亮度')
        print('\t\t5.退出')
        print('\t\t6.开发者信息')
        print('------------------------------')
        try:
            num = int(input('请选择想要进行的操作【输入对应的数字】:'))
        except ValueError:
            print('请正确输入数字！\r\n')
            continue
        try:
            if num == 1:
                image_path = str(input('请输入目标图片所在地址:'))
                image_self = image_Open(image_path)
                image_ShowResolution(image_self)
            elif num == 2:
                image_path = str(input('请输入目标图片所在地址:'))
                image_self = image_Open(image_path)
                __image_return = image_Turn(image_self)
                image_SaveChose(__image_return)
            elif num == 3:
                image_path = str(input('请输入目标图片所在地址:'))
                image_self = image_Open(image_path)
                image_ShowResolution(image_self)
                __image_return = image_Cut(image_self)
                image_SaveChose(__image_return)
            elif num == 4:
                image_path = str(input('请输入目标图片所在地址:'))
                image_self = image_Open(image_path)
                __image_return = image_Compress(image_self)
                image_SaveChose(__image_return)
            # elif num == 5:
            #     image_self = image_Open(image_path)
            #     image_con = input('请输入想要调节亮度到多少倍【输入数字即可】:')
            #     image_Control(image_con,image_self)
            elif num == 5:
                exit()
            elif num == 6:
                print('''\t开发者:董建池\r\n\t版本号:0.1\r\n''')
            else:
                # raise ValueError('您输入的并非可选项')
                print('您输入的并非可选项!\r\n')
        except FileNotFoundError:
            print('该文件不存在！\r\n')
        except PermissionError:
            print('该路径有错误！\r\n')


if __name__ == '__main__':
    main()