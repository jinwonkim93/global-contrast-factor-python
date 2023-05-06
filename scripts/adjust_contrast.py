import numpy as np
import cv2
import click

from global_contrast_factor import GlobalContrastFactor


@click.command()
@click.option("--contrast_reference_path", "-c")
@click.option("--image_path", "-i")
@click.option("--output_path", "-o")
def main(contrast_reference_path, image_path, output_path):

    reference = cv2.imread(contrast_reference_path)
    image = cv2.imread(image_path)
    gfc = GlobalContrastFactor()

    gfc_ratio = gfc(reference)/gfc(image)

    contrast_adjusted_img =  gfc_ratio * image
    contrast_adjusted_img = np.clip(contrast_adjusted_img, 0, 255).astype(np.uint8)
    cv2.imwrite(output_path, contrast_adjusted_img)

if __name__ == "__main__":
    main()