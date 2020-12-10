# FasterRCNN
Faster-rcnn is one of the most classic algorithms in the field of object detection. It mainly consists of two parts. One is a deep full convolutional network for generating candidate area frames, and the other is a Fast R-CNN detection model. The two share parameters during training.

A Faster R-CNN object detection network is composed of a feature extraction network which is typically a pretrained CNN, similar to what we had used for its predecessor. This is then followed by two subnetworks which are trainable. The first is a Region Proposal Network (RPN), which is, as its name suggests, used to generate object proposals and the second is used to predict the actual class of the object. So the primary differentiator for Faster R-CNN is the RPN which is inserted after the last convolutional layer. This is trained to produce region proposals directly without the need for any external mechanism like Selective Search. After this we use ROI pooling and an upstream classifier and bounding box regressor similar to Fast R-CNN.

Faster R-CNN can solve the problem that Fast RCNN uses the third-party tool selective search to extract the region proposal. It uses RPN instead of selective search to make the entire target detection function into a unified network. Faster RCNN uses RPN to make the calculation of region proposals more elegant and efficient. RPN is a full convolutional network. Candidate region generation and target detection share convolutional features. Attention mechanism is used . RPN will tell the network where to focus.

## RPN (Region Proposal network)
RPN is the core of faster rcnn. Its essence is a classless object detector based on sliding windows. There are multiple types of anchor boxes (region proposals) at each position of the image. Faster rcnn is trained with these region proposals. Classification and box regression pass Gradient descent backpropagation adjusts network parameters, regenerates the region proposal, and then continues training faster rcnn, repeating this process continuously.

### FatserRCNN paper https://arxiv.org/pdf/1506.01497.pdf

## About me

**Piyush Pathak**

[**PORTFOLIO**](https://anirudhrapathak3.wixsite.com/piyush)

[**GITHUB**](https://github.com/piyushpathak03)

[**BLOG**](https://medium.com/@piyushpathak03)


# 📫 Follw me: 

[![Linkedin Badge](https://img.shields.io/badge/-PiyushPathak-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/piyushpathak03/)](https://www.linkedin.com/in/piyushpathak03/)

<p  align="right"><img height="100" src = "https://media.giphy.com/media/l3URDstnIjBNY7rwLB/giphy.gif"></p>
