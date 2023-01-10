

train_mass = 0
train_acceleration = 0
train_distance = 0
bomb_mass = 0



def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

def average(num1, num2):
  return (num1 + num2) / 2

def win_percentage(wins, losses):
  total_games = wins + losses
  ratio_won = wins / total_games
  return ratio_won * 100

def square_root(num):
  return num ** 0.5

def tenth_power(num):
  return num ** 10





def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5 / 9 
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)


c0_in_fahrenheit = c_to_f(0) 
print(c0_in_fahrenheit)


def get_force(mass, acceleration):
  return mass * acceleration

def get_energy(mass, c = 3*10**8):
  return mass + c * c 

def get_work(mass,acceleration,distance):
  return get_force(mass,acceleration) * distance

bomb_mass = 0
bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")


train_mass = 0
train_accleration = 0
train_distance = 0
train_force = get_force(train_mass, train_accleration)

print("The GE train supplies " + str(train_force) +  " Newtons of force.")


train_work = get_work(train_mass, train_acceleration, train_distance)
