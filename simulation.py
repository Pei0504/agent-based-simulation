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
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)
        self.grid[agent.position[0]][agent.position[1]] = agent

    def step(self):
        for agent in self.agents:
            agent.move(self)

    def display(self):
        for row in self.grid:
            print(row)
        print("--------")


world = World(5)  
for i in range(3):  
    agent = Agent(i, (i, i))
    world.add_agent(agent)

# 運行模擬
for _ in range(5):  
    world.step()
    world.display()  


