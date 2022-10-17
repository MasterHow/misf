# 用于生成图片和mask的地址list
import json
import os


def load_file_list_recursion(fpath, result):
    allfilelist = os.listdir(fpath)
    for file in allfilelist:
        filepath = os.path.join(fpath, file)
        if os.path.isdir(filepath):
            load_file_list_recursion(filepath, result)
        else:
            result.append(filepath)
            print(len(result))


def scan(input_path, out_put):
    result_list = []
    load_file_list_recursion(input_path, result_list)
    result_list.sort()

    for i in range(len(result_list)):
        print('{}_{}'.format(i, result_list[i]))

    with open(out_put, 'w') as j:
        json.dump(result_list, j)


def save_list(input_path, out_put):
    """用于生成输出文件夹的list"""
    allfilelist = os.listdir(input_path)
    out_put_list = []
    for file in allfilelist:
        filepath = os.path.join(input_path[:-len(input_path.split('\\')[:-4])], 'results', file)
        out_put_list.append(filepath)
        print(len(out_put_list))
    out_put_list.sort()
    for i in range(len(out_put_list)):
        print('{}_{}'.format(i, out_put_list[i]))

    with open(out_put, 'w') as j:
        json.dump(out_put_list, j)



# scan('mask', './flist.txt')
# Inner Sphere
# scan('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\InnerSphere\\imgs\\', './kexi_flist.txt')
# scan('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\InnerSphere\\masks\\fov5\\', './kexi_fov5_mlist.txt')
# scan('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\InnerSphere\\masks\\fov10\\', './kexi_fov10_mlist.txt')
# scan('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\InnerSphere\\masks\\fov20\\', './kexi_fov20_mlist.txt')
# save_list('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\InnerSphere\\imgs\\', './kexi_save_list.txt')

# Outer Pinhole
# scan('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\OuterPinhole\\imgs\\', './kexo_flist.txt')
# scan('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\OuterPinhole\\masks\\fov5\\', './kexo_fov5_mlist.txt')
# scan('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\OuterPinhole\\masks\\fov10\\', './kexo_fov10_mlist.txt')
# scan('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\OuterPinhole\\masks\\fov20\\', './kexo_fov20_mlist.txt')
# save_list('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\OuterPinhole\\imgs\\', './kexo_save_list.txt')

# Outer Pinhole Train
scan('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\train\\OuterPinhole\\imgs\\', './kexo_flist_train.txt')
scan('D:\\MyProject\\PyThon\\FlowInpainting\\misf\\data\\KITTI360-EX\\train\\OuterPinhole\\masks\\', './kexo_fov_mlist_train.txt')
