from bs4 import BeautifulSoup
import json

def text2json(base_file_path):
    content2dict = {}
    for chapter in range(1, 10):
        with open('{0}-{1}.xhtml'.format(base_file_path, chapter)) as f:
            content = f.read()
            s = BeautifulSoup(content, 'html.parser')
            for index, p in enumerate(s.find_all('p')):
                key = '{0}.{1}'.format(chapter, index + 1)
                line = p.text
                content2dict[key] = line

    return content2dict

def write2file(file_path, content):
    with open(file_path, 'w+') as f:
        f.write(json.dumps(content, indent=4, sort_keys=True))

if __name__ == "__main__":
    content = text2json("text/book")
    write2file("text/content.json", content)
