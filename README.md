# PySVD Image Compression & Analysis

PySVD Image Compression & Analysis is a Python-based tool for image compression using Singular Value Decomposition (SVD) and subsequent evaluation of compression quality. This project provides functionalities to compress images by reducing the number of singular values through SVD and assesses the quality of compression using metrics like Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM).

## Key Features

- **SVD-Based Compression:** Efficiently compress images using Singular Value Decomposition, a powerful matrix factorization technique.
  
- **Compression Quality Assessment:** Evaluate the quality of compressed images through quantitative metrics like PSNR and SSIM.
  
- **Interactive Visualizations:** Visualize original and compressed images side by side to observe the impact of compression levels on image fidelity.
  
- **Flexible Compression Levels:** Customize compression levels by adjusting the number of retained singular values to achieve varying degrees of compression.


## Getting Started

To run the  locally, follow these steps:

1. Ensure you have latest Python version installed on your machine.
2. Clone the repository to your local environment:
	git clone https://github.com/YouKnowJoey/py-svd-image-compression-analysis
3. Navigate to the project directory:
	cd py-svd-image-compression-analysis
	python svd_image_compression.py

## Changable Values

- **Image**: Change the image path of the defined variable "image_path"

- **Compression levels**: Change the values (eigenvalues) of the defined array "compression_levels" 


## Why Use PySVD Image Compression & Analysis?

- **Educational Tool:** Learn and understand the fundamentals of SVD and its application in image compression.
  
- **Research and Development:** Experiment with different compression settings and analyze the trade-offs between image size reduction and quality preservation.
  
- **Open-Source and Extendable:** Contribute to and extend the project's functionalities to explore advanced image processing techniques.


## Contributing

Contributions are welcome! If you'd like to contribute to RecruitStatsFXExcel, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the gnu v.3 license - see the LICENSE file for details.

## Contact

If you have any questions or suggestions, feel free to contact the project maintainers:
- [Joey Garcia](mailto:youknowjoey@outlook.com)

