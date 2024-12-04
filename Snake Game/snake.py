location = [(0,0) , (-20,0) ,(-40,0),]
perpindahan_jarak = 20
from turtle import Turtle
ATAS = 90
BAWAH = 270
KANAN = 0
KIRI = 180

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head =  self.segment[0]

    def create_snake(self):
        for posisi in location:
           self.tambah_segment(posisi)
    
    def tambah_segment(self, posisi):
            segment_baru = Turtle("square")
            segment_baru.color("white")
            segment_baru.goto(posisi)
            segment_baru.penup()
            self.segment.append(segment_baru)

    def memperpanjang(self):
        self.tambah_segment(self.segment[-1].position())


    def move(self):
        for seg_num in range(len(self.segment) - 1 , 0 , -1):
            x_baru = self.segment[seg_num -1].xcor()
            y_baru = self.segment[seg_num -1].ycor()
            self.segment[seg_num].goto(x_baru , y_baru)
        self.segment[0].forward(perpindahan_jarak)        

    def up(self):
        if self.head.heading() != BAWAH:
            self.head.setheading(90)
    
    def down(self):
     if self.head.heading() != ATAS:
         self.head.setheading(270)
    
    def right(self):
     if self.head.heading() != KIRI:
        self.head.setheading(0)
    
    def left(self):
     if self.head.heading() != KANAN:
            self.head.setheading(180)
