from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

url="http://ict.hanyang.ac.kr"

def get_adjunct():
    with urllib.request.urlopen(
            "http://ict.hanyang.ac.kr/members/professor.php?ptype=list&code=professor&category=59") as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

    photo = []
    name_kor = []
    name_eng = []
    position = []
    location = []
    call = []
    email = []

    for x in soup.find_all("td", class_="organ_list"):
        name_kor.append(x.find("td", class_="or_name").find('a').string)
        phourl=url+x.find("img")["src"]
        photo.append(phourl)
        for th in x.find_all("th", class_="or_tit"):
            if th.string == "영문명":
                name_eng.append(th.next_sibling.next_sibling.string)
            elif th.string == "직위":
                position.append(th.next_sibling.next_sibling.string)
            elif th.string == "위치":
                location.append(th.next_sibling.next_sibling.string)
            elif th.string == "이메일":
                e = th.next_sibling.next_sibling.find('a').next_element.next_element.string
                e = e.replace(" ", "")
                e = e.replace("\t", "")
                email.append(e)
            elif th.string == "전화번호":
                call.append(th.next_sibling.next_sibling.next_element.next_element.string)

    return {"name_kor": name_kor,
            "name_eng": name_eng,
            "position": position,
            "location": location,
            "call": call,
            "email": email,
            "photo": photo}


def get_prof():
    with urllib.request.urlopen(
            "http://ict.hanyang.ac.kr/members/professor.php?ptype=list&code=professor&category=43") as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

    photo = []
    name_kor = []
    name_eng = []
    position = []
    location = []
    call = []
    email = []

    for x in soup.find_all("td", class_="organ_list"):
        name_kor.append(x.find("td", class_="or_name").find('a').string)
        phourl=url+x.find("img")["src"]
        photo.append(phourl)
        for th in x.find_all("th", class_="or_tit"):
            if th.string == "영문명":
                name_eng.append(th.next_sibling.next_sibling.string)
            elif th.string == "직위":
                position.append(th.next_sibling.next_sibling.string)
            elif th.string == "위치":
                location.append(th.next_sibling.next_sibling.string)
            elif th.string == "이메일":
                e = th.next_sibling.next_sibling.find('a').next_element.next_element.string
                e = e.replace(" ", "")
                e = e.replace("\t", "")
                email.append(e)
            elif th.string == "전화번호":
                call.append(th.next_sibling.next_sibling.next_element.next_element.string)
    return {"name_kor": name_kor,
            "name_eng": name_eng,
            "position": position,
            "location": location,
            "call": call,
            "email": email,
            "photo": photo}


