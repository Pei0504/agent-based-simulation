class Agent:
    def __init__(self, id, position):
        self.id = id
        self.position = position

    def move(self, world):
        new_position = self.find_empty_patch(world)
        if new_position:
            world.grid[self.position[0]][self.position[1]] = None
            self.position = new_position
            world.grid[new_position[0]][new_position[1]] = self

    def find_empty_patch(self, world):
        for i in range(world.size):
            for j in range(world.size):
                if world.grid[i][j] is None:
                    return (i, j)
        return None

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

world = World(5)
for i in range(3):
    agent = Agent(i, (i, i))
    world.add_agent(agent)

for _ in range(5):
    world.step()

