from PIL import Image
from django.shortcuts import render
from .forms import ImageUploadForm
from .inference import ModelInference

# Create an instance of ModelInference
model = ModelInference('model.pkl')

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Get the uploaded image from the form
#             image = form.cleaned_data['image']
            
#             # Convert the image to a PIL image
#             image = Image.open(image)
            
#             # Resize the image to 128x128
#             image = image.resize((128, 128))
            
#             # Save the image to a permanent file
#             image_path = 'static/images/uploaded_image.jpg'
#             image.save(image_path)
            
#             # Make a prediction using the model
#             prediction = model.predict(image)
            
#             # Return the prediction and the image in the response
#             return render(request, 'HAR_app/result.html', {'prediction': prediction, 'image_path': image_path})
#     else:
#         form = ImageUploadForm()

#     return render(request, 'HAR_app/upload.html', {'form': form})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded image from the form
            image = form.cleaned_data['image']

            # Convert the image to a PIL image
            image = Image.open(image)

            # Resize the image to 128x128
            image = image.resize((128, 128))

            # # Save the image to a permanent file
            # image_path = 'static/images/uploaded_image.jpg'
            # image.save(image_path)
            
            # Save the image to a permanent file
            image_path = 'images/uploaded_image.jpg'
            image.save('static/' + image_path)

            # Make a prediction using the model
            sorted_probs = model.predict(image)

            # Return the prediction and the image in the response
            return render(request, 'HAR_app/result.html', {'sorted_probs': sorted_probs, 'image_path': image_path})
    else:
        form = ImageUploadForm()

    return render(request, 'HAR_app/upload.html', {'form': form})
