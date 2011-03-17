#!/usr/bin/env python

import VisionEgg
from VisionEgg.Core import Stimulus, get_default_screen
from VisionEgg.Text import Text

from itertools import chain


class Panel:
    """Information for a panel in the grid
    """
    def __init__(self, position, size, coords, on = 0, label = ''):
        """Accept a position, size, and label for each panel, and
        infer some other measurements """

        self.position = position
        self.size = size
        self.coords = coords
        self.label = label

        self.stimulus = Stimulus()

        self.left = position[0]
        self.bottom = position[1]
        self.width = size[0]
        self.height = size[1]
        self.right = self.left + self.width
        self.top = self.bottom + self.height
        self.center = (self.left + self.width/2, self.bottom + self.height/2)

    def draw(self, t = None):
        """Draw the stimulus
        
        Arguments:
        - `self`:
        
        """
        self.stimulus.draw()

    def turn_on(self, t = None):
        """Set stimulus.on to 1 if it exists
        """
        try:
            self.stimulus.on = 1
        except:
            pass

    def turn_off(self, t = None):
        """Set stimulus.on to 0 if it exists
        
        Arguments:
        - `self`:
        """
        try:
            self.stimulus.off = 0
        except:
            pass



class Grid:
    """A list of list of panels.
    """
    def __init__(self, nrow, ncol, screen, anchor = 'center'):
        """Accept number of columns and rows, and how to anchor stimuli
        """
        self.nrow = nrow
        self.ncol = ncol
        self.screen = screen
        self.anchor = anchor

        self.npanels = nrow*ncol

        self.panel = []
        
        for i in xrange(nrow):
            self.panel.append([])
            for j in xrange(ncol):
                p = Panel(size = (screen.size[0]/ncol,
                                  screen.size[1]/nrow),
                          position = ((j) * screen.size[0]/ncol,
                                      (i) * screen.size[1]/nrow),
                          coords = (i, j),
                          label = "(%d, %d)" % (i, j))
                p.stimulus = Text(text = p.label,
                                  position = p.center,
                                  anchor = anchor)
                self.panel[i].append(p)

        self.all_panels = list(chain.from_iterable(self.panel))
        
    def draw(self, t = None):
        """Draw the stimulus in each panel
        
        Arguments:
        - `self`:
        """
        [p.draw() for p in self.all_panels]

    def turn_on(self, t = None):
        """Turn on all panels
        
        Arguments:
        - `self`:
        """
        [p.turn_on() for p in self.all_panels]

    def turn_off(self, t = None):
        """Turn off all panels
        
        Arguments:
        - `self`:
        """
        [p.turn_off() for p in self.all_panels]


