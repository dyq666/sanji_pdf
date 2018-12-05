from PIL import Image
from lxml.builder import E

def print_control_chars():
    """查看 lxml 无法转换的控制字符"""
    # 0-31, 127 为控制字符
    control_chars = [i for i in range(32)] + [127]

    for i in control_chars:
        try:
            E.p(chr(i))
        except ValueError:
            fmt = '{:<3} {}'
            print(fmt.format(i, repr(chr(i))))


def change_opacity(opacity, img_path, save_path):
    """去除图片白底, 并改变其他的透明度"""

    assert save_path.endswith('.png'), 'save_path ext must be .png'

    img = Image.open(img_path)
    new_data = [(px[0], px[1], px[2], int(255 * opacity) if px[:3] != (255, 255, 255) else 0)
                for px in img.getdata()]
    img.putdata(new_data)
    img.save(save_path)


def build_watermark(img_path, save_path, top, right, bottom, left):
    """
    生成一张符合 pdf 大小的图片.
    wkhtmltopdf 默认情况下 a4 大小 (210mm * 297mm), dpi 96 (每英寸 96 像素)
    """

    assert save_path.endswith('.png'), 'save_path ext must be .png'

    def _mm_to_px(mm):
        dpi = 94
        mm_to_inch = 0.0393701
        return mm * mm_to_inch * dpi

    bg_size = (210 - left - right, 297 - top - bottom)
    bg_px = [int(_mm_to_px(i)) for i in bg_size]
    bg = Image.new('RGBA', bg_px, (255, 255, 255, 0))

    img = Image.open(img_path)
    img_w, img_y = img.size
    bg_w, bg_y = bg.size
    offset = (bg_w - img_w) // 2, (bg_y - img_y) // 2

    bg.paste(img, offset)
    bg.save(save_path)
