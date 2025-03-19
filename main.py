import random
import pickle
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import copy
import skimage.io as io


def hello_world():
    print('hello world')


def deci_to_base(num, base):
    q = num
    binary = ''
    while q != 0:
        rem = q % base
        q = q // base
        binary = str(rem) + binary
    print(binary)


def fahrenheit_to_celsius(temp):
    # (F-32)*5/9 = C
    cel = (temp - 32) * 5 / 9
    print(cel)


def echo():
    user_in = input("Please type something: ")
    print('User has typed:', user_in)


def simple_calc():
    user_in1 = input("Pls type an int: ")
    user_in2 = input("Pls type an int: ")
    try:
        user_in1 = int(user_in1)
        user_in2 = int(user_in2)
        ans = user_in1 + user_in2

    except ValueError:
        print("Either input was not integer")
        exit()

    print(ans)


def input_newline():
    user_in = input("Pls type something: ")
    print(user_in)
    print("newline")


def even_or_odd(num):
    if num % 2 == 0:
        print(num, " is an even number")
    else:
        print(num, " is an odd number")


def print_line(char, cols):
    line = char * cols
    print(line)


def print_box(char, cols, rows):
    for i in range(rows):
        print_line(char, cols)


global_var = 10


def change_global_var(num: int):
    global global_var
    global_var = num


def print_global_var():
    print(global_var)


def is_prime_number(num):
    """ (int) -> bool
    Returns a boolean value whether the input is a prime number or not.
    >>> is_prime_number(10)
    False
    >>> is_prime_number(7)
    True
    >>> is_prime_number(2)
    True
    """
    is_prime = True
    for i in range(num - 2):
        if num % (i + 2) == 0:
            is_prime = False
    return is_prime


def guess_it():
    rand_num = random.randint(0, 100)
    guess = int(input("Please try to guess the random int: "))
    correct_guess = False
    while not correct_guess:
        if rand_num > guess:
            print("Your guess is too low")
            guess = int(input("Guess again: "))
        elif rand_num < guess:
            print("Your guess is too high")
            guess = int(input("Guess again: "))
        else:
            correct_guess = True
            print("Congratulations you are correct!")


def smallest_divisor(num):
    smallest_div = 1
    for i in range(num - 2):
        if num % (i + 2) == 0:
            smallest_div = i + 2
            break
    return smallest_div


def largest_divisor(num):
    largest_div = num
    for i in range(num - 2):
        if num % (i + 2) == 0:
            largest_div = i + 2
    return largest_div


def is_vowel(c):
    vowels = ["a", "e", "i", "o", "u"]
    c = c.lower()
    if len(c) != 1:
        raise ValueError("The input was not a single character")
    elif c in vowels:
        return True
    else:
        return False


def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    string = string.lower()
    num_vowels = 0
    for i in vowels:
        num_vowels += string.count(i)
    return num_vowels


def pet_list(num):
    pet_names = []
    for i in range(num):
        name = input("Please insert a pet name: ")
        pet_names.append(name)
    for j in pet_names:
        print(j)
    return pet_names


def print_list(in_list):
    for i in in_list:
        print(i)


def int_ind(ints):
    for i in range(len(ints)):
        ints[i] += i
    return ints


def get_min(num_list):
    print(min(num_list))


def n_rand_nums(num):
    num_list = []
    for i in range(num):
        num_list.append(random.random())
    return num_list


def comp_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Please input two equal length lists")
    same_len = 0
    for i in range(len(list1)):
        if len(list1[i]) == len(list2[i]):
            same_len += 1
    print(same_len)


def words_letters(words, letters):
    for i in words:
        for j in range(len(i)):
            if i[j] not in letters:
                return False
    return True


def input_one(num):
    """ (int) -> bool
    Returns an exception if the input is not 1.
    >>> input_one(1)
    True
    >>> input_one("string")
    Traceback (most recent call last):
    ValueError: input is not one
    """
    if num != 1:
        raise ValueError("input is not one")
    return True


def write_file():
    filename = "quotes.txt"
    fobj = open(filename, "w")
    fobj.write("My first line in a file!!\n")
    fobj.write("This will appear on the second line(?)")
    fobj.close()


def pickle_write():
    a = [1, 3, 1001, 5, 'a', [7]]
    pick = open("write.pkl", "wb")
    # noinspection PyTypeChecker
    pickle.dump(a, pick)
    pick.close()


def pickle_read():
    with open("write.pkl","rb") as pick:
        a = pickle.load(pick)
        print(a)


def paragraph_words(filename):
    with open(filename,"r") as f:
        para = f.read()
        words = [word.lower() for word in para.split() if word.isalpha()]
        words = list(set(words))
    return words


def write_words(filename,strings):
    with open(filename,"w") as f:
        for word in strings:
            f.write(word + "\n")

def join_words(filename,strings):
    with open(filename,"w") as f:
        words = "\n".join(strings)
        f.write(words)


def read_csv(filename):
    with open(filename,"r") as f:
        mat = []
        for line in f:
            line = line.strip("\n")
            line_list = line.split(",")
            mat.append(line_list)
    return mat


def write_phonebook():
    with open("phonebook.csv", "a") as pb:
        name = input("Please input contact name: ")
        while True:
            number = input("Please input contact number: ")
            while len(number) != 7:
                print("THIS IS AN INVALID PHONE NUMBER")
                number = input("Please input contact number: ")
            contact = name + "," + number + "\n"
            pb.write(contact)
            name = input("Please input contact name: ")
            if name == "stop":
                break


def card_pickle():
    rank = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
    suit = ["diamonds", "hearts", "clubs", "spades"]
    list_of_cards = []
    if os.path.exists("cards.pkl"):
        with open("cards.pkl","rb") as f:
            pickle_str = pickle.load(f)
            prev_cards = pickle_str.split(",")
            list_of_cards = list_of_cards + prev_cards
    with open("cards.pkl","wb") as f:
        in_rank = input("Please input a rank: ").lower()
        in_suit = input("Please input a suit: ").lower()
        while True:
            while in_rank not in rank:
                print("THIS IS AN INVALID RANK")
                in_rank = input("Please input a rank: ")
            while in_suit not in suit:
                print("THIS IS AN INVALID SUIT")
                in_suit = input("Please input a suit: ")
            card = suit.index(in_suit) * 13 + rank.index(in_rank)
            list_of_cards.append(str(card))
            in_rank = input("Please input a rank: ").lower()
            if in_rank == 'stop':
                break
            in_suit = input("Please input a suit: ").lower()
        pickle_str = ",".join(list_of_cards)
        # noinspection PyTypeChecker
        pickle.dump(pickle_str, f)
    for card in list_of_cards:
        int_card = int(card)
        card_rank = int_card % 13
        card_suit = int_card // 13
        print(rank[card_rank] + " of " + suit[card_suit])


def comp_202_dict():
    comp202_enrollment = {
        'Fall 2017': 816,
        'Winter 2018': 613,
        'Fall 2018': 709,
        'Winter 2019': 590,
        'Fall 2019': 744
    }
    tot_enrollment = 0
    semesters = 0
    for key in comp202_enrollment:
        semesters += 1
        tot_enrollment += comp202_enrollment[key]
    return tot_enrollment / semesters


def count_az(str_list):
    """ Makes a dict of how many of the strings start with A-Z """
    az_count = dict()
    for i in str_list:
        str_start = i[0]
        if str_start.isupper():
            if str_start in az_count:
                az_count[str_start] += 1
            else:
                az_count[str_start] = 1
    return az_count


def alph_check(to_check, alph):
    """ (str,str) -> dict
    Whether each character in alph appears in to_check.
    >>> alph_check('banana','abcd')
    {'a': True, 'b': True, 'c': False, 'd': False}
    >>> alph_check('dhgate','bbgd')
    {'b': False, 'd': True, 'g': True}
    """
    alph_list = sorted(list(set(alph)))
    check = []
    for i in alph_list:
        if i in to_check:
            check.append(True)
        else:
            check.append(False)
    alph_check_dict = dict(zip(alph_list, check))
    return alph_check_dict


def sum_even(int_list):
    even_sum = 0
    for index,num in enumerate(int_list):
        if index % 2 == 0:
            even_sum += num
    return even_sum

def avg(x):
    return sum(x) / len(x)

def get_indices(num_list,f):
    """ (list,function) -> list
    Evaluates the function on the list and return a list of indices
    where that element occurs.
    >>> nums = [5, 2, 2, 3]
    >>> get_indices(nums, max)
    [0]
    >>> get_indices(nums, avg)
    [3]
    >>> get_indices(nums, min)
    [1, 2]
    """
    x = f(num_list)
    indices = [i for i, val in enumerate(num_list) if val == x]
    return indices

class Student:
    """ This class represent students """

    num_students = 0

    def __init__(self,name="Jerry",id_num=000,course_list=[]):
        print("Creating a new student")
        self.name = name
        self.id = id_num
        self.courses = course_list
        Student.num_students += 1

    def display_info(self):
        print("Student name is : " + self.name)
        print("Student ID num is : " + str(self.id))
        print("Student's courses :", self.courses)

    def update_name(self,new_name):
        self.name = new_name

    def add_course(self,course_name):
        self.courses.append(course_name)

    def __str__(self):
        string = ""
        string += "Name: " + str(self.name) + "\n"
        string += "ID: " + str(self.id) + "\n"
        string += "Courses: " + str(self.courses)
        return string

def create_student(name,id_num):
    student = Student()
    student.name = name
    student.id = id_num
    return student

def id_num_comp(stud1,stud2):
    if stud1.id > stud2.id:
        return stud1.name
    else:
        return stud2.name

class Book:
    def __init__(self,id,title,author,genre,price):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    @classmethod
    def ten_dollar_book(cls,title,author):
        return Book(1001,title,author,"Novel",10.00)

    def __str__(self):
        return self.title + ": " + str(self.price)

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        return self.id == other.id

    def on_sale(self):
        new_price = ((self.price * 100) // 2) / 100
        self.price = new_price

    def is_cheaper(self,book):
        if self.price < book.price:
            return True
        else:
            return False

    def book_in_list(self,books):
        for book in books:
            if book.id == self.id:
                return True
        return False

    @staticmethod
    def books_to_dictionary(books):
        d = {}
        for book in books:
            if book.author not in d:
                d[book.author] = [book]
            else:
                d[book.author].append(book)
        return d

    @staticmethod
    def cheapest_book_author(books):
        """ A method that takes a dictionary mapping authors to books and
        returns a list containing the cheapest book from each author. """
        cheapest = []
        for author in books:
            cheapest_book = min(books[author],key=lambda book: book.price,default=None)
            cheapest.append(cheapest_book)
        return cheapest

class Bookstore:
    def __init__(self,name,library={}):
        self.name = name
        self.library = library

    def __str__(self):
        string = "\n".join(f"{book.title}: {book.price}" for book in self.library.values())
        return string

    def start_sale(self):
        for book in self.library.values():
            book.price = round(book.price/2,2)

    def books_by_genre(self,genre):
        books_in_genre = []
        for book in self.library.values():
            if book.genre == genre:
                books_in_genre.append(book.title)
        return books_in_genre

    def get_all_genres(self):
        return list({book.genre for book in self.library.values()})

    def find_cheapest(self,genre):
        filtered_books = [book for book in self.library.values() if book.genre == genre]
        return min(filtered_books, key=lambda book: book.price, default=None)

    def plot_by_genre(self):
        x = self.get_all_genres()
        genre_count = {genre: 0 for genre in x}
        for book in self.library.values():
            genre_count[book.genre] += 1

        plt.figure(figsize=(10, 10))
        plt.bar(genre_count.keys(), genre_count.values())
        plt.xlabel('Genres')
        plt.ylabel('Number of Books')
        plt.title(self.name + ' Books by Genre')
        plt.xticks(rotation=75,fontsize=10)
        plt.tight_layout()
        plt.savefig(self.name + '_by_genre.png')

    @classmethod
    def bookstore_from_list(cls,name,books_list):
        d = {}
        for book in books_list:
            d[book.id] = book
        return cls(name,d)

    @staticmethod
    def cheapest_in_bookstores(bookstores):
        d = {}
        for bookstore in bookstores:
            books_list = list(bookstore.library.values())
            books_dict = Book.books_to_dictionary(books_list)
            d[bookstore.name] = Book.cheapest_book_author(books_dict)
        return d

def create_bookstore_from_file(filename):
    book_dict = {}
    with open("City_Lights.txt","r") as f:
        for line in f:
            line = line.strip("\n")
            line_list = line.split(", ")
            book_id = int(line_list[0])
            title = line_list[1]
            author = line_list[2]
            genre = line_list[3]
            price = float(line_list[4].strip("$"))
            book = Book(book_id,title,author,genre,price)
            book_dict[book_id] = book
    bookstore_name = filename.strip(".txt").replace("_", " ")
    return Bookstore(bookstore_name,book_dict)

class Cat:

    cats_created = 0

    def __init__(self,name,age=0):
        self.name = name
        self.age = age
        Cat.cats_created += 1

    def __str__(self):
        string = self.name + ": " + str(self.age)
        return string

    def __eq__(self,other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

    def is_older_than(self,other_cat):
        if self.age > other_cat.age:
            return True
        else:
            return False

    @staticmethod
    def find_oldest(cats):
        oldest_idx = max(enumerate(cats), key=lambda cat: cat[1].age)[0]
        return oldest_idx

    @classmethod
    def from_birthdate(cls,name,date):
        now = datetime.date.today()
        age = (now-date).days
        return cls(name,age)


class CatShelter:
    def __init__(self,name,cats=[]):
        self.name = name
        self.cats = cats

    def __str__(self):
        string = "Welcome to " + self.name + "!\n"
        string += "We have " + str(len(self.cats)) + " cats\n"
        for i,cat in enumerate(self.cats):
            string += str(i) + ". " + cat.name + ": "
            string += str(cat.age) + " days old\n"
        return string

    def add_cat(self,cat):
        self.cats.append(cat)

    def adopt(self):
        adopted_cat = Cat.find_oldest(self.cats)
        return self.cats.pop(adopted_cat)

    @staticmethod
    def most_cats(shelter1,shelter2):
        if len(shelter1.cats) >= len(shelter2.cats):
            return shelter1
        else:
            return shelter2

if __name__ == '__main__':
    #hello_world()
    #deci_to_base(123,5)
    #fahrenheit_to_celsius(85)
    #echo()
    #simple_calc()
    #input_newline()
    #even_or_odd(766)
    #print_box('x',3,4)
    #change_global_var(29)
    #print_global_var()
    #print(is_prime_number(2))
    #guess_it()
    #print(smallest_divisor(121))
    #print(largest_divisor(97))
    #print(is_vowel("h"))
    #print(count_vowels("mimic"))
    #print_list(pet_list(5))
    #print(int_ind([5,2,-3,1,15]))
    #get_min([1,53,78,23,98,0.2,57.3])
    #print(n_rand_nums(7))
    #comp_lists(["cat","goat","house","puppy"],["cow","horse","dog","mouse"])
    #print(words_letters(["cat","rat","char","charter","truck"],"character"))
    #input_one(1)
    #write_file()
    #pickle_write()
    #pickle_read()
    #print(paragraph_words("paragraph.txt"))
    #write_words("words.txt",paragraph_words("paragraph.txt"))
    #join_words("joins.txt",paragraph_words("paragraph.txt"))
    #print(read_csv("movie_data.csv"))
    #write_phonebook()
    #card_pickle()
    #print(comp_202_dict())
    #print(count_az(['Dendrite','rate','Jersey','Gate','tomb','droid','Jacksonville']))
    #print(alph_check('banana', 'abcd'))
    #print(sum_even([10,3,37,57,34,55,86,45,34,54]))
    #nums = [5,2,2,3]
    #print(get_indices(nums,avg))
    # brent = create_student('Brent',999)
    # chris = create_student('Chris',193)
    # print(id_num_comp(chris,brent))
    # brent = Student('Brent',999)
    # def_stu = Student()
    # brent.update_name("Steven")
    # brent.add_course("COMP202")
    # print(brent)
    # holes = Book(999,"Holes","Judy Hops","Fiction",13.99)
    # divergent = Book(998,"Divergent","Joe Patterson","Fiction",10.99)
    # hope = Book(997,"Hope","Sarah Kim","Autobiography",23.83)
    # power = Book(996,"Power","Jim Beam","Autobiography",1.99)
    # mistakes = Book(101,"Mistakes","Christina Hughes","Autobiography",49.99)
    # empty = Book(345,"Empty","Gordon Howard","Dystopian",20.99)
    # collection = {holes.id:holes,divergent.id:divergent,hope.id:hope,power.id:power,mistakes.id:mistakes,empty.id:empty}
    # chapters = Bookstore("Chapters",collection)
    # print(chapters)
    # chapters.start_sale()
    # print(chapters)
    # print(chapters.books_by_genre("Autobiography"))
    # print(chapters.get_all_genres())
    # print(chapters.find_cheapest("Dystopian"))
    # chapters = create_bookstore_from_file("City_Lights.txt")
    # chapters.plot_by_genre()
    # b1 = Book(1,"Hello","John","Novel",10.22)
    # b2 = Book(2,"Intentions","John","Novel",4.22)
    # b3 = Book(3, "Toronto", "John", "Novel", 14.00)
    # b4 = Book(4,"Mention","Sam","Novel",12.85)
    # b5 = Book(5, "Bread", "Sam", "Novel", 32.99)
    # b6 = Book(6, "Studio", "Travis", "Novel", 60.91)
    # b7 = Book(7, "Hello", "John", "Novel", 10.22)
    # b8 = Book(8, "Intentions", "John", "Novel", 14.22)
    # b9 = Book(9, "Toronto", "John", "Novel", 14.00)
    # b10 = Book(10, "Mention", "Sam", "Novel", 42.85)
    # b11 = Book(11, "Bread", "Sam", "Novel", 22.99)
    # b12 = Book(12, "Studio", "Travis", "Novel", 60.99)
    # booklist1 = [b1,b2,b3,b4,b5,b6]
    # booklist2 = [b7,b8,b9,b10,b11,b12]
    # chapters = Bookstore.bookstore_from_list("Chapters",booklist1)
    # indigo = Bookstore.bookstore_from_list("Indigo",booklist2)
    # bookstores = [chapters,indigo]
    # print(Bookstore.cheapest_in_bookstores(bookstores))
    # b2 = copy.copy(b1)
    # print(b1 == b2)
    # date1 = datetime.date(2001,5,2)
    # my_cat = Cat.from_birthdate("Brent",date1)
    # cat1 = Cat("Jo",13)
    # cat2 = Cat("Cathy",9000)
    # cat3 = Cat("Bert",283)
    # cat4 = Cat("Bob",28)
    # cat5 = Cat("Jess",86)
    # cat6 = Cat("Seb",829)
    # cat7 = Cat("Kelly",10000)
    # cats1 = [my_cat,cat3,cat2,cat1]
    # cats2 = [cat6,cat5,cat4]
    # hope = CatShelter("Hope Shelter",cats1)
    # sc = CatShelter("Second Chance Shelter",cats2)
    # print(CatShelter.most_cats(hope,sc))
    # hope.adopt()
    # hope.adopt()
    # print(CatShelter.most_cats(hope,sc))
    image = io.imread("monkey.jpg")
    neg_image = 255 - image
    io.imshow(neg_image)
    io.show()