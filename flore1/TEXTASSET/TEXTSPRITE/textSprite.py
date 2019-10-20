"""/////////////////////////
///
///   File: TEXTASSET/TEXTSPRITE/textSprite.py
///   Author: Anicet Nougaret
///   QuickDesc: The Text Asset's "text sprite" subclass
///   License: CC BY-SA (see FLORE1/license.txt)
///
/////////////////////////"""


# ------------------------------------------------------------
# ------------------   TextSprite Class  ---------------------
# ------------------------------------------------------------
class TextSprite:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.layer = None
    self.scene = None
    self.chart = None
    self.prtcrd = set()
    self.act_prtcrd = set()

# ------------------------------------------------------------

  def set_asset(self,asset):
    self.chart = asset.chart

    if self.scene != None:
        self.scene.frame_event = True

    if (self.x != 0 or self.y != 0) and asset.prtcrd != self.prtcrd:
      self.prtcrd = asset.prtcrd.copy()
      self.act_prtcrd = set()

      if self.scene != None:
        for px in self.prtcrd:
          x, y = px

          if 0 < x + self.x < self.scene.res_x and 0 < y + self.y < self.scene.res_y:
            self.act_prtcrd.add((x+self.x,y+self.y))
    else:
      self.prtcrd = set(asset.prtcrd)
# ------------------------------------------------------------
