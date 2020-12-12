# Steps To Run
1. Install Docker Desktop Application
https://www.docker.com/products/docker-desktop

2. Start the Application that you downloaded.

3. Pull the Tensorflow Serving Image

**CMD**
    docker pull lokv007/saved11:latest
 
https://hub.docker.com/repository/docker/lokv007/saved11

4. Now, run the tfx serving docker image that you just pulled.

**CMD**
    docker run -p 8501:8501 lokv008/saved11

5. Pull the django web application 

**CMD:** 
    docker pull lokv007/dldjango:latest

https://hub.docker.com/repository/docker/lokv007/dldjango

6. Now, run the django docker image that you just pulled.

**CMD**
    docker run -p 8000:8000 lokv008/dldjango

**after running**

  **stop all containers:**
  docker kill $(docker ps -q)

  **remove all containers:**
  docker rm $(docker ps -a -q)

  **remove all docker images:**
  docker rmi $(docker images -q)


# Model is deployed using TFX tensorflow serving, docker and kubernetes

**Project Name** : Histopathological Image Analysis using attention-based MIL and Transfer Learning techniques

**Team Members and their Contributions** :

| Team Member  | Contribution(s) |
| ------------- | ------------- |
| Chetan Kulkarni  | Attention-based MIL on BreakHis dataset (Pytorch implementation), model deployment  |
| Lokesh Vadlamudi  | Attention-based MIL on Breast Cancer histopathological (IDC) images (IDC dataset, data augmentation and Keras implementation), model deployment  |
| Nupur Yadav  | Transfer Learning on BreakHis dataset (using DenseNet201 with weights pre-trained on ImageNet), model deployment |

In this project we have used two techniques which are attention-based MIL and transfer learning to detect cancer in breast cancer histopathological images dataset.

[MIL_on_BreastCancer_Pytorch.ipynb](https://github.com/nupursjsu/EmergingTechnologiesProject/blob/main/MIL_on_BreastCancer_Pytorch.ipynb) - This colab demonstrates the pytorch implementation of the Attention-based Multi Instance Learning on breast cancer histopathological images to detect breast cancer. The dataset used is [BreakHis](https://www.kaggle.com/kritika397/breast-cancer-dataset-from-breakhis). Following diagram shows the approach used:

![](https://github.com/nupursjsu/EmergingTechnologiesProject/blob/main/Images/Attention-based%20MIL%20approach.png)


The model yielded an accuracy of '69%' which is very low for medical domain where most precision is required. In general this dataset is difficult due to high variability of slides and small number of cases.

This is also backed by the following paper which we later came across.

https://arxiv.org/pdf/1802.04712.pdf

So, we thought of experimenting a bit and used another breast cancer dataset from Kaggle to apply attention-based MIL using Keras. This time we also did data augmentation to increase the number of samples.

[MIL_on_BreastCancer__Keras.ipynb](https://github.com/nupursjsu/EmergingTechnologiesProject/blob/main/MIL_on_BreastCancer__Keras.ipynb) - This colab demonstrates the keras implementation of the Attention-based MIL on [different breast cancer histpathological image dataset](https://www.kaggle.com/paultimothymooney/breast-histopathology-images) (IDC) taken from Kaggle. As mentioned above, we did data augmentaion to increase the dataset and hoping to improve the model accuracy. The model yielded an accuracy of '73%' this time which is better than the previous one but still low for the medical domain.

Though Attention-based Deep Multiple Instance Learning is applied in a wide range of medical imaging applications. Surprisingly, it didn't work for the breast cancer dataset. So we thought of using a pretrained model (transfer learning technique) for breast cancer classification on BreakHis dataset to see if it can achieve better accuracy.

[TransferLearning_on_BreastCancer_TFX.ipynb](https://github.com/nupursjsu/EmergingTechnologiesProject/blob/main/TransferLearning_on_BreastCancer_TFX.ipynb) - This colab demonstrates the use of a pretrained model "DenseNet201" to perform classification on breast cancer histopathological images (BreakHis). The model achieved an accurcay of '94%' which is quite good. 

Following table summarizes all the experiments and observations.

| Technique  | Accuracy |
| ------------- | ------------- |
| Attention-based MIL on BreakHis dataset (Pytorch implementation)  | 69%  |
| Attention-based MIL on Breast Cancer histopathological (IDC) images (IDC dataset, data augmentation and Keras implementation)  | 73%  |
| Transfer Learning on BreakHis dataset (using DenseNet201)  | 94%  |

Hence, we used this transfer learning model for deployment and making future inferences.

**We have used Django to build our web application and tensorflow serving, docker and kubernetes to deploy our model. We created two docker images one for our Django app and another for our model for deployment.**

[Django application code](https://github.com/nupursjsu/EmergingTechnologiesProject/tree/main/DLProject)

Following is the system architecture we have used:

![](https://github.com/nupursjsu/EmergingTechnologiesProject/blob/main/Images/System%20architecture.png)

Following are the UI screenshots for our application:

Homepage

![](https://github.com/nupursjsu/EmergingTechnologiesProject/blob/main/Images/Web%20homepage.png)

Prediction

![](https://github.com/nupursjsu/EmergingTechnologiesProject/blob/main/Images/Web%20prediction.png)


# View the end to end TFX interactive context for the transfer learning colab

https://github.com/nupursjsu/EmergingTechnologiesProject/blob/main/TFXpipeline/TFXpipeline.ipynb

COLAB

https://colab.research.google.com/github/LokeshVadlamudi/EmergingTechnologiesML/blob/master/TFXpipeline.ipynb



[Project Presentation in PDF format](https://github.com/nupursjsu/EmergingTechnologiesProject/blob/main/Project_presentation.pdf)

[Project Report in PDF format](https://github.com/nupursjsu/EmergingTechnologiesProject/blob/main/Project_Report_Histopathological_Image_Analysis.pdf)


**Note
The web application has been taken down to save cloud computing costs. Please use docker images mentioned above to run the application locally. 



