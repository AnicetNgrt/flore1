import math

# ------------------------------------------------------------
# ------------------    FLIPBOOK CLASS   ---------------------
# ------------------------------------------------------------
class Flipbook:
    def __init__(self, Refresh, Sprite, assets, fps=24, sync=True):
        self.Refresh = Refresh
        self.asset_list = assets

        def play(Sprite, asset_list, fps):
            if not hasattr(play, "last_frame"):
                play.last_frame = -1
            if not hasattr(play, "frame"):
                play.frame = 0
            if not hasattr(play, "speed"):
                fps_ratio = play.refresh.fps / fps
                if fps_ratio > 1:
                    play.speed = 1 / fps_ratio
                else:
                    play.speed = fps_ratio

            #print("\033["+str(len(asset_list)-1)+";1H "+("%2s" % str(play.speed)))
            #print("\033["+str(len(asset_list))+";1H "+("%2s" % str(play.last_frame)))

            play.frame = play.speed * play.i
            crt_frame = math.floor(play.frame) % len(asset_list)

            if crt_frame != play.last_frame:
                Sprite.set_asset(asset_list[crt_frame])

            play.last_frame = crt_frame

        play.sync = sync
        self.material = (play, Sprite, self.asset_list, fps)

# ------------------------------------------------------------

    def start(self):
        if not self.Refresh.is_fed_with(*self.material):
            self.Refresh.feed(*self.material)
            return True
        else:
            return False

# ------------------------------------------------------------

    def stop(self):
        if self.Refresh.is_fed_with(*self.material):
            self.Refresh.terminate(*self.material)
            return True
        else:
            return False
# ------------------------------------------------------------
