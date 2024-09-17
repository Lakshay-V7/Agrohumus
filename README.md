# DESCRIPTION #
AgroHums is an innovative platform designed to support farmers in optimizing their agricultural practices. The website offers tailored fertilizer recommendations based on soil analysis and crop requirements, ensuring enhanced growth and yield. Additionally, AgroHums features early disease prediction technology, allowing farmers to detect potential threats to their crops before they become severe. By leveraging advanced algorithms and real-time data, AgroHums empowers farmers with the tools they need to make informed decisions, improve crop health, and maximize productivity.

AgroHums is a cutting-edge platform designed to assist farmers with fertilizer recommendations and early disease detection. Our website utilizes React and Tailwind for a seamless, user-friendly interface.
Key Features:
Fertilizer Recommendation: Using advanced algorithms, the platform provides personalized fertilizer suggestions based on soil and crop parameters.

Disease Prediction: Employing Convolutional Neural Networks (CNNs), the system predicts potential crop diseases from uploaded images, allowing for early intervention.

Chatbot Support: An integrated chatbot offers real-time assistance to help farmers with their queries and support needs.

Technical Overview:
The backend of AgroHums leverages Recurrent Neural Networks (RNNs) and Convolutional Neural Networks (CNNs) to power its recommendation and prediction systems. The RNNs are used for analyzing temporal data patterns, while CNNs are employed for image analysis, enhancing the accuracy of disease predictions.

# ALL ABOUT IT:
We provides a user-friendly front end designed with React and styled using Tailwind CSS. The interface is crafted for ease of navigation, making it accessible for farmers of all tech levels.
Front End Features:
i. Dashboard: A clean and intuitive dashboard displays key features and recent activities. It provides quick access to the fertilizer recommendation service, disease prediction tool, and chatbot support.
ii. Fertilizer Recommendation Page: This section features an interactive form where users input soil and crop details. Tailwind CSS ensures a responsive design that adjusts to different screen sizes, making it easy to complete the form on any device.
iii. Disease Prediction Page: Users can upload images of their crops directly through a simple, drag-and-drop interface. The page includes visual feedback on image uploads and displays predictions in a user-friendly format.
iv. Chatbot Support: An embedded chatbot window is available for instant help. It is designed to be easily accessible from any page, providing real-time assistance with a conversational interface.
![image](https://github.com/user-attachments/assets/085f0f63-8970-4f63-ab6e-43a6cbc34ea0)


### Visuals:
I. The Fertilizer Recommendation Form on AgroHums is designed to be user-friendly and efficient, offering two distinct methods for obtaining fertilizer recommendations: Manual and Automatic.

#### Manual Recommendation
Input Requirements: Users need to provide a detailed lab soil test report to receive precise fertilizer recommendations. This report includes various parameters such as soil pH, nutrient levels, and other critical soil characteristics.
Form Design: The form is organized with clear, labeled fields for each parameter from the soil test report. Tailwind CSS is used to style the form with a clean layout and responsive design, ensuring ease of use on both desktop and mobile devices.
Validation and Feedback: The form includes validation checks to ensure all required fields are filled out correctly. Users receive immediate feedback on any missing or incorrect information, guiding them to complete the form accurately.
#### Automatic Recommendation
Input Requirements: For users who prefer a quicker approach, the automatic recommendation method requires only the crop type.
Geolocation Integration: The system uses the user's geolocation to determine the common soil parameters for the region. This information is combined with the crop type to generate suitable fertilizer recommendations.
Form Design: The automatic recommendation form is streamlined with a single input field for the crop type and a geolocation-enabled button. This form is styled to be intuitive and quick to complete, minimizing the input required from the user.
#### User Experience
Manual Method: Provides highly accurate recommendations based on detailed soil data, ideal for users seeking precise information.
Automatic Method: Offers a faster, more convenient option for users who need general recommendations based on their location and crop type.

![WhatsApp Image 2024-09-17 at 12 06 30_de0e9ccc](https://github.com/user-attachments/assets/a74e2828-430f-4ab2-979b-ea883b89f9dd)
![WhatsApp Image 2024-09-17 at 12 05 33_6057dfec](https://github.com/user-attachments/assets/fe347849-5812-4aa0-afb5-2e325e605e2d)

II. Disease Prediction
The Disease Prediction feature of AgroHums is designed to simplify the process of identifying potential crop diseases. This feature allows users to upload images of their crop leaves to receive early warnings about possible infections.
#### How It Works
Image Upload: Users need to upload a clear image of the leaf showing any visible infected areas. The system uses this image to analyze and detect signs of disease.
Image Processing: The uploaded image is processed using Convolutional Neural Networks (CNNs), which are trained to recognize various disease patterns from leaf images.
Prediction Results: After processing, the system provides a prediction of potential diseases, along with information on symptoms and suggested actions for treatment or prevention.
#### User Experience
Simple Upload Interface: The upload area is designed to be intuitive and user-friendly. Users can drag and drop their images or select them through a file picker.
Visual Feedback: Once an image is uploaded, users receive immediate feedback, including the predicted disease and recommendations for next steps. The interface ensures that the results are easy to understand and actionable.

![WhatsApp Image 2024-09-17 at 12 07 47_44b349bf](https://github.com/user-attachments/assets/b390bdad-c17a-46d6-acd5-fdd8ddf48add)
III. 24 hours bot support
The Chatbot Support feature on AgroHums provides farmers with round-the-clock assistance, ensuring they receive help whenever needed.
Key Features
24/7 Availability: The chatbot operates continuously, offering instant responses and support at any time of day or night.
Interactive Assistance: Farmers can ask questions related to fertilizer recommendations, disease predictions, and general agricultural practices. The chatbot is designed to handle a wide range of queries and provide relevant, accurate information.
User-Friendly Interface: The chatbot is seamlessly integrated into the website, appearing as a chat window that is easily accessible from any page. Its design is optimized for a smooth, engaging user experience.
Real-Time Responses: The chatbot uses advanced natural language processing to understand and respond to user inquiries in real time, ensuring that farmers receive timely and helpful information.

![WhatsApp Image 2024-09-17 at 12 10 15_64903da0](https://github.com/user-attachments/assets/7bfa57a2-2d46-4020-8b67-607b699e51af)

# RESULTS:



- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh
