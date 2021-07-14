# MNIST - Handwritten Digit Classifier with GUI


This is a deep learning project where we have classfied hand written digits using simple ANN. <br><br>GUI is made using python Tkinter where we can draw a digit, upload a photo and also paste the link of the image consisting of a digit and ANN model will display the predicted digit.

# Dataset - tensorflow.keras.datasets.mnist
MNIST is a dataset of handwritten digit images consisting of a training set of 60,000 images and a test set of 10,000 images. Each example is a 28x28 grayscale image, associated with a label from 10 classes ( 0 - 9 )


## Experiment Results:

 * **Performance Evaluation**
    * Out of 50000 training images 10000 images were used for validation set.
 * **Training and Validation**
    * Dense ANN with 2 layers is used with RELU as activation function and softmax for output.
 * **Performance Results**
    * Training Score: 100.0%
    * Validation Score: 98.03%
    * Testing Score: 98.0%

![]https://github.com/SahilSK202/MNIST_Digit_Classifier_GUI/blob/main/Output/9.jpg)


## GUI Features :

* **Draw a digit** - Tkinter canvas is used to draw
* **Upload a photo** - Upload a photo of handwritten digit
* **Paste a link** - Paste a link of the photo includes handwritten digit
* **Clear** - Clear previous drawing and sketch new
* **Save** -  Save the image

# Demo

## First Look
![](https://github.com/SahilSK202/MNIST_Digit_Classifier_GUI/blob/main/Output/1.jpg)

## Draw and Predict
![](https://github.com/SahilSK202/MNIST_Digit_Classifier_GUI/blob/main/Output/2.jpg)
![](https://github.com/SahilSK202/MNIST_Digit_Classifier_GUI/blob/main/Output/3.jpg)

## Save Image
![]https://github.com/SahilSK202/MNIST_Digit_Classifier_GUI/blob/main/Output/4.jpg)

## Saved Image
![]https://github.com/SahilSK202/MNIST_Digit_Classifier_GUI/blob/main/Output/5.jpg)

## Predicting saved image
![]https://github.com/SahilSK202/MNIST_Digit_Classifier_GUI/blob/main/Output/6.jpg)
![]https://github.com/SahilSK202/MNIST_Digit_Classifier_GUI/blob/main/Output/7.jpg)

## paste link of Image and predict
![]https://github.com/SahilSK202/MNIST_Digit_Classifier_GUI/blob/main/Output/8.jpg)


## Further Improvements
There are lot of things to improve upon

- CNN can be used to increase accuracy on unknown data. 
- More data can be provided.


