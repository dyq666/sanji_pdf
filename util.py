__all__ = (
    'build_watermark',
    'make_opacity',
)

from PIL import Image


def build_watermark(img_path, save_path, top, right, bottom, left):
    """生成一张水印图片.

    水印图片的大小等于页面大小减去上下左右 padding, 由于图片以像素为单位, 因此还需将大小转为像素.
    页面默认大小是 a4 (210mm * 297mm), 96 dpi.
    """

    def _mm_to_px(mm):
        dpi = 96
        mm_to_inch = 0.0393701
        return mm * mm_to_inch * dpi

    bg_size = (210 - left - right, 297 - top - bottom)
    bg_px = [int(_mm_to_px(i)) for i in bg_size]
    bg = Image.new('RGBA', bg_px, (255, 255, 255, 0))

    # 再中间放上水印图片
    img = Image.open(img_path)
    img_w, img_y = img.size
    bg_w, bg_y = bg.size
    offset = (bg_w - img_w) // 2, (bg_y - img_y) // 2

    bg.paste(img, offset)
    bg.save(save_path)


def make_opacity(opacity, img_path, save_path):
    """改变图片透明度, 如果像素是白色则改为透明"""

    img = Image.open(img_path)
    new_data = [
        [px[0], px[1], px[2], (int(255 * opacity) if px[:3] != (255, 255, 255) else 0)]
        for px in img.getdata()
    ]
    img.putdata(new_data)
    img.save(save_path)
