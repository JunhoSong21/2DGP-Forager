import game_framework
import game_world
import pico2d
import state_machine

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Idle:
    @staticmethod
    def enter(forager, e):
        forager.image = pico2d.load_image('Sprites/Playeridle.png')
        forager.frame = 0
        forager.Xdir = 0
        forager.Ydir = 0

    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        forager.frame = (forager.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    @staticmethod
    def draw(forager):
        if forager.imageDir == 1:
            forager.image.clip_draw(
                int(forager.frame) * 15, 0, 15, 20, forager.x, forager.y, 45, 60
            )
        elif forager.imageDir == -1:
            forager.image.clip_composite_draw(
                int(forager.frame) * 15, 0, 15, 20, '', True, False, forager.x, forager.y, 45, 60
            )

class Run:
    @staticmethod
    def enter(forager, e):
        forager.image = pico2d.load_image('Sprites/Playerwalk.png')
        if state_machine.d_down(e) or state_machine.a_up(e):
            forager.Xdir = 1
        elif state_machine.a_down(e) or state_machine.d_up(e):
            forager.Xdir = -1

        if state_machine.w_down(e) or state_machine.s_up(e):
            forager.Ydir = 1
        elif state_machine.s_down(e) or state_machine.w_up(e):
            forager.Ydir = -1

        forager.frame = 0

    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        forager.frame = (forager.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        PIXEL_PER_METER = (10.0 / 0.3)
        RUN_SPEED_KMPH = 20.0
        RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
        forager.x += forager.Xdir * RUN_SPEED_PPS * game_framework.frame_time
        forager.y += forager.Ydir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(forager):
        forager.image.clip_draw(
            int(forager.frame) * 15, 0, 15, 20, forager.x, forager.y, 45, 60
        )

class Forager:
    def __init__(self):
        self.x, self.y = 960, 540
        self.frame = 0
        self.Xdir, self.Ydir = 0, 0
        self.image = pico2d.load_image('Sprites/Playeridle.png')
        self.imageDir = 1
        self.state_machine = state_machine.StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {state_machine.d_down: Run, state_machine.a_down: Run, state_machine.a_up: Run, state_machine.d_up: Run,
                       state_machine.w_down: Run, state_machine.w_up : Run, state_machine.s_down: Run, state_machine.s_up : Run},
                Run: {state_machine.d_down: Idle, state_machine.a_down: Idle, state_machine.d_up: Idle, state_machine.a_up: Idle,
                      state_machine.w_down: Idle, state_machine.w_up: Idle, state_machine.s_down: Idle, state_machine.s_up: Idle}
            }
        )
    
    def update(self):
        self.state_machine.update()

    def add_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

    def set_item(self, item):
        self.item = item
