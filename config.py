# paths
qa_path = '/Data_HDD/fyp22_haochen_luo/vqa_final/basic_vqa/datasets/vqa'  # directory containing the question and annotation jsons
train_path = '/Data_HDD/fyp22_haochen_luo/vqa_final/basic_vqa/datasets/Images/train2014'  # directory of training images
val_path = '/Data_HDD/fyp22_haochen_luo/vqa_final/basic_vqa/datasets/Images/val2014'  # directory of validation images
test_path = '/Data_HDD/fyp22_haochen_luo/vqa_final/basic_vqa/datasets/Images/test2015'  # directory of test images
preprocessed_path = './resnet-14x14.h5'  # path where preprocessed features are saved to and loaded from
vocabulary_path = 'vocab.json' 

task = 'OpenEnded'
dataset = 'mscoco'

# preprocess config
preprocess_batch_size = 64
image_size = 448  # scale shorter end of image to this size and centre crop
output_size = image_size // 32  # size of the feature maps after processing through a network
output_features = 2048  # number of feature maps thereof
central_fraction = 0.875  # only take this much of the centre when scaling and centre cropping

# training config
epochs = 50
batch_size = 128
initial_lr = 1e-3  # default Adam lr
lr_halflife = 50000  # in iterations
data_workers = 8
max_answers = 3000
