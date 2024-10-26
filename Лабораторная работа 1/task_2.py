# TODO Найдите количество книг, которое можно разместить на дискете

disk_size_in_mb = 1.44
count_of_letter = 100
count_of_str = 50
count_of_symbols_in_one_str = 25
one_symbol = 4

disk_size_in_b = disk_size_in_mb * 1024 ** 2
size_one_book = one_symbol * count_of_symbols_in_one_str * count_of_str * count_of_letter
count_of_book = disk_size_in_b // size_one_book
print("Количество книг, помещающихся на дискету:", count_of_book)
