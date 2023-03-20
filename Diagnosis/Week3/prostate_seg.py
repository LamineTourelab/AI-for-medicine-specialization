
import numpy as np
import nibabel as nib
import itk
import itkwidgets
from ipywidgets import interact, interactive, IntSlider, ToggleButtons
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set_style('darkgrid')

image_path = "C:\Users\Lamine\Downloads\AI-for-medicine-specialization\Data-MSD-images\Task05_Prostate\imagesTr\prostate_00.nii.gz"
image_obj = nib.load(image_path)
print(f'Type of the image {type(image_obj)}')

# Extract data as numpy ndarray
image_data = image_obj.get_fdata()
type(image_data)

# Get the image shape and print it out
height, width, depth, channels = image_data.shape
print(f"The image object has the following dimensions: height: {height}, width:{width}, depth:{depth}, channels:{channels}")

# Select random layer number
maxval = 15
i = np.random.randint(0, maxval)
# Define a channel to look at
channel = 0
print(f"Plotting Layer {i} Channel {channel} of Image")
plt.imshow(image_data[:, :, i, channel], cmap='gray')
plt.axis('off');
