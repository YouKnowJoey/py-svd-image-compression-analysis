import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio, structural_similarity


def compress_image_with_svd(image_path, num_singular_values):
    # Load image and convert to grayscale
    img = Image.open(image_path).convert('L')
    A = np.array(img)
    
    # Apply Singular Value Decomposition (SVD)
    U, Sigma, Vt = np.linalg.svd(A, full_matrices=False)
    
    # Truncate singular values to achieve compression
    # num_singular_values = k = number of eigenvectors 
    truncated_Sigma = np.diag(Sigma[:num_singular_values])
    U_truncated = U[:, :num_singular_values]
    Vt_truncated = Vt[:num_singular_values, :]
    
    # Reconstruct compressed image matrix
    compressed_A = np.dot(U_truncated, np.dot(truncated_Sigma, Vt_truncated))
    
    # Convert compressed matrix back to image format
    compressed_img = Image.fromarray(compressed_A.astype('uint8'), mode='L')
    
    return compressed_img

def evaluate_compression_quality(original_image, compressed_image):
    # Calculate PSNR (Peak Signal-to-Noise Ratio)
    psnr_value = peak_signal_noise_ratio(original_image, compressed_image)
    
    # Calculate SSIM (Structural Similarity Index)
    ssim_value = structural_similarity(original_image, compressed_image)
    
    return psnr_value, ssim_value

def plot_compression_results(original_image, compressed_images, compression_levels):
    num_compressions = len(compressed_images)
    fig, axes = plt.subplots(1, num_compressions + 1, figsize=(15, 5))
    
    # Plot original image
    axes[0].imshow(original_image, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    # Plot compressed images
    for i in range(num_compressions):
        axes[i + 1].imshow(compressed_images[i], cmap='gray')
        axes[i + 1].set_title(f'Compressed (k = {compression_levels[i]})')
        axes[i + 1].axis('off')
    
    plt.tight_layout()
    plt.show()


# Specify image path and number of singular values for compression
# Get the absolute path to the file
current_dir = os.path.abspath(os.path.dirname(__file__)) # Get current directory of the script
image_path = os.path.join(current_dir, '..', 'linear_algebra.jpg')
print(image_path)
num_singular_values = 50  # Adjust this value to control compression level

# Compress the image using SVD
compressed_image = compress_image_with_svd(image_path, num_singular_values)

# Display original and compressed images
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(Image.open(image_path), cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(compressed_image, cmap='gray')
axes[1].set_title(f'Compressed Image (k = {num_singular_values})')
axes[1].axis('off')
plt.show()


# Load original image
original_img = np.array(Image.open(image_path).convert('L'))


# Evaluate compression quality for different compression levels
compression_levels = [5, 10, 25, 50, 125, 175]  # Example compression levels (k values, amount of eigenvectors)


# Compress the image and evaluate quality for different compression levels
compressed_images = []
psnr_values = []
ssim_values = []

for k in compression_levels:
    compressed_img = compress_image_with_svd(image_path, k)
    compressed_images.append(compressed_img)
    psnr, ssim = evaluate_compression_quality(original_img, np.array(compressed_img))
    psnr_values.append(psnr)
    ssim_values.append(ssim)


# Plot results and evaluate compression quality
plot_compression_results(original_img, compressed_images, compression_levels)

# Display quality metrics for each compression level
for i, k in enumerate(compression_levels):
    print(f'Compression with k = {k}: PSNR = {psnr_values[i]:.2f}, SSIM = {ssim_values[i]:.4f}')

# Plot compression quality metrics versus compression rank
plt.figure(figsize=(10, 6))
plt.plot(compression_levels, psnr_values, label='PSNR', marker='o')
plt.xlabel('Compression Rank (Number of Singular Values)')
plt.ylabel('Quality Metric')
plt.title('Impact of Compression Rank on Image Quality')
plt.xticks(compression_levels)
plt.legend()
plt.grid(True)
plt.show()

# Plot compression quality metrics versus compression rank
plt.figure(figsize=(10, 6))
plt.plot(compression_levels, ssim_values, label='SSIM', marker='s')
plt.xlabel('Compression Rank (Number of Singular Values)')
plt.ylabel('Quality Metric')
plt.title('Impact of Compression Rank on Image Quality')
plt.xticks(compression_levels)
plt.legend()
plt.grid(True)
plt.show()
