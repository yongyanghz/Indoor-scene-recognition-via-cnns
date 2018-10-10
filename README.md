# Indoor-scene-recognition-via-cnns

## The main work in this project
1. Based on AlexNet, designed 5 different CNNs models for different types of inputs,
use Adam method to train our models. Though experiments, analyzed the
performance of our CNNs models and the effect of adding depth information.

### model 0
input channel: color(rgb)
### model 1
input channel: color(rgb) + depth
### model 2
input channel: color(rgb) + hha
### model 3
input channel: color(rgb) + depth + hha
### model 4
input channel: hha


2. To explore the mechanism of CNNs models, visualized the weights. Besides,
we use a technique to compute a class saliency map, specific to a given scene image
and class. And Observed the salience maps to study the attentions of scene recognition.

## Conclusion
The experiments show that the CNNs models have higher accuracies than the
traditional computer vision methods, and adding depth information can improve accuracies. The visualization of CNNs models and the class salience maps can further help us design better CNNs architectures and select appropriate features for scene
recognition. 

## CNNs Info
Network Architecture: AlexNet
Train method: Adam method
## Data Set
[NYUD Dpeth V2](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html)

Silberman N, Hoiem D, Kohli P, Fergus R. Indoor segmentation and support inference from
RGBD images[C]. InEuropean Conference on Computer Vision 2012 Oct 7 (pp. 746-760).
Springer Berlin Heidelberg.


## Encode Method
[HHA](https://arxiv.org/abs/1407.5736)

Gupta S, Girshick R, Arbeláez P, Malik J. Learning rich features from RGB-D images for
object detection and segmentation[C]. In European Conference on Computer Vision 2014 Sep
6 (pp. 345-360). Springer International Publishing.

