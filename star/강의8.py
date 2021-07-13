from tkinter import *
import math
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Game")
        self.tk.resizable(0,0)
        self.tk.wm_attributes("-topmost",1)

        self.canvas = Canvas(self.tk, width=500, height=500)
        self.canvas.pack()

    def mainLoop(self):
        self.unit_manager = UnitManager(self.canvas)
        for i in range(5):
            self.unit_manager.add_unit(Marine(30, 30 * i, self.canvas))
                                       
        while True:
            self.unit_manager.update()
            self.tk.update()
            time.sleep(0.01)

class Marine:
    
    STATE_IDLE = 0
    STATE_ATTK = 1
    STATE_MOVE = 2
    STATE_DEAD = 3
    
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
        self.state = Marine.STATE_IDLE
        self.next_state = Marine.STATE_IDLE
        self.remove_flag = False
        self.health = 5
        

        # 표 크기 및 오프셋, 애니메이션 프레임 갯수
        self.sprite_row = 32
        self.sprite_column = 14
        
        # [idle, attack, move, death]
        self.animation_frame_number = [2,2,9,8]
        self.animation_frame_offset = [0,2,4,13]
        self.animation_speed = [30,5,5,5]

        # 왼쪽과 오른쪽 스프라이트 셋
        self.sprite_sheet_L = PhotoImage(file="Marine_L.gif")
        self.sprite_sheet_R = PhotoImage(file="Marine_R.gif")

        # 스프라이트 크기
        self.sprite_width = 64
        self.sprite_height = 64

        # 애니메이션을 위한 인덱스
        self.animation_counter = 0
        self.current_frame_number = 0
        self.rot_index = 0
        
        # 애니메이션 이미지들을 담을 2차원 리스트
        self.animation_sprites = []
        
        # 스프라이트 시트를 조각내서 2차원 리스트로 저장
        for j in range(self.sprite_column):
            temp_column = []
            for i in range(self.sprite_row):
                
                # 오른쪽 부분 애니메이션
                if i < self.sprite_row//2:
                    temp_column.append(self.subimage(self.sprite_sheet_R, \
                            self.sprite_width*i, self.sprite_height*j,self.sprite_width*(i+1), self.sprite_height*(j+1)))
                    
                # 왼쪽 부분 애니메이션
                else:
                    i2 = i-self.sprite_row//2;
                    temp_column.append(self.subimage(self.sprite_sheet_L, \
                            self.sprite_width*i2, self.sprite_height*j, self.sprite_width*(i2+1), self.sprite_height*(j+1)))
            self.animation_sprites.append(temp_column)

        # 실제 화면상에 나타날 이미지
        self.sprite = canvas.create_image(self.x,self.y,image=self.animation_sprites[0][0])

    def subimage(self, spritesheet, l, t, r, b):
        dst = PhotoImage()
        dst.tk.call(dst, 'copy', spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst
    
    def set_destination(self, event: Event):
        self.next_state = Marine.STATE_MOVE
        self.des_x = event.x
        self.des_y = event.y
        
    def set_attack(self, event: Event):
        if self.state is not Marine.STATE_ATTK:
            self.next_state = Marine.STATE_ATTK
        else:
            self.next_state = Marine.STATE_IDLE

    def set_health(self, event:Event):
        if event.keysym == 'Left':
            self.health -=1
            
    def update_sprite(self):
        frame_offset = self.animation_frame_offset[self.state]
        frame_number = self.animation_frame_number[self.state]
        animation_speed = self.animation_speed[self.state]

        # 일정 횟수의 업데이트가 지나면 frame을 하나 증가시킴 (애니메이션 속도 조절)
        if self.animation_counter is animation_speed:
            self.animation_counter = 0
            self.current_frame_number += 1

        # 애니메이션 프레임이 끝에 도달하면 다시 0으로 돌아감 (반복 재생)
        # 죽는 경우는 remove_flag를 true로 바꿔 제거해줌.
        if self.current_frame_number >= frame_number:
            if self.state is Marine.STATE_DEAD:
                self.remove_flag = True
                self.canvas.itemconfig(self.sprite, image = '')
                return
            self.current_frame_number = 0

        # 스프라이트 업데이트
        if self.state is Marine.STATE_DEAD:
            self.canvas.itemconfig(self.sprite, image=self.animation_sprites[self.animation_frame_offset[Marine.STATE_DEAD]][self.current_frame_number])
        else:
            self.canvas.itemconfig(self.sprite, image=self.animation_sprites[self.current_frame_number + frame_offset][self.rot_index])
        
    def move(self):
        if self.state is not Marine.STATE_MOVE:
            return
        
        # 목표 지점까지 남은 거리 및 각도
        dx = self.des_x - self.x
        dy = self.des_y - self.y
        theta = math.atan2(dy, dx);

        # 단위시간당 이동할 수 있는 거리만큼 이동 or
        # 단위시간당 이동할 수 있는 거리보다 적게 남았으면 그만큼만 이동
        # 정지 시 애니메이션 X.
        move_length = self.speed
        left_length = math.sqrt(dx*dx + dy*dy)
        if left_length < move_length:
            move_length = left_length
            self.next_state = Marine.STATE_IDLE

        # 유닛이 돌아간 정도
        self.rot_index = (int)((theta + math.pi/2 + math.pi/self.sprite_row)/(math.pi/(self.sprite_row//2)) + self.sprite_row)
        self.rot_index %= self.sprite_row
        
        # 유닛 이동
        self.canvas.move(self.sprite, move_length * math.cos(theta), move_length * math.sin(theta))

        # x, y 상태 변화
        self.x += move_length * math.cos(theta)
        self.y += move_length * math.sin(theta)
        
    def check_dead(self):
        if self.health <=0:
            self.next_state = Marine.STATE_DEAD
            
    def update(self):
        self.check_dead()
        self.move()
        self.update_sprite()
        self.animation_counter += 1

        # 상태 변화시 카운터 초기화
        if self.next_state is not self.state:
            self.animation_counter = 0
        self.state = self.next_state

class UnitManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.unit_list = []
        
        # 마우스 클릭 연결
        self.canvas.bind_all('<Button-3>', self.set_destination)
        self.canvas.bind_all('<Button-1>', self.set_attack)
        self.canvas.bind_all('<KeyPress>', self.set_health)

    def add_unit(self, unit):
        self.unit_list.append(unit)

    def update(self):
        temp_list = []
        for unit in self.unit_list:
            unit.update()
            
            # 이터레이션 도중 리스트 변경 불가하기 때문에
            # 새로운 리스트를 만들어서 옮겨담음.
            if not unit.remove_flag:
                temp_list.append(unit)
                
        self.unit_list = temp_list

    def set_destination(self, event: Event):
        for unit in self.unit_list:
            unit.set_destination(event)

    def set_attack(self, event: Event):
        for unit in self.unit_list:
            unit.set_attack(event)

    def set_health(self, event: Event):
        for unit in self.unit_list:
            unit.set_health(event)
        
g = Game()
g.mainLoop()
