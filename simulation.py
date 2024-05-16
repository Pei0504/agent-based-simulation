import random

class Agent:
    def __init__(self, id, position):
        self.id = id
        self.position = position

    def move(self, world):
        empty_patches = self.find_empty_patches(world)
        if empty_patches:
            new_position = random.choice(empty_patches)
            world.grid[self.position[0]][self.position[1]] = None
            self.position = new_position
            world.grid[new_position[0]][new_position[1]] = self

    def find_empty_patches(self, world):
        empty_patches = []
        for i in range(world.size):
            for j in range(world.size):
                if world.grid[i][j] is None:
                    empty_patches.append((i, j))
        return empty_patches

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = []
        self.initialize_agents(num_agents)

    def initialize_agents(self, num_agents):
        for i in range(num_agents):
            position = self.find_empty_patch()
            agent = Agent(i, position)
            self.agents.append(agent)
            self.grid[position[0]][position[1]] = agent

    def find_empty_patch(self):
        empty_patches = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] is None]
        return random.choice(empty_patches) if empty_patches else None

    def step(self):
        for agent in self.agents:
            agent.move(self)

    def display(self):
        for row in self.grid:
            print(row)
        print("--------")


world = World(size=5, num_agents=3)  

# 運行模擬
for _ in range(5):  
    world.step()
    world.display() 


