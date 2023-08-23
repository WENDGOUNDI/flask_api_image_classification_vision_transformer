# Flask Restful API For Garabage Image Classification Trained on Vision Transformer

In this project, we firstly trained a garabage classifier model using vision transformer pre-trained model. The second step involve the creation of a restful API built with flask. 
The API is secured with an authentication token.

## Dataset
The Garbage Classification Dataset collected from kaggle, contains 6 classifications: cardboard (393), glass (491), metal (400), paper(584), plastic (472) and trash(127).

![dataset_images_overview](https://github.com/WENDGOUNDI/flask_api_image_classification_vision_transformer/assets/48753146/744af43d-3615-4415-b718-d53b0c6e59b1)

dataset link: https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification

## Dependencies
 - flask
 - matplotlib
 - torch
 - torchvision
 - os
 - engine (local file available in the repo)
 - helper_functions (local file available in the repo)
 - torchinfo
 - requests
 - predictions (local file available in the repo)
 - typing
 - PIL
 - io
 - base64

## Training Info
 - Image size: (3, 224, 224)
 - Batch size: 32
 - Epochs: 10
 - Number classes: 6
 - Vit pretrained model: ViT_B_16_Weights.DEFAULT 
 - Training / Validation data ratio: 80/20
 - Optimizers: Adam
 - Learning rate: 1e-3
 - Loss: Crossentropy
![train_test_loss_accuracy](https://github.com/WENDGOUNDI/flask_api_image_classification_vision_transformer/assets/48753146/59bd6237-4b48-4563-b5e2-0a4a4180f7d5)

## Testing
![result_test_1](https://github.com/WENDGOUNDI/flask_api_image_classification_vision_transformer/assets/48753146/ae67a5cf-d794-4000-9911-94663e53d24c)
![result_test_2](https://github.com/WENDGOUNDI/flask_api_image_classification_vision_transformer/assets/48753146/8f581c29-45b0-4511-a26d-307aad5d2a4f)
![result_test_3](https://github.com/WENDGOUNDI/flask_api_image_classification_vision_transformer/assets/48753146/fd2ae46e-1ade-4834-b32a-0eddd4932de7)
![result_test_4](https://github.com/WENDGOUNDI/flask_api_image_classification_vision_transformer/assets/48753146/11348072-fcd7-4224-9c9d-3459865e8173)
![result_test_5](https://github.com/WENDGOUNDI/flask_api_image_classification_vision_transformer/assets/48753146/5cce9ed0-a548-45a1-b68c-abe1a0c7cbe4)
![result_test_6](https://github.com/WENDGOUNDI/flask_api_image_classification_vision_transformer/assets/48753146/14b53b3e-49ed-4d5a-951b-cb38d96d2e45)

## API Info
 - The API is implemented using flask.
 - Token used for security reasons.
 - The image has to be encoded into a base64 file then sent to the flask server that will decode it, predict the label and send the result to the user.
   
![system_overview](https://github.com/WENDGOUNDI/flask_api_image_classification_vision_transformer/assets/48753146/4128affe-aaf2-47e0-ab6a-dea881859c65)

## How to run
 - Create a training environ by running **pyton -m venv vit_env** . You can adjust the environment name according to your needs.
 - for training, open and run **vit_trash_classification_train.ipynb** cells.
 - for inference, open and run **inference.ipynb** cells. The first part will do the inference using the saved training weight. For testing the API, you need to run **flask_api.py** first to enable the local server (see below on how to run your local flask server).
![run_api](https://github.com/WENDGOUNDI/flask_api_image_classification_vision_transformer/assets/48753146/4c071fae-119f-4ab5-9ae7-58519bef631b)


## Notes
 - Adjust the paths in the codes according to your system.

Thanks for giving me a star.
