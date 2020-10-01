def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age


dads_age = calculate_age(2049, 1953) 

my_age = calculate_age(2049, 2033)


print("I am "+str(my_age) + " years old and my dad is " +str(dads_age) + " years old")