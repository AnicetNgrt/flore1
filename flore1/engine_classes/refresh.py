import time

# ------------------------------------------------------------
# ------------------    REFRESH CLASS    ---------------------
# ------------------------------------------------------------
class Refresh:
    def __init__(self, fps=35):
        self.fps = fps
        self.pv_i = 0
        self.i = 0
        self.pv_frame = 0
        self.frame = 0
        self.stack = []

# ------------------------------------------------------------

    def terminate(self, func, *args, **kwargs):
        self.stack.remove((func, args, kwargs))

# ------------------------------------------------------------

    def is_fed_with(self, func, *args, **kwargs):
        if (func, args, kwargs) in self.stack:
            return True
        else:
            return False

# ------------------------------------------------------------

    def feed(self, func, *args, **kwargs):
        self.stack.append((func, args, kwargs))

# ------------------------------------------------------------

    def do(self):
        for func, args, kwargs in self.stack:
            if hasattr(func, "refresh") == False:
                func.__dict__["refresh"] = self
            if hasattr(func, "sync") == False:
                func.__dict__["sync"] = True
            if not hasattr(func, "i"):
                func.__dict__["i"] = 0
            if not hasattr(func, "last_i"):
                func.__dict__["last_i"] = 0
            else:
                func.__dict__["last_i"] = func.__dict__["i"]

                if func.sync == True and (self.frame-self.pv_frame) > 0:
                    func.__dict__["i"] += self.frame-self.pv_frame
                    func(*args, **kwargs)
                elif func.sync == False:
                    func.__dict__["i"] += 1
                    func(*args, **kwargs)



# ------------------------------------------------------------

    def run(self, debug=False):
        required_fps = self.fps

        start_time = time.time()

        self.do()

        exec_time = time.time()
        latency = exec_time - start_time

        if latency < 0.0001: latency = 0.0001

        fps = 1 / latency

        self.pv_frame = self.frame
        self.pv_i = self.i

        if fps > required_fps:
            time.sleep(((1 / required_fps) - latency)/1.1)
            self.i += 1

        if required_fps >= fps:
            self.i += required_fps / fps

        self.frame = round(self.i)
        #print(self.i)

        if debug:
            otp = "\33[0m\033[1;0H| >>>> Refresh.\33[34mrun \33[33mdebug"
            print(otp)

            otp = "\033[2;0H\33[0m|\u001b[38;5;15m\u001b[48;5;16m  INVERTED_LATENCY_CAP: "
            print(otp + str(self.fps))

            otp = "\33[0m\033[3;0H|\u001b[48;5;16m\u001b[38;5;15m  LATENCY: "
            print("%s%1.2f   " % (otp, latency))

            otp = "\033[4;0H\33[0m|\u001b[38;5;16m"
            if fps >= self.fps:
                otp += "\u001b[48;5;85m"
            elif self.fps * 0.8 <= fps < self.fps:
                otp += "\u001b[48;5;87m"
            elif self.fps * 0.5 <= fps < self.fps * 0.8:
                otp += "\u001b[48;5;221m"
            elif self.fps * 0.2 <= fps < self.fps * 0.5:
                otp += "\u001b[48;5;202m"
            else:
                otp += "\u001b[48;5;9m"
            otp += "  EXECUTION_FREQUENCY: "
            print("%s%1.2f   " % (otp, fps))

            otp = "\33[0m\033[5;0H|\u001b[48;5;16m\u001b[38;5;15m  FRAME_DIFF: "
            print("%s%1.2f   " % (otp, self.frame-self.pv_frame))

            otp = "\33[0m\033[6;0H|\u001b[48;5;16m\u001b[38;5;15m  ACCUMULATOR_DIFF: "
            print("%s%1.2f   " % (otp, self.i-self.pv_i))

            final_time = time.time()
            total_latency = final_time - start_time
            otp = "\33[0m\033[7;0H|\u001b[38;5;15m\u001b[48;5;16m  STABILISED_FREQUENCY: "
            print("%s%1.2f   " % (otp, (self.i - self.pv_i)/total_latency))

# ------------------------------------------------------------
