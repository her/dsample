### dsample 🌌

#### Install
Requires Python 3\
`$ pip install -e .`

#### Usage
```
usage: dsample.py [-h] [-o OUTPUT] [-d n] [-g] [-s] filename

downsample image using bicubic interpolation

positional arguments:
  filename              input filename to downsample

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output filename for downsampled image
  -d n, --downsample n  downsample by a factor of 2, 3, or 4
  -g, --gaussian-kernel
                        apply a gaussian kernel, effective in reducing
                        gaussian noise
  -s, --save-dimensions
                        downsampled image dimensions are the same as input
                        dimensions
```

#### Examples

Original image:\
![lotus.png](https://github.com/her/dsample/blob/master/img/lotus.png)

```
python dsample.py lotus.png -sgd 4 -o output.png
```
Downsamples lotus.png by a factor of four, applies a guassian mask and keeps
the original image dimensions

![ds_4x_s_mask.png](https://github.com/her/dsample/blob/master/img/ds_4x_s_mask.png)

```
python dsample.py lotus.png -sd 4 -o output.png
```
Downsamples lotus.png by a factor of four and keeps
the original image dimensions

![ds_4x_s.png](https://github.com/her/dsample/blob/master/img/ds_4x_s.png)

```
python dsample.py lotus.png -d 4 -o output.png
```
Downsamples lotus.png by a factor of 4

![ds_4x.png](https://github.com/her/dsample/blob/master/img/ds_4x.png)

```
python dsample.py lotus.png -gd 4 -o output.png
```
Downsamples lotus.png by a factor of four and applies a guassian mask

![ds_4x_mask.png](https://github.com/her/dsample/blob/master/img/ds_4x_mask.png)
