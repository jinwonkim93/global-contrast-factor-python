# Python implementation of [Global Contrast Factor - a New Approach to Image Contrast](https://www.vrvis.at/publications/pdfs/PB-VRVis-2005-035.pdf)

# Usage

```python
import cv2
from global_contrast_factor import GlobalContrastFactor

img = cv2.imread("./images/img1.png")
img_low_contrast = cv2.imread("./images/img_contrast50.png")

gfc = GlobalContrastFactor()

print(gfc(img))
print(gfc(img_low_contrast))
```

# Install
```bash
git clone https://github.com/jinwonkim93/global-contrast-factor-python.git
cd global-contrast-factor-python
pip install -e .
```