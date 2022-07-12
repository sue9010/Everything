import tkinter
import cv2
import PIL.Image
import PIL.ImageTk
import datetime


class App:
    def __init__(self, window, window_title):
        video_source = 'rtsp://admin:cg600ip100m@169.254.0.100/PSIA/Streaming/channels/0 : Stream 0'
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.is_recording = False

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(
            window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot = tkinter.Button(
            window, text="녹화 시작", width=20, height=5, command=self.record)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.fps = self.vid.webcam.get(cv2.CAP_PROP_FPS)
        self.delay = round(1000.0/self.fps)
        self.update()

        self.window.mainloop()

    def record(self):
        self.is_recording = ~self.is_recording
        if self.is_recording:
            self.vid.create_video(self.fps)
            self.btn_snapshot.config(text="녹화 중단")
        else:
            self.vid.video.release()
            self.btn_snapshot.config(text="녹화 시작")

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            if self.is_recording:
                self.vid.video.write(frame)

            self.photo = PIL.ImageTk.PhotoImage(
                image=PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.window.after(self.delay, self.update)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.is_recording:
            self.vid.video.release()


class MyVideoCapture:
    def __init__(self):
        video_source = 'rtsp://admin:cg600ip100m@169.254.0.100/PSIA/Streaming/channels/0 : Stream 0'
        # Open the video source
        self.webcam = cv2.VideoCapture(video_source)
        if not self.webcam.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        # self.width = self.webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
        # self.height = self.webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.width = 640
        self.height = 480
        #self.webcam.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        #self.webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    def create_video(self, fps):
        file_name = str(datetime.datetime.now()) + '.mp4'
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # opencv 3.0
        # Error: 'module' object has no attribute 'VideoWriter_fourcc'
        # fourcc=cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        # jpeg,h263,'m', 'p', '4', 'v'
        self.video = cv2.VideoWriter(
            file_name, fourcc, fps/3.0, (self.width, self.height))

    def get_frame(self):
        if self.webcam.isOpened():
            font_color = (255, 255, 255)
            ret, frame = self.webcam.read()
            if ret:
                frame = cv2.flip(frame, 1)

                # describe the type of
                # font you want to display
                font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

                # Get date and time and
                # save it inside a variable
                dt = str(datetime.datetime.now())

                # put the dt variable over the
                # video frame
                frame = cv2.putText(frame, dt,
                                    (30, 60),    # position
                                    font, 1, font_color, 4, cv2.LINE_AA)

                # Return a boolean success flag and the current frame converted to BGR
                return (ret, frame)
            else:
                return (ret, None)
        else:
            return (False, None)

     # Release the video source when the object is destroyed
    def __del__(self):
        if self.webcam.isOpened():
            self.webcam.release()


# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")
