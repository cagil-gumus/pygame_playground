import numpy as np

class object:
  def __init__(self, 
               init_position, # left is pos, right is neg, up is neg, down is pos 
               init_velocity, # left is pos, right is neg, up is pos, down is neg
               weight,
               gravity, # Scalar
               radius,
               screen_width,
               screen_height,
               air_resistance,
               dt_speed_up_factor
               ):
    
    self.position = np.asarray(init_position) # m 
    self.velocity = np.asanyarray(init_velocity) # m/s^2
    self.weight = weight # kg
    self.gravity = gravity # in m/s^2 Scalar value
    self.acceleration = np.zeros(2)
    self.force = np.zeros(2)
    self.go_down = False
    self.go_up = False
    self.go_left = False
    self.go_right = False
    self.dt = None
    self.collision_x = False
    self.collision_y = False
    self.radius = radius
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.air_resistance =  air_resistance
    self.dt_speed_up_factor = dt_speed_up_factor

  def update_dt(self, dt):
    # Update important variables between delta-time
    self.dt = dt * 10
    self.handle_collision()
    self.update_acceleration()
    self.update_velocity()
    self.update_position()
    self.print_all_info()

  # Things dt can effect:
  def update_position(self):
      self.position += self.velocity * self.dt
  
  def update_velocity(self):
    self.velocity += self.acceleration * self.dt
    
  
  def update_acceleration(self):

    if self.collision_x:
      self.acceleration[0] *= -0.8
      self.velocity[0] *= -0.8

    if self.collision_y:
      self.acceleration[1] *= -0.8
      self.velocity[1] *= -0.8

    if self.go_up:
      self.acceleration[1] = -30
    elif self.go_down:
      self.acceleration[1] = 15
    else:
      self.acceleration[1] = self.gravity

    if self.go_left and not self.go_right:
      self.acceleration[0] = -30
    elif not self.go_left and self.go_right:
      self.acceleration[0] = 30
    elif self.velocity[0] < 0: 
      self.acceleration[0] = self.air_resistance
    elif self.velocity[0] > 0:
      self.acceleration[0] = -1*self.air_resistance
    else:
       self.acceleration[0] = 0

  def handle_collision(self):
      if (self.position[0] - self.radius < 0):
        self.collision_x = True
        self.position[0] = self.radius
      elif (self.position[0] + self.radius) > self.screen_width:
        self.collision_x = True
        self.position[0] = self.screen_width - self.radius
      else:
          self.collision_x = False
      
      if (self.position[1] - self.radius < 0):
        self.collision_y = True
        self.position[1] = self.radius
      elif (self.position[1] + self.radius > self.screen_height):
        self.collision_y = True
        self.position[1] = self.screen_height - self.radius
      else:
          self.collision_y = False

  def print_all_info(self):
    print("Force: {}".format(self.force))
    print("Position: {}".format(self.position))
    print("Velocity: {}".format(self.velocity))
    print("Acceleration: {}".format(self.acceleration))        
    print("Dt: {}".format(self.dt))
    print("Collision-X: {}".format(self.collision_x))
    print("Collision-y: {}".format(self.collision_y))