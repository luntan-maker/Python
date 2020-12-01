import wikipediaapi as wiki
import os

def get_page(str_of):
    wik = wiki.Wikipedia('en')
    # page_py = wik.page('Diophantine equation')
    return wik.page(str_of)

def get_and_check(str_of):
    page = get_page(str_of)
    if page.exists():
        return page
    else:
        print("Page '" + str_of + "' doesn't exist")

def get_page_links(page):
    return set(page.links.keys())

def iterate_links(links):
    set_of = set()
    for link in links:
        print(link)
        new_page = get_and_check(link)
        set_of = set_of.union(get_page_links(new_page))
    return set_of

#Set2 > set1
#Yes A-B != B-A
def set_delta(set1, set2):
    return len(set2.difference(set1))

def get_pages(links_of):
    set_of = set()
    for i in links_of:
        set_of = set_of.union(s)

def get_summary(page_of):
    return page_of.summary

def get_many_pages(pages_of):
    set_of = set()
    for i in pages_of:
        # print(i)
        temp = get_page(i)
        set_of.add(temp)
    return set_of

def get_many_summary(pages_of):
    set_of = set()
    for i in pages_of:
        print(i)
        set_of.add(i.summary)
    return set_of

def split_and_flatten(set_of):
    list_of = list(set_of)
    list_to = list()
    for i in list_of:
        list_to.append(i.split("."))
    list_to = [item for sublist in list_to for item in sublist]
    return list_to

def clean_summary(text_of):
    return text_of.strip('\n')

def write_file(direc, name_of, text_of):
    with open(os.path.join(direc, name_of), "w") as f:
        f.write(text_of)

test_page = get_and_check("Diophantine equation")
links_of = get_page_links(test_page)
# children_links = iterate_links(links_of)
# print(set_delta(links_of, children_links))
# temp = clean_summary(get_summary(test_page)).split(".")
pages_of = get_many_pages(links_of)
summary_of = get_many_summary(pages_of)
summary_list = split_and_flatten(summary_of)
# from gensim.test.utils import common_texts
from gensim.models import Word2Vec

model = Word2Vec(sentences=summary_list, window=5, min_count=1, workers=4)
model.save("word2vec.model.wiki.summary.unclean")

# dir_to = r'C:\Users\lucas\Code\Python\wiki_data'
# name_of = "Test.txt"
# text_of = "Dummy text"
# write_file(dir_to, name_of, text_of)
