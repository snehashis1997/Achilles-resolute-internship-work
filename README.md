# Achilles resolute internship work

Blood vessels damaged from diabetic retinopathy can cause vision loss in two ways:Fragile, abnormal blood vessels can develop and leak blood into the center of the eye, blurring vision. This is proliferative retinopathy and is the fourth and most advanced stage of the disease.

Fluid can leak into the center of the macula, the part of the eye  where sharp, straight-ahead vision occurs. The fluid makes the macula  swell, blurring vision. This condition is called macular edema.  It can occur at any stage of diabetic retinopathy, although it is more  likely to occur as the disease progresses. About half of the people with  proliferative retinopathy also have macular edema.

## What are the symptoms of proliferative retinopathy if bleeding occurs?
At first, you will see a few specks of blood, or spots, “floating” in  your vision. If spots occur, see your eye care professional as soon as  possible. You may need treatment before more serious bleeding occurs.  Hemorrhages tend to happen more than once, often during sleep.

![image](https://user-images.githubusercontent.com/33135767/97417895-36973000-192e-11eb-9c21-82475cfb21dc.png)

## Eye disesase detection and  diabetic retinopathy dieases grading

In this part of the project I use [odir dataset] and [aptos dataset]. At first using [odir dataset] I detect which disease present then using [aptos dataset] decide diabetic retinopathy diesses grading or sevierity.

## [odir dataset] labels are as follows:
* normal (N) 
* diabetes (D) 
* glaucoma (G) 
* cataract (C)
* AMD (A),
* hypertension (H)
* myopia (M) 
* other diseases/abnormalities (O) 

## [aptos dataset] labels are as follows:

* No DR
* Mild
* Moderate
* Severe
* Proliferative DR

[Tortuosity]: https://en.wikipedia.org/wiki/Tortuosity
[odir dataset]: https://odir2019.grand-challenge.org/dataset/
[aptos dataset]: kaggle.com/c/aptos2019-blindness-detection/data

## Blood vessels segmentation to calculate tortuiosity index of the blood vessel 

## Tortuosity

[Tortuosity] is a property of a curve being tortuous (twisted; having many turns). There have been several attempts to quantify this property. Tortuosity is commonly used to describe diffusion and fluid flow in porous media, such as soils and snow.

For this part of the project I use [DRIVE] dataset.

### Example image and it's coresponding segmentation image 


![1](https://user-images.githubusercontent.com/33135767/97539503-14fa7f00-19e8-11eb-91d4-6bed1a7e92bc.png)
                                                                                                                                        
#### Histogram plot of the upper image of the DRIVE dataset's 

![1](https://user-images.githubusercontent.com/33135767/97538935-35760980-19e7-11eb-89b0-d06cf3ecf08b.png)

### Exaple image from test set and it's Histogram plot

![1](https://user-images.githubusercontent.com/33135767/97540848-39575b00-19ea-11eb-9d9d-ec6048351f37.png)


### You can see from histogram plot that there is some serious channel issue. Try to fix it first with image processing

### Now it is much better

<p align="center">
  <img src= "https://user-images.githubusercontent.com/33135767/97541171-b71b6680-19ea-11eb-9bcc-b29418cb8684.png"/>
</p>

## Let's try some Deep learning based image segmentation algorithim

### For segmentation here I use [UNET].

[UNET]: https://arxiv.org/abs/1505.04597

<p align="center">
  <img src="https://user-images.githubusercontent.com/33135767/97540005-f943a880-19e8-11eb-9bb3-cf800a9385c0.png"/>
</p>



### Accuracy and loss for the segmentation architecture

![unet_retinal_acc](https://user-images.githubusercontent.com/33135767/92506741-88231880-f223-11ea-87a0-4dd298a26020.png) ![unet_loss](https://user-images.githubusercontent.com/33135767/92506797-9ffa9c80-f223-11ea-923b-4cb7c6d1b17a.png)

## Eye Ball detection

### Tensorflow object detecton API result. Model used here is SSD

<p align="center">
  <img src="https://user-images.githubusercontent.com/33135767/96847650-10c2e480-1471-11eb-893b-d7bf8bd8244c.gif"/>
</p>
## Loss curve of the SSD model

![image](https://user-images.githubusercontent.com/33135767/96848024-82029780-1471-11eb-8e71-6aa1da751a5c.png)

## Fovea detection
### Tensorflow object detecton API result. Model used here is SSD

<p align="center">
  <img src="https://user-images.githubusercontent.com/33135767/97060798-268bf300-15b2-11eb-8645-4500f2cdae1c.gif"/>
</p>


