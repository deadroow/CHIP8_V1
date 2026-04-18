from app import Chip8

machine = Chip8()
machine.load_rom(path='./data/chip8_softwares/test.ch8')
for i in range(6):
    machine.steps()
