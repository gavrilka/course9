import requests
import json
import re

def read_file_data(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_to_file_data(filename, content, mode='w'):
    # mode w - rewrite
    # mode a - append
    with open(filename, mode=mode) as f:
        f.write(content)

#url = 'https://jsonplaceholder.typicode.com/comments'
def get_request(url):
    r = requests.get(url)
    if r.status_code == 200:
        headers = dict(r.headers)
        obj = json.loads(r.content)
        for key, value in headers.items():
            print('{}: {}'.format(key, value))
        write_to_file_data('site_response.json', json.dumps(obj, sort_keys=True, indent=4))
    else:
        raise RuntimeError("Request from url = '{}' ended with code {}".format(url, r.status_code))

    #print('Status code: ', r.status_code)
    #print('Headers: ', r.headers)
    #print('Content: ', r.content)
#+ Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
#При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
#Ответить себе на вопрос удобно ли так делать?
def get_habrhabr(url):
    r = requests.get(url)
    links = re.findall(r'href="(http.*?)"', r.text)
    return links
if __name__ == '__main__':
    # reading
    #print(read_file_data('text.txt'))
    #writing
    #write_to_file_data("text.txt", '\nARAM KRASAVA', 'w')
    #get_request('https://jsonplaceholder.typicode.com/comments')
    print(get_habrhabr('https://habrahabr.ru/'))