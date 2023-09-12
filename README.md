# Template Matching Under Noise

1) We select an image and an object that exists more than once in the image.
2) We run the template matching algorithm iteratively, adding 5% random noise each time.
3) Gaussian filter is applied on the image.

# Adding Noise
To add noise to the image you need to use the function ```noise(image, prob)```. On the 
```noise``` parameter you need to insert the image and on the ```prob``` parameter, the percentage of the noise you want to add.
Example: If you want to add 10% noise on the image the ```prob``` parameter must be set to ```0.1```.

The noise values that will be used are 0%, 5%, 10%, 15%, 20%.


# Images Used

<div style="display: flex; justify-content: center;">
  <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/3cf3fd1c-d593-443f-a02f-840d463b5060" alt="Diamond1 1" width="400px">
</div>

The above image is used for the recognition. We will try to detect the diamond in the image.
The image was drawn by hand
and it consists of 5 different geometric shapes that are mixed with each other. The image is on the ```images``` folder
with name ```diamond1.1.jpg```.

<div style="display: flex; justify-content: center;">
  <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/37a28eab-8493-4a8b-92a2-c693e5a7c81e">
</div>

The "diamond" shape is what we'll be looking for in the image above. The
specific shape appears 9 times in scattered parts of our image, between
other shapes. The image is on the ```images``` folder with name ```diamond2.1.jpg```


# Effect of Noise on Matching

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/236da910-33e4-46e5-8331-d3000264ba7a">
      <br>
       <figcaption>0%</figcaption>  
    </td>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/c72d68a1-3813-4e6c-90ea-62c11cae2ecd">
<br>
       <figcaption>5%</figcaption>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/f04df01a-1a16-4897-90a4-9d347ac33d02">
<br>
       <figcaption>10%</figcaption>
    </td>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/03f0802b-3522-4ff5-89b8-7d36b90b1962">
<br>
       <figcaption>15%</figcaption>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/e408f420-1571-4518-8e90-2a51a9163470">
<br>
       <figcaption>20%</figcaption>
    </td>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/0d554a5a-0386-4f5f-baad-82673b58195b">
<br>
       <figcaption>30%</figcaption>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/aae42e0e-1163-46a5-916e-f8e8a281ca34">
<br>
       <figcaption>40%</figcaption>
    </td>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/f8e29120-6c27-467f-80e5-4e5ed5ef8c42">
<br>
       <figcaption>50%</figcaption>
    </td>
  </tr>
</table>

 In these images we observe the effect of adding noise at a small stage untill it reaches 50%.
As we can see, there is not much difference in the match at the beginningm but after 30%, the results
are rapidly changing. We see that by adding more noise, data
which were previously recognized, are now unrecognizable. As the noise rises, more
and more diamonds are not recognized.

Conclusion: Noise has a negative effect as it increases. The total recognised diamonds decrease as noise rises.

# Adding Gaussian Noise
To add Gaussian Noise, you need to use the command below.

```blur = cv2.GaussianBlur(img_noise_rgb, (5, 5), 0)```

This command is as a comment on the code. 

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/f8351a79-12ee-4fb4-a429-5a20352daee3">
      <br>
       <figcaption>0%</figcaption>  
    </td>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/af58acf2-3e35-4076-bddc-7cbbb3ab150f">
<br>
       <figcaption>5%</figcaption>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/f8e18de8-77c8-4253-ba00-fb55a08dba6e">
<br>
       <figcaption>10%</figcaption>
    </td>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/99e8e2a3-7e28-4248-a126-1cc41cd5dacc">
<br>
       <figcaption>15%</figcaption>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/cbc67f22-fa88-4f05-9d4a-7461b342e212">
<br>
       <figcaption>20%</figcaption>
    </td>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/0d554a5a-0386-4f5f-baad-82673b58195b">
<br>
       <figcaption>40%</figcaption>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/46be7cc4-c50c-4314-aa9d-db4b62b93a0b">
<br>
       <figcaption>50%</figcaption>
    </td>
    <td align="center">
      <img src="https://github.com/PhilippBarr/RSA-Basics/assets/103950889/73d113c8-3168-4a78-b80a-e569eb86fc7d">
<br>
       <figcaption>70%</figcaption>
    </td>
  </tr>
</table>

We distinguish that in the case that a filter is applied, at small noise addition values there are not many differences.
One difference is that some items are recognized
as 'double', this is what we see in all the images for the 'diamond' shown below
left part and appears as double recognition (two yellow outlines on it). When increasing the noise, 
the "diamond" which was
recognized as double in previous tests, is now recognized as single.

The biggest
difference in performance is that when even large noise values are added, the template
matching is performed correctly and many elements are found, we can see that without
the filter, only one "diamond" is recognized at 50% noise, while with the filter, even at 70% noise,
5 diamonds are recognized.

Conclusion: Using a filter results in better template matching even if the plugin
noise has high values.



# Libraries Used

- Python Version ```3.6.7```
- cv2 ```3.4.2```
- numpy ```1.19.5```

# Folders and Files

```images``` This folder contains the initial images that were used for the project.

```imageResults``` This folder contains the images generated.

```templateMatching.py``` The code.

```README.md``` The Readme that you are reading now.
 
