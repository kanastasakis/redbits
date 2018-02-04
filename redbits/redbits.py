from math import ceil
from PIL import Image, ImageDraw, ImageColor

class Redbits():
    '''
    This class stylizes png images.
    
    Example::

        from redbits import Redbits
        rb = Redbits(foreground_color, background_color)
        stylized_image = rb.process(image)
    
    :param foreground: (unsigned integer) Foreground color as a hexidecimal.
    :param background: (unsigned integer) Background color as a hexidecimal.

    Todo:
        * Allow user to select output size
        * Allow User to select box density of output image
    '''
    

    def __init__(self, foreground = 0xff0000, background = 0x000000):
        self.foreground = foreground
        self.background = background

    def process(self, pil_image):
        '''
        Processes an image. 

        :param pil_image: (PIL.Image) The image to process.
        '''
        # Create small copy
        size = pil_image.size
        temp_val = 100.0
        multiplier = temp_val / float(max(size))
        reduced_image_size = self.__scaleTuple(size, multiplier, True)
        smaller_image = pil_image.resize(reduced_image_size)
        bw_image = smaller_image.convert("L")

        # Create return image
        box_size = 9
        offset = ceil(box_size * 0.5)
        return_image = Image.new("RGB", self.__scaleTuple(reduced_image_size, box_size, True), color=self.background)
        draw = ImageDraw.Draw(return_image)

        for y in range(reduced_image_size[1]):
            for x in range(reduced_image_size[0]):
                pixel = bw_image.getpixel((x, y))
                bb = self.__getBoundingBox(offset + x * box_size, offset + y * box_size, box_size * 0.5)
                color = self.__getColorForIntensity(pixel)
                draw.rectangle(bb, fill=color)

        del draw
        smaller_image.close()
        bw_image.close()
        return return_image
    
    def __scaleTuple(self, tpl, scalar, forceint = False):
        if forceint:
           return tuple(int(scalar * x) for x in tpl)
        else:
           return tuple(scalar * x for x in tpl)
    
    def __getBoundingBox(self, x, y, box_size):
        upper_left = (x - (box_size * 0.5), y - (box_size * 0.5))
        lower_right = (x + (box_size * 0.5), y + (box_size * 0.5))
        return (upper_left, lower_right)

    def __getColorForIntensity(self, intensity):
        return (int(intensity),0,0)
