<center><font size='5'><b>���ѧϰ�ʼ�</b></font></center>

<center>materials from : [https://tf.wiki/zh_hans/basic/installation.html]</center>

# Tensorflow �İ�װ�Լ���������
Windows �û��޷�ֱ�Ӵ�����Ϊ .condarc ���ļ�������ִ�� `conda config --set show_channel_urls yes` ���ɸ��ļ�
�������֮�󱨴��ᵽ��Դ����������report��conda��˵��������proxy�����⣬ɾ��C:\\[username]\\.condarc
```shell
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```
���� conda clean -i ����������棬��֤�õ��Ǿ���վ�ṩ��������

ע�������Ҫpytorch, ����Ҫ���pytorch�ľ���

```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
```
����conda��Ĭ��Դ��[conda config���ĵ�]:ֱ��ɾ��channels���ɡ�

```shell
conda config --remove-key channels
```

> ʹ��conda install tensorflow���ܲ������°汾

***����conda install �� pip install***

```txt
������tensorflowʱ������ͨ��pip����conda���װ,����֮�������
conda �� pip��python������ + virtualenv�����⻷���� + ��python����������

����һ��conda��yum�Ƚ����ƣ����԰�װ�ܶ�⣬������Python��conda�Ǵ���һ���ֲ��Ļ���������װ��Ӧ����pip�ǰ�װ����ԭ�еĻ����С�

pip install����һЩ�����������㰲װ����conda�����ּ����࣬������������е�ж���滻������Ϊ���ʵ�...����conda��ֻ������������װһֱ��pip install...conda install���Ĳ�̫ϲ���Ҽ��������....

1.pipֻ�ܰ�װpython������conda���԰�װ���κ����Ա�д�İ�
2.pip���ܴ������⻷������Ҫ��������İ�������virtualenv,��conda���Դ������⻷����
3.pip�ǰ���pythonʱ�Դ��ģ���conda��Ҫ��װanaconda�����á�
pip pip install xxx�����ض�������ʹ��pip�����صİ�������ض�������Ŀ¼���棬���磺
D:\Anaconda3\envs\nlp\Lib\site-packages\fasttextʹ��pip uninstallxxx������ж�ص��ˣ�Ҳ������
conda remove--name nlp--all ��ɾ������
conda conda install xxx��������ʲô�������صİ�����ͳһ����һ��Ŀ¼���棺
D:\Anaconda3\pkgs\fasttext���fasttext����Ҳ��site-packages�ļ���
��ĳ����������������ĳ�������ٵ�����һ����������ͬ���İ���conda���Զ��������Ŀ¼�����ң�����У��Ͳ����ظ����أ����ǽ��������site-packages�µ��ļ����Ƶ���ǰ�����£���ֱ��pip installһ����ʹ��conda uninstall xxxʱ����pip uninstallһ����ɾ���˵�ǰ����site-packages����İ����ݣ�����������Ŀ¼���滹���������������ʱ�ٵ�����һ��������������������ǽ�site-packages����һ�ݵ���ǰ�����£�������һ�����أ�����ʹ�á�
pip��������װpython���ģ���װ����python wheel����Դ����İ�����Դ�밲װ��ʱ����Ҫ�б�������֧�֣�pipҲ����ȥ֧��python����֮��������

conda��������װconda package����Ȼ�󲿷�conda����python�ģ�����֧���˲��ٷ�python����д�����������mkl cuda����c c++д�İ���Ȼ��conda��װ�Ķ��Ǳ���õĶ����ư�������Ҫ���Լ����롣���ԣ�pip��ʱ��ϵͳ����û��ĳ�����������ܻ�ʧ�ܣ�conda���ᡣ�⵼����condaװ���������һ��Ƚϴ�������mkl���֣�����������������һG�ࡣ

Ȼ��conda������ʵ��pip���ࡣpip�������Ǹ���װ���������conda�Ǹ���������Ĺ��ߡ�conda�Լ�������������������pip���ܣ���Ҫ����virtualenv֮��ġ���ζ��������conda��װpython��������pip���С���һ���Ҿ�����conda�������Ƶĵط�����conda env���Ժ����ɵع���ܶ���汾��python��pip���С�

Ȼ����һЩ���ܲ�̫���ײ���ĵط���conda��pip���ڻ��������Ĵ���ͬ������������conda��pip�����ϸ�conda���鵱ǰ���������а�֮���������ϵ��pip���ܶ�֮ǰ��װ�İ��Ͳ����ˡ��������Ļ���conda�����ϰ����˾��ܱ�֤������pip��ʱ�����װ����Ҳ��work�������Ҹ��˸о����Ӱ�첻�󣬱Ͼ���������֧�ֶ�ͦ����ģ���������broken��������������Ҳ�����˰�װ��ʱ��conda���������ʱ���pip��ܶ࣬�������°�װ�İ�Ҳ����ࣨ��ѡ����¾ɰ��İ汾����

���pip�İ���conda����ȫ�ص�����Щ��ֻ��ͨ������һ��װ��
conda���԰�װ�Ŀⶼ��Anaconda��˾���������������룬�ύ��anaconda�������ģ�����һЩpython�⣨�϶���ȫ����Ҳ����һЩC++�Ŀ⡣���ܻ���R���Եģ�

pip����python�ٷ��İ�����

conda�а���һЩC++�⣬һ�㶼�Ǻ�python�Ŀ�ѧ�����йصġ��������ֱ�Ӱ�װ��ЩC++�⣺

conda install cudatoolkit
conda install mkl
conda install hdf5
����ͨ��conda��װTensorFlow��ʱ��

conda install tensorflow-gpu
��ͻ���˱������ӵ�cuda��mkl�ӳֵ�tensorflow�⣬ͬʱ���б������ӵ�mkl�ϵ�numpy��
```

�����»����Ĺ��̣�

```shell
conda create --name tf2 python=3.7      # ��tf2�����㽨����conda���⻷��������
conda activate tf2                      # ������Ϊ��tf2����conda���⻷��
```


�������pip��������ȷʹ�õĲ���ϵͳpip��������Ҫ�����ض��Ļ���
> pip install --upgrade pip

�����pipupgradeʱ��ȷ�����������⻷����pip�����Ҵ󲿷�����»�ʧ��(proxy/��Ȩ��)�����Թ���pip���������ʹ��

>conda upgrade pip

������pip upgradeʱʧ�ܣ���������conda upgrade pip������pip����һ�벢ʧ��(�Ѿ����غã�׼��ɾ��ʱ����д��Ȩ��)�����Ա���
![pipfailed.png](./img/pipfailed.png)
���������conda install -f pip ʹ��condaǿ�ư�װpip

ͬ��֮ǰ�ڰ�װtensorflowʱ��;ʧ�ܣ����Դ�ʱ���ɻᱨ�����������ɾ�����ļ�������~��ʼ�� �ļ�
![piptensorfailed.png](./img/piptensorfailed.png)
![deletefilepipfailed.png](./img/deletefilepipfailed.png)
python ��python2��python3������
��ôpipҲ��pip��pip3������
1��pip��python�İ������ߣ�pip��pip3�汾��ͬ����λ��Scripts\Ŀ¼�£�
2�����ϵͳ��ֻ��װ��Python2����ô��ֻ��ʹ��pip��
3�����ϵͳ��ֻ��װ��Python3����ô�ȿ���ʹ��pipҲ����ʹ��pip3�������ǵȼ۵ġ�
4�����ϵͳ��ͬʱ��װ��Python2��Python3����pipĬ�ϸ�Python2�ã�pip3ָ����Python3�á�
5����Ҫ�����⻷���У���ֻ����һ��python�汾��������Ϊ����ϵͳ��pip��pip3�������ͬ��

�����鷳���������ˣ�����tensorflow���ٶȹ�������Ҫ����pip��Դ����һ����windows��Linux���ǲ�ͬ��
��ʱ�޸ģ� 
```txt
������ʹ��pip��ʱ���ں������-i������ָ��pipԴ 
eg: pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
```
�����޸ģ� 
linux: 
�޸� ~/.pip/pip.conf (û�оʹ���һ��)�� �������£�
```txt
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
windows: 
ֱ����userĿ¼�д���һ��pipĿ¼���磺C:\Users\xx\pip���½��ļ�pip.ini����������:
ע�⣬�޸ĵ�pip��ȫ�ֵģ��������⻷�����ض��ģ����ղ�ͬ�������
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
�������޸�Դ��

```command
chennybaba:~ $ pip3 config set global.index-url https://pypi.douban.com/simple/
Writing to /Users/chenhang_vendor/.config/pip/pip.conf
```

�鿴��ǰԴ��

```command
chennybaba:~ $ pip3 config list
global.index-url='https://pypi.douban.com/simple/'
```
������user�»���ȫ�ֵ�pipԴ�����ܻᵼ�¿���ֲ�Բ���ԣ��Ժ�pip����ʹ�� `-i` ��ָ�����ӵ�Դ

> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple [��װ������]

> pip search �������

�����tensorflow�İ�װ����Ҫ������
![https://www.tensorflow.org/install/pip?hl=zh-cn#windows]
����ע��ָ��ΪTUNAԴ�����⻹�а�װ����֤(����������в�֪��Ϊ�λᱨ��������֮��ȫ��������֮����ipynb����������)

```shell
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

֮������������cuda�� cudnn
����cudaʱע�������İ汾�ţ�����֮�󣬽��а�װ�������Ұ�װ��vs2022����ʾû���ҵ�������visual studio 2019���������Ǻ���֮��װ���ɳɹ�
![nvcc_config.png](./img/nvcc_config.png)
***��֤cudnn�Ƿ�װ�ɹ��ķ���***
�ڴ�֮ǰȷ�������غõ�cudnn�ĸ���Ŀ¼�е����ݷ����Ӧ��cuda��װĿ¼�ĸ�������

���Ƚ��뵽��װcuda��Ŀ¼
![cudnn_config.png](./img/cudnn_config.png)

ע�����е�������ִ���ļ�:
* deviceQuery.exe
* bandwidthTest.exe
����ִ�У�deviceQuery.exe���鿴�Ƿ�������½��棺
Ȼ��ִ��bandwidth.exe����������ҳ�棺
![cudnnc_2.png](./img/cudnnc_2.png)
��ʱ˵�����߶���װ�ɹ�

����ʹ��jupyter notebookʱ�޷�ѡ���Ѿ������Ļ��������ԣ���Ҫʹ��tf2env������notebook��������ʾ

> conda install -n [name_env] ipykernel

�ڰ�װ��ipykernel֮����Ҫָ���û�����kernel����
> python -m ipykernel install --user --name tf2env --display-name tf_env


���Ե�py����
```python
import tensorflow as tf
print(tf.test.is_built_with_cuda())
print(tf.test.is_gpu_available())
```
![tfsuccess.png](./img/tfsuccess.png)
���ʹ��GPU��һ���򵥵Ĵ���
```python
import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  # Restrict TensorFlow to only allocate 1GB of memory on the first GPU
  try:
    tf.config.experimental.set_virtual_device_configuration(
        gpus[0],
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Virtual devices must be set before GPUs have been initialized
    print(e)
```

```python
import tensorflow as tf
 
from tensorflow.python.client import device_lib
 
gpu_device_name = tf.test.gpu_device_name()
print(gpu_device_name)
 
 
 
# �г����еı��ػ����豸
local_device_protos = device_lib.list_local_devices()
# ��ӡ
#     print(local_device_protos)
 
# ֻ��ӡGPU�豸
[print(x) for x in local_device_protos if x.device_type == 'GPU']
```
![gpu_info.png](./img/gpu_info.png)

# Pytorch�İ�װ�Լ���������
��֮ǰ��tensorflowһ������ָ��һ�����⻷����Ȼ���������н����������

�鿴���е�env��������Ϣ
> conda env list
> conda info -e

***conda ����������***
ͨ����¡һ���µĻ�����ɾ���ϵĻ��������������⡣
```cmd
conda create --name python32�������֣� --clone python321�������֣�

conda remove --name old_name --all
```
���ڴ�����cuda�汾��pytorch�Ĳ�ƥ�����⣬��ʱ�Ƚ�����ã��ȵ�pytorch����Ƚ����Ƶİ汾֮�������ذ�װ

���ˣ������ҵ���һ����������汾����Ҫ�Ƿ���ʵ���ϲ�����cuda11.2������cuda11.1��Ϊpytorch�İ�װ����(https://blog.csdn.net/weixin_43543177/article/details/121495921)��Ҳ�ǿ��Եģ���װ���£�

> pip install torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html

�ڰ�װʱ�����Զ�����pytorch 1.8.0
![torch_install.png](./img/torch_install.png)

�����jupyter notebook����ʾ��kernel
![torch_jupyter.png](./img/torch_jupyter.png)
��֤��װ�ɹ���
![torch_config.png](./img/torch_config.png)
