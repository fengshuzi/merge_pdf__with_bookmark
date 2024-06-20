import PyPDF2
import os
import sys


def merge_with_bookmarks(pdf_dir):
    pdf_files = []

    for file_name in os.listdir(pdf_dir):
        if file_name.endswith('.pdf'):
            pdf_files.append(file_name)

    pdf_files = sorted(pdf_files, key=lambda x: str.lower(x))  # 按字典顺序排序
    pdf_writer = PyPDF2.PdfFileWriter()
    page_num = 0  # 记录已添加的页面数

    for file_name in pdf_files:
        pdf_reader = PyPDF2.PdfFileReader(open(os.path.join(pdf_dir, file_name), 'rb'))
        num_pages = pdf_reader.numPages

        for page_index in range(num_pages):
            page = pdf_reader.getPage(page_index)
            pdf_writer.addPage(page)
            page_num += 1

        # 使用文件名作为书签标题
        bookmark_title = os.path.splitext(os.path.basename(file_name))[0]
        bookmark_dest = pdf_writer.addBookmark(bookmark_title, page_num - (num_pages))  # 添加书签到每个PDF的第一页


    # 使用文件夹名称作为PDF名称
    folder_name = os.path.basename(pdf_dir)
    pdf_name = f"{folder_name}.pdf"

    with open(pdf_name, 'wb') as pdf_output:
        pdf_writer.write(pdf_output)

    print("congratulations  pdf merge success:", pdf_name)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("need dir!!!")
        sys.exit(0)
    merge_with_bookmarks(sys.argv[1])