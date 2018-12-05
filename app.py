import os

import pdfkit


BIN_FILE = './static/bin/wkhtmltopdf'
HTML_DIR = './static/html/'
OUT_PATH = './out/example.pdf'


def build_pdf():
    html_files = ('home.html', 'text.html')
    html_paths = [os.path.join(HTML_DIR, fn) for fn in html_files]

    # 参数文档 https://www.bookstack.cn/read/wkhtmltopdf_en/intro.md
    pdf_options = {
        '--margin-top': '25mm',
        '--margin-left': '25mm',
        '--margin-right': '25mm',
        '--margin-bottom': '25mm',
        '--header-center': 'dyq666 - test pdf',
        '--header-spacing': 10,
        '--header-font-size': '8',
        '--footer-center': '[page] / [toPage]', # [xx] 会自动转换成页数
        '--footer-spacing': 10,
        '--footer-font-size': '8',
    }
    pdfkit.from_file(html_paths, OUT_PATH, options=pdf_options)
    # 指定目录的方式
    # config = pdfkit.configuration(wkhtmltopdf=BIN_FILE)
    # pdfkit.from_file(html_paths, OUT_PATH, configuration=config, options=pdf_options)


if __name__ == '__main__':
    build_pdf()
