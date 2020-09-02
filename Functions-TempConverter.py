train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp 

f100_in_celcius = f_to_c(100)


def c_to_f(c_temp):
  f_temp = (c_temp * (9/6)) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)


def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(22680, 10) 

print("The GE train supplies " + str(train_force) + " Newtons of force. ")


def get_energy(mass, c = 3*10**8):
  get_energy = mass * c
  return mass

bomb_energy = get_energy(1, c = 3*10**8)

print("A 1KG bomb supplies " + str(bomb_energy) + " Joules.")


def get_work(mass, acceleration):
  return 226800 * 100

train_work = get_work(22680, 10)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")



















