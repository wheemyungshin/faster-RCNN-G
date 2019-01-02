import pickle

with open('C:\\Users\\Administrator\\Desktop\\2018Graphene\\vgg16\\voc_2007_test\\faster_rcnn_10\\aeroplane_pr.pkl', 'rb') as f:
    data = pickle.load(f, encoding='latin1')
    print(data)

