import argparse
import cv2

class DSample:

    SUPPORTED_FORMATS = (
        ".bmp",
        ".dib",
        ".jpeg",
        ".jpg",
        ".jpe",
        ".jp2",
        ".png",
        ".pbm",
        ".pgm",
        ".ppm",
        ".sr",
        ".ras",
        ".tif",
        ".tiff",
    )

    def __init__(self, *args_dict, **kwargs):
        for dictionary in args_dict:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

        self.image()
        if self.gaussian_kernel:
            self.blur()
        self.dimensions()
        self.scale_factor()
        self.sample()

    # DSample.image
    def image(self):
        """Read image data"""
        self.image = cv2.imread(self.filename)

    # DSample.blur
    def blur(self):
        """Apply Gaussian Blur"""
        self.image = cv2.GaussianBlur(
            self.image,
            ksize=(0, 0),
            sigmaX=1,
            sigmaY=1
        )

    # DSample.dimensions
    def dimensions(self):
        """Set image dimensions"""
        self.dimensions = (self.image.shape[1], self.image.shape[0])

    # DSample.scale_factor
    def scale_factor(self):
        """Factor for downsample, 2x, 3x, 4x"""
        scale = {
            '2': (0.5, 0.5),
            '3': (0.33, 0.33),
            '4': (0.25, 0.25),
            '5': (0.2, 0.2),
            '6': (0.12, 0.12),
        }
        self.scale_factor = scale.get(self.downsample, None)

    # DSample.sample
    def sample(self):
        """Downsample the image."""
        fx, fy = self.scale_factor or (1, 1)
        self.d_sample = cv2.resize(
            self.image,
            (0, 0),
            fx=fx,
            fy=fy,
           interpolation=cv2.INTER_CUBIC
        )

        self.p_sample = cv2.resize(
            self.d_sample,
            self.dimensions,
            interpolation=cv2.INTER_CUBIC
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='downsample image using bicubic interpolation',
    )

    parser.add_argument(
        "filename",
        help="input filename to downsample"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="output filename for downsampled image"
    )

    parser.add_argument(
        "-d",
        "--downsample",
        metavar='n',
        help="downsample by a factor of 2, 3, 4, 5, 6"
    )

    parser.add_argument(
        "-g",
        "--gaussian-kernel",
        help="apply a gaussian kernel, effective in reducing gaussian noise",
        action="store_true"
    )

    parser.add_argument(
        "-s",
        "--save-dimensions",
        help="downsampled image dimensions are the same as input dimensions",
        action="store_true"
    )

    args = parser.parse_args()

    dsample = DSample(**vars(args))

    if dsample.save_dimensions:
        cv2.imwrite(dsample.output, dsample.p_sample)
    else:
        cv2.imwrite(dsample.output, dsample.d_sample)
