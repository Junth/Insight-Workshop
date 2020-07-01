# Question 16: Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.



# States: ['dead', 'allow_fireball', 'jump', 'crouch', ...]
# Forces: ['x_velocity', 'y_velocity', 'max_x_vel', 'max_y_vel', 'x_acceleration', 'gravity', ...]


class Mario(Object):
    def __init__(self):
        self.states = states
        self.forces = forces
        self.life_count = life_count
        self.timer = timer
        
    def get_image():
        """Extracts image"""
        pass
    
    def update():
        """Updates Mario's states and animations once per frame"""
        pass
    
    def handle_state():
        """Determines Mario's behavior based on his state"""
        pass
    
    def check_to_allow_fireball():
        """Check to allow the shooting of a fireball"""
        pass
    
    def shoot_fireball():
        """Shoots fireball, allowing no more than two to exist at once"""
        pass
    
    def changing_to_big():
        """Changes Mario's image attribute based on time while
        transitioning to big"""
        pass
    
    def death_mario():
        """logic for mario death"""
        pass
        
        
        
        