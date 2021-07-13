from tkinter import *
import math
import time


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Game")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)

        self.canvas = Canvas(self.tk, width=500, height=500)
        self.canvas.pack()

    def mainLoop(self):
        self.marine = Marine(64, 64, self.canvas)
        while True:
            if self.marine is not None:
                self.marine.update()
                if self.marine.remove_flag:
                    self.marine = None
            self.tk.update()
            time.sleep(0.01)


class Marine:
    def __init__(self, x, y, canvas):
        self.canvas = canvas

        # 현재 위치
        self.x = x
        self.y = y

        # 목표지점
        self.des_x = self.x
        self.des_y = self.y

        # 속도
        self.speed = 1

        # 유닛 상태
        self.is_stopped = True
        self.is_attacking = False
        self.is_dead = False
        self.remove_flag = False
        self.health = 5

        # 마우스 클릭 연결
        self.canvas.bind_all('<Button-3>', self.set_destination)
        self.canvas.bind_all('<Button-1>', self.set_attack)
        self.canvas.bind_all('<KeyPress>', self.set_health)

        # 표 크기 및 오프셋, 애니메이션 프레임 갯수
        self.sprite_row = 32
        self.sprite_column = 14

        # 왼쪽과 오른쪽 스프라이트 셋
        self.sprite_sheet_L = PhotoImage(file="Marine_L.gif")
        self.sprite_sheet_R = PhotoImage(file="Marine_R.gif")

        # 스프라이트 크기
        self.sprite_width = 64
        self.sprite_height = 64

        # 애니메이션을 위한 인덱스
        self.time_index = 0
        self.rot_index = 0

        # 애니메이션 이미지들을 담을 2차원 리스트
        self.animation_sprites = []

        # 스프라이트 시트를 조각내서 2차원 리스트로 저장
        for j in range(self.sprite_column):
            temp_column = []
            for i in range(self.sprite_row):

                # 오른쪽 부분 애니메이션
                if i < self.sprite_row // 2:
                    temp_column.append(self.subimage(self.sprite_sheet_R, \
                                                     self.sprite_width * i, self.sprite_height * j,
                                                     self.sprite_width * (i + 1), self.sprite_height * (j + 1)))

                # 왼쪽 부분 애니메이션
                else:
                    i2 = i - self.sprite_row // 2;
                    temp_column.append(self.subimage(self.sprite_sheet_L, \
                                                     self.sprite_width * i2, self.sprite_height * j,
                                                     self.sprite_width * (i2 + 1), self.sprite_height * (j + 1)))
            self.animation_sprites.append(temp_column)

        # 실제 화면상에 나타날 이미지
        self.sprite = canvas.create_image(self.x, self.y, image=self.animation_sprites[0][0])

    # 부분 이미지로 쪼개주는 함수
    def subimage(self, spritesheet, l, t, r, b):
        dst = PhotoImage()
        dst.tk.call(dst, 'copy', spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst

    def set_destination(self, event: Event):
        self.is_stopped = False
        self.des_x = event.x
        self.des_y = event.y

    def move(self):
        if self.is_stopped:
            return

        # 목표 지점까지 남은 거리 및 각도
        dx = self.des_x - self.x
        dy = self.des_y - self.y
        theta = math.atan2(dy, dx);

        # 단위시간당 이동할 수 있는 거리만큼 이동 or
        # 단위시간당 이동할 수 있는 거리보다 적게 남았으면 그만큼만 이동
        # 정지 시 애니메이션 X.
        move_length = self.speed
        left_length = math.sqrt(dx * dx + dy * dy)
        if left_length < move_length:
            self.time_index = 0
            move_length = left_length
            self.is_stopped = True

        # 유닛이 돌아간 정도
        self.rot_index = (int)(
            (theta + math.pi / 2 + math.pi / self.sprite_row) / (math.pi / (self.sprite_row // 2)) + self.sprite_row)
        self.rot_index %= self.sprite_row

        # 유닛 이미지 업데이트
        self.canvas.itemconfig(self.sprite,
                               image=self.animation_sprites[(self.time_index // 3) % 9 + 4][self.rot_index])
        self.time_index += 1

        # 유닛 이동
        self.canvas.move(self.sprite, move_length * math.cos(theta), move_length * math.sin(theta))

        # x, y 상태 변화
        self.x += move_length * math.cos(theta)
        self.y += move_length * math.sin(theta)

    def set_attack(self, event: Event):
        self.is_attacking = not self.is_attacking

    def attack(self):
        if self.is_stopped and self.is_attacking:
            self.canvas.itemconfig(self.sprite,
                                   image=self.animation_sprites[(self.time_index // 10) % 2 + 2][self.rot_index])

    def idle(self):
        self.canvas.itemconfig(self.sprite, image=self.animation_sprites[(self.time_index // 30) % 2][self.rot_index])

    def set_health(self, event: Event):
        if event.keysym == 'Left':
            self.health -= 1

    def die(self):
        self.canvas.itemconfig(self.sprite, image=self.animation_sprites[13][(self.time_index // 10)])

    def update(self):
        if self.health <= 0:
            if not self.is_dead:
                self.is_dead = True
                self.time_index = 0
            if self.time_index > 80:
                self.remove_flag = True
            self.die()

        elif self.is_stopped:
            if self.is_attacking:
                self.attack()
            else:
                self.idle()
        else:
            self.move()
        self.time_index += 1


g = Game()
g.mainLoop()
