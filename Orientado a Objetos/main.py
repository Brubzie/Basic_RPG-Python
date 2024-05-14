class Personagem:
    def __init__(self, nome: str, level: int, exp: int, exp_max: int, hp: int, hp_max: int, dano: int):
        self.nome = nome
        self.level = level
        self.exp = exp
        self.exp_max = exp_max
        self.hp = hp
        self.hp_max = hp_max
        self.dano = dano

    def exibir(self):
        print(f'Nome: {self.nome} | Level: {self.level} | Dano: {self.dano} | HP: {self.hp}/{self.hp_max} | EXP: {self.exp}/{self.exp_max}')

    def reset(self):
        self.hp = self.hp_max

    def level_up(self):
        if self.exp == self.exp_max:
            self.level += 1
            self.exp = 0
            self.exp_max = self.exp_max * 2
            self.hp_max += 20

    def atacar(self, outro):
        outro.hp -= self.dano

class NPC(Personagem):
    def __init__(self, level):
        super().__init__(f'Monstro #{level}', level, 0, 0, 100 * level, 100 * level, 5 * level)
        self.exp = 7 * level

class Player(Personagem):
    pass

class Jogo:
    def __init__(self, n_npcs):
        self.lista_npcs = [NPC(i + 1) for i in range(n_npcs)]
        self.player = Player('Bruno', 1, 0, 35, 100, 100, 25)

    def exibir_npcs(self):
        for npc in self.lista_npcs:
            npc.exibir()

    def iniciar_batalha(self, npc):
        while self.player.hp > 0 and npc.hp > 0:
            self.player.atacar(npc)
            npc.atacar(self.player)
            self.exibir_info_batalha(npc)

        if self.player.hp > 0:
            print(f'O jogador {self.player.nome} venceu e ganhou {npc.exp} de EXP!')
            self.player.exp += npc.exp
            self.player.level_up()
            self.player.exibir()
        else:
            print(f'O NPC {npc.nome} venceu!')
            npc.exibir()

        npc.reset()
        self.player.reset()

    def exibir_info_batalha(self, npc):
        print(f'Player HP: {self.player.hp}/{self.player.hp_max}')
        print(f'NPC {npc.nome}: {npc.hp}')
        print('-' * 50, end = '\n\n')

jogo = Jogo(5)
for _ in range(6):
    jogo.iniciar_batalha(jogo.lista_npcs[0])
