from ..decorators import check_path , get_data_factory, check_rom_factory

from utils import display_msg

class Chip8:
    W=64
    H=32

    def __init__(self):
        self.memory=[0]*4096
        self.V=[0]*16
        self.keys=[0]*16
        self.pc=0x200
        self.stack=[0xF]
        self.I=0
        self.sound=0
        self.delay=0
        self.ecran=[]*self.W*self.H
        self.draw_flag=False 
        self.fontset=[
    0xF0, 0x90, 0x90, 0x90, 0xF0, 0x20, 0x60, 0x20, 0x20, 0x70, # 0 et 1
    0xF0, 0x10, 0xF0, 0x80, 0xF0, 0xF0, 0x10, 0xF0, 0x10, 0xF0, # 2 et 3
    0x90, 0x90, 0xF0, 0x10, 0x10, 0xF0, 0x80, 0xF0, 0x10, 0xF0, # 4 et 5
    0xF0, 0x80, 0xF0, 0x90, 0xF0, 0xF0, 0x10, 0x20, 0x40, 0x40, # 6 et 7
    0xF0, 0x90, 0xF0, 0x90, 0xF0, 0xF0, 0x90, 0xF0, 0x10, 0xF0, # 8 et 9
    0xF0, 0x90, 0xF0, 0x90, 0x90, 0xE0, 0x90, 0xE0, 0x90, 0xE0, # A et B
    0xF0, 0x80, 0x80, 0x80, 0xF0, 0xE0, 0x90, 0x90, 0x90, 0xE0, # C et D
    0xF0, 0x80, 0xF0, 0x80, 0xF0, 0xF0, 0x80, 0xF0, 0x80, 0x80  # E et F
]
        for i,glyphe in enumerate(self.fontset):
            self.memory[0x50+i]=glyphe
    @check_path
    @get_data_factory()
    @check_rom_factory(checklist=['len'])
    def load_rom(self,path, content=None):
        start=0x200
        end=start+len(content)
        self.memory[start:end]=content
        print(self.memory)

    def fetch(self):
        opcode_first_bytes = self.memory[self.pc]
        opcode_second_bytes= self.memory[self.pc+1]
        opcode=opcode_first_bytes<<8|opcode_second_bytes
        display_msg(opcode, "04X")
        self.pc+=(2 & 0xFFF)
        return opcode

    def steps(self):
        opcode=self.fetch()
        kk=opcode & 0x00FF
        x= (opcode >> 8 )& 0xF
        y= (opcode >> 4) & 0xF
        n= opcode & 0xF
        NNN= opcode & 0x0FFF

        if opcode == 0x00E0:
            display_msg("Clear the screen")
            self.ecran=[0]*self.W*self.H
            return
        if opcode == 0x00EE:
            display_msg("LIFO-> pc value")
            self.pc = self.stack.pop()
            return
        
        if (opcode & 0xF000)==0x6000:
            self.V[x]=kk
            return
        
        if (opcode & 0xF000)== 0x1000:
            display_msg(f"V[{x}]= {kk}")
            self.pc = NNN
            return
        
        if (opcode & 0xF000)== 0xA000:
            self.I=NNN
            return 
        
        if (opcode & 0xF000) == 0xD000:
            self.V[0xF]=0
            for row in range(n):
                spr=self.memory[(self.I+row)& 0xFFF]
                for bit in range(8):
                    if spr & (0x80>>bit):
                        xi=(self.V[x]+bit)% self.W
                        yi=(self.V[y]+bit)% self.H
                        idx= xi +yi *self.W
                        self.V[0xF] |= self.ecran[idx]
                        self.ecran[idx] ^=1
                self.draw_flag=True
                return
        display_msg("opcode unknown", "danger")

        