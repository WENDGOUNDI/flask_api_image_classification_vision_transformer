# Libraries Importtaion

from flask import Flask,request, jsonify
import torch
import os
import predictions
from PIL import Image
from io import BytesIO
import base64

# Initialize the flask app
app = Flask(__name__)


# Loading the model
pretrained_vit = torch.load("./vit_model2.pt")

# Initialize classes 
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# Set authentication key (token)
AUTHENTICATION_KEY = "woOrp8UvW4GkThnh19"


@app.route("/predict_func", methods=["POST"])
def predict_func():

    # Get the key attached to the url
    auth_token = request.args.get('auth_token', None)
    if auth_token == AUTHENTICATION_KEY:   # Check if the authentication key is correct before doing the prediction
        
        predict_image = request.json['encoded_image']
        
        if not predict_image: # return an error message if impossible to decode the encoded element
            
            return jsonify(response="Unable to read the Image. \n Please verify the correctness of your image."), 417
            
        else:
            im = BytesIO(base64.b64decode(predict_image))       
            map_result = predictions.pred_image_label(model=pretrained_vit,
                        image_path=im,
                        class_names=class_names)

            return jsonify(response=map_result), 200
    else:
        return jsonify(response="Wrong Authentification Code."),417


if __name__ == "__main__":
    app.run(debug=True)