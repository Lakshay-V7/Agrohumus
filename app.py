from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import numpy as np
import cv2
from keras.models import load_model

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predic_num(file_add):
    model = load_model("final_tomato.h5")
    tomato_disease_mapping = {
        'Tomato___Bacterial_spot': 0,
        'Tomato___Early_blight': 1,
        'Tomato___Late_blight': 2,
        'Tomato___Leaf_Mold': 3,
        'Tomato___Septoria_leaf_spot': 4,
        'Tomato___Spider_mites Two-spotted_spider_mite': 5,
        'Tomato___Target_Spot': 6,
        'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 7,
        'Tomato___Tomato_mosaic_virus': 8,
        'Tomato___healthy': 9
    }
    ref = list(tomato_disease_mapping.values())
    ref = list(dict(zip(list(tomato_disease_mapping.values()), list(tomato_disease_mapping.keys()))).values())

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], file_add)
    img = cv2.imread(image_path)
    if img is None:
        return "Error", "Unable to load image"

    img = cv2.resize(img, (228, 228))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    predictions = model.predict(x)
    class_idx = np.argmax(predictions, axis=1)
    class_name = ref[class_idx[0]]

    disease_suggestions = {
        0: ("Bacterial Spot", "Avoid handling plants when they are wet. Use pathogen-free seed as the first step in disease management."),
        1: ("Early Blight", "Maintain optimum growing conditions, including proper fertilization, irrigation, and pest management."),
        2: ("Late Blight", "Spraying fungicides is the most effective way to prevent late blight."),
        3: ("Leaf Mold", "Maintain adequate spacing between plants. Apply fungicides when symptoms first appear."),
        4: ("Septoria Leaf Spot", "Eliminate the initial source of infection by removing infected plant debris."),
        5: ("Two-Spotted Spider Mite", "Keep production areas free of weeds. Water plants thoroughly before spraying pesticides."),
        6: ("Target Spot", "Regular application of fungicides is preferred. Avoid overhead irrigation."),
        7: ("Yellow Leaf Curl Virus", "Intercrop with non-susceptible plants. Plant early to avoid peak whitefly populations."),
        8: ("Mosaic Virus", "Remove diseased plants, control weeds, and rotate crops."),
        9: ("Healthy", "Your Plant is healthy")
    }

    disease, suggestion = disease_suggestions.get(class_idx[0], ("Unknown", "No suggestion available"))
    return disease, suggestion

@app.route('/new-route/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    # print("this will run")
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No image selected for uploading'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        disease, suggestion = predic_num(filename)
        return jsonify({'disease': disease, 'suggestion': suggestion, 'filename': filename}), 200
    else:
        return jsonify({'error': 'Allowed image types are - png, jpg, jpeg, gif'}), 400

@app.route('/static/uploads/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
    app.run(debug=True)
