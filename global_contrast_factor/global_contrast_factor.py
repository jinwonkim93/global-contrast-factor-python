import numpy as np
import cv2


class GlobalContrastFactor:
    
    def compute_luminance(self, image: np.ndarray, gamma : float = 2.2):
        return (image/255)**gamma
    
    def compute_perceptual_luminance(self, image: np.ndarray, gamma : float = 2.2):
        return 100 * np.sqrt(self.compute_luminance(image, gamma))
    
    def weight_factors(self, level: int, max_level: int = 9):
        return (-0.406385 * level / max_level + 0.334573) * level/max_level + 0.0877526

    def compute_image_average_contrast(self, image: np.ndarray, gamma : float = 2.2):
        L = self.compute_perceptual_luminance(image, gamma)
        # pad image with border replicating edge values
        L_pad = np.pad(L,1,mode='edge')

        # compute differences in all directions
        left_diff = L - L_pad[1:-1,:-2]
        right_diff = L - L_pad[1:-1,2:]
        up_diff = L - L_pad[:-2,1:-1]
        down_diff = L - L_pad[2:,1:-1]

        # create matrix with number of valid values 2 in corners, 3 along edges and 4 in the center
        num_valid_vals = 3 * np.ones_like(L)
        num_valid_vals[[0,0,-1,-1],[0,-1,0,-1]] = 2
        num_valid_vals[1:-1,1:-1] = 4

        pixel_avgs = (np.abs(left_diff) + np.abs(right_diff) + np.abs(up_diff) + np.abs(down_diff)) / num_valid_vals

        return np.mean(pixel_avgs)
    
    def __call__(self, image : np.ndarray, gamma : float = 2.2):
        if image.ndim != 2:
            gr = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gr = image

        superpixel_sizes = [1, 2, 4, 8, 16, 25, 50, 100, 200]

        gcf = 0

        for i,size in enumerate(superpixel_sizes,1):
            wi = self.weight_factors(i)
            im_scale = cv2.resize(gr, (0,0), fx=1/size, fy=1/size,
                                interpolation=cv2.INTER_LINEAR)
            avg_contrast_scale = self.compute_image_average_contrast(im_scale, gamma)
            gcf += wi * avg_contrast_scale

        return gcf