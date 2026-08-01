class Head:
    def __init__(self, eyes, nose, mouth):
        self.eyes = eyes
        self.nose = nose
        self.mouth = mouth

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg, chest, stomach, back):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        self.chest = chest
        self.stomach = stomach
        self.back = back

class Arm:
    def __init__(self, hand, elbow):
        self.hand = hand
        self.elbow = elbow

class Hand:
    def __init__(self, fingers):
        self.fingers = fingers

class Leg:
    def __init__(self, knee, foot):
        self.knee = knee
        self.foot = foot

class Feet:
    def __init__(self, toes):
        self.toes = toes

class Human:
    def __init__(self, torso):
        self.torso = torso
        self.head = torso.head
        self.right_arm = torso.right_arm
        self.left_arm = torso.left_arm
        self.right_leg = torso.right_leg
        self.left_leg = torso.left_leg