from importlib.resources import contents
from bs4 import BeautifulSoup

# abrir o arquivo home.html apenas para leitura
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    # criamos uma variável que será uma instância do BeatifulSoup 
    # passamos o conteúdo da página que estamos scrapianfo e o método de transformação que desejamos
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # encontramos a primeira ocorrência da tag h5
    # first_tag_h5 = soup.find('h5')
    # print(first_tag_h5)

    # encontramos todas as ocorrências da tag h5
    # tags_h5 = soup.find_all('h5')
    # print(tags_h5)

    # exploramos as informações das tags h5
    # for tag_h5 in tags_h5:
    #     print(f'{tag_h5.name} -> {tag_h5.text} -> {tag_h5.attrs}')

    # encontrar o nome e o custo de cada um dos cursos
    course_cards = soup.find_all(class_='card')
    total_price = 0
    for course in course_cards:
        course_name = course.h5.text
        course_price = int(course.a.text[:-1].split()[-1])
        print(f'{course_name} -> {course_price}')
        total_price += course_price
    
    # somar custo total dos cursos
    print(f'-------------------------------')
    print(f'total_price = {total_price}')


