

from bs4 import BeautifulSoup

# with open('poe_div_cards.html', 'r', encoding='utf8') as html:
#     content = html.read()
#     # print(content)
#
#     html_object = BeautifulSoup(content, 'lxml')
#     skin = html_object.prettify()
#
#     table_el = html_object.find_all('table')


def download(url, file_path, file_name, file_format):
    from os import chdir
    import urllib.request

    chdir(file_path)
    full_path = file_path + file_name + file_format
    urllib.request.urlretrieve(url, full_path)


with open('div_cards.html', 'r', encoding='utf8') as html:
    content = html.read()
    html_obj = BeautifulSoup(content, 'lxml')
    # print(html_obj.prettify())

    for tag in html_obj.find_all('th'):
        print(tag)

    # for pos, tag in enumerate(html_obj.find_all('a')):
    #     each_tag = str(tag)
    #     tag_link = each_tag.split('href="')[1].split(' ')[0].replace('"', '')
    #     img_name = tag_link.split('wiki')[1].replace('/', '')
        # print([pos], tag_link)
        # print([pos], img_name)

        # download(
        #     url=tag_link,
        #     file_path='C:/Users/lucasf/PycharmProjects/python_my_db/assunto_BIBLIOTECAS/beautifulsoup/img',
        #     file_name=img_name,
        #     file_format='.png'
        # )
