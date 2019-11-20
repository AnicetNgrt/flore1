"""
File: engine_locals/flipbook.py
Author: Anicet Nougaret
Version: 19.11.2019.A
"""

import math

class Flipbook:
    """The class for TextSprite animation.

    The Flipbook object applies a collection of TextAsset objects to a TextSprite
    object one by one at a rythm in order to animate the TextSprite
    object.

    Attributes:
        Refresh (:obj:'<flore1.Refresh>'):
            The Refresh object that will handle animation speed and speed
            stabilization.
        asset_list (:obj:'list [<flore1.TextAsset object>]'):
            Assets list (frames) for the animation.
        material (:obj:'tuple (function, *args)'):
            Tuple containing the animation's play function and all it's params.
            The Flipbook object's Refresh has it added to it's execution stack
            for rythmed execution.
    """

    def __init__(self, Refresh, Sprite, assets, fps=24, sync=True):
        """Inits the Flipbook object.

        Args:
            Refresh (:obj:'<flore1.Refresh object>'):
                The Refresh object that will handle animation speed and speed
                stabilization.
            Sprite (:obj:'<flore1.TextSprite object>'):
                The TextSprite object which will be animated.
            assets (:obj:'list [<flore1.TextAsset object>]'):
                Assets list (frames) for the animation.
            fps (int, optional):
                Animation's frame per second goal. Defaults to 24.
            sync (bool, optional):
                Speed stabilization on/off. Defaults to True.
        """

        self.Refresh = Refresh
        self.asset_list = assets

        def play(Sprite, asset_list, fps):
            """Animation's function for running in a Refresh object's stack."""

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
        """Starts the animation from where it stopped last time"""

        if not self.Refresh.is_fed_with(*self.material):
            self.Refresh.feed(*self.material)
            return True
        else:
            return False

# ------------------------------------------------------------

    def stop(self):
        """Stops the animation"""

        if self.Refresh.is_fed_with(*self.material):
            self.Refresh.terminate(*self.material)
            return True
        else:
            return False
# ------------------------------------------------------------
