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


<img width="300" height="300" src="https://user-images.githubusercontent.com/33135767/92504727-ab989400-f220-11ea-9207-5f1dfb7e0ad9.png"> <img width="300" height="300" src="https://user-images.githubusercontent.com/33135767/92501002-9a995400-f21b-11ea-82c9-adf5076ec593.png"> 

You can see from histogram plot that there is some serious channel issue. Try to fix it first with image processing.

![image](https://user-images.githubusercontent.com/33135767/92499374-6b81e300-f219-11ea-80b8-624a8c145cb2.png)
![image](https://user-images.githubusercontent.com/33135767/92499438-7b99c280-f219-11ea-88c2-e90980192234.png)
![image](https://user-images.githubusercontent.com/33135767/92499472-88b6b180-f219-11ea-83b0-48e981d7b35b.png)


<img width="300" height="300" src="https://user-images.githubusercontent.com/33135767/92504885-e39fd700-f220-11ea-9f8a-1e02f53d8ea5.png"> <img width="300" height="300" src="https://user-images.githubusercontent.com/33135767/92504303-1eedd600-f220-11ea-89f8-b2cb48011e0a.png"> <img width="300" height="300" src="https://user-images.githubusercontent.com/33135767/92504076-c1598980-f21f-11ea-9050-efac70728c73.gif">

<img width="300" height="300" src="https://user-images.githubusercontent.com/33135767/92504034-b69ef480-f21f-11ea-8a48-3b4b0e87a28d.png"> 

![image](https://user-images.githubusercontent.com/33135767/92506538-3c706f00-f223-11ea-9c95-0603b6a1fcec.png)

![unet_retinal_acc](https://user-images.githubusercontent.com/33135767/92506741-88231880-f223-11ea-87a0-4dd298a26020.png)
![unet_loss](https://user-images.githubusercontent.com/33135767/92506797-9ffa9c80-f223-11ea-923b-4cb7c6d1b17a.png)



![eye ball](https://user-images.githubusercontent.com/33135767/96847650-10c2e480-1471-11eb-893b-d7bf8bd8244c.gif)
![image](https://user-images.githubusercontent.com/33135767/96848024-82029780-1471-11eb-8e71-6aa1da751a5c.png)

![fovea1](https://user-images.githubusercontent.com/33135767/97060798-268bf300-15b2-11eb-8645-4500f2cdae1c.gif)

