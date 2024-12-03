from sdl2 import *

# 이벤트 체크 함수를 정의
# 상태 이벤트 e = (종류, 실제값)

def start_event(e):
    return e[0] == 'START'

def d_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d

def d_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d

def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a

def w_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w

def w_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w

def s_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s

def s_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s

class StateMachine:
    def __init__(self, obj):
        self.obj = obj # 어떤 객체의 상태 머신인지 설정
        self.event_q = [] # 상태 이벤트를 보관할 큐

    def start(self, state):
        self.cur_state = state # 시작 상태를 받아서, 그걸로 현재 상태를 정의
        self.cur_state.enter(self.obj, ('START', 0))
        # print(f'Enter into {state}')

    def update(self):
        self.cur_state.do(self.obj)
        
        if self.event_q: # list는 요소가 존재하면 True
            e = self.event_q.pop(0) # 0 으로 설정하면 맨 앞에서 pop 수행
            # 현재 상태와 발생한 이벤트에 따라서 다음 상태를 결정 = 상태 변환 테이블
            for check_event, next_state in self.transitions[self.cur_state].items():
                if check_event(e):
                    self.cur_state.exit(self.obj, e)
                    self.cur_state = next_state
                    self.cur_state.enter(self.obj, e) # 상태 변환 이유를 구분
                    return # event에 따른 상태 변환 완료
            
    def draw(self):
        self.cur_state.draw(self.obj)

    def add_event(self, e):
        # print(f'    DEBUG: add event {e}')
        self.event_q.append(e)

    def set_transitions(self, transitions):
        self.transitions = transitions