# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
cashier2 = Staff.objects.create(full_name = "Петров Петр Петрович",
                                choices = "CA",
                                labor_contract = 4355)

class Staff(models.Model):
    #stuff = models.AutoField()-ебонная ошибка на 2 дня#
    full_name = models.CharField(max_length = 64)
    position = models.CharField(max_length = 2,
                                choices = POSITIONS,
                                default = cashier)
    labor_contract = models.IntegerField()

    def get_last_name(self):
        return self.full_name.split()[0]



director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

class Staff(models.Model):
    #stuff = models.AutoField()-ебонная ошибка на 2 дня#
    full_name = models.CharField(max_length = 64)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=cashier)
    labor_contract = models.IntegerField()

    def get_last_name(self):
        return self.full_name.split()[0]

cashier1 = Staff.objects.create(full_name = "Иванов Иван Иванович",
                                position = 'CA',
                                labor_contract = 1754)
cashier2 = Staff.objects.create(full_name = "Петров Петр Петрович",
                                position = 'CA',
                                labor_contract = 4355)
direct = Staff.objects.create(full_name = "Максимов Максим Максимович",
                                position = 'DI',
                                labor_contract = 1254)

cashier3 = Staff.objects.create(full_name = "Петров Петр Петрович",
                                position = 'CA',
                                labor_contract = 1155)



1. user1 = User.objects.create_user(username= "randomName")
2. rand_aut = Author.objects.create(relation = "user1")
3. random_cat_name = Category.objects.create(namecat = "randomName")
4. Post.objects.create(post_author = rand_aut, field_choise = 'NW', title = 'randomtitle', text = 'randomtext)')
5. Post.objects.get(id = 1).PostCategory.add(Category.objects.get(id = 2))
6. Comment.objects.create(post_comm = Post.objects.get(id = 3), user_comm = Author.objects.get(id = 2).relation, comm_text = 'text')
7. Comment.objects.get(id=1).like()
Post.objects.get(id=2).dislike()
8.Author.objects.get(id=1).update_rating()
9.top_aut = Author.objects.order_by("-rating_aut")[:1]
for i in top_aut:
    i.rating_aut
    i.relation.username
top_post - Post.objects.order_by("-rating_post")
for i in top_post:
    i.time_wr
    i.post_category
    i.title
    i.post_text
