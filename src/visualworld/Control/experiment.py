class Repeater:
    """Base class for sessions, blocks, and trials.  Provides access
    to hooks, common attributes and implements interator interface.
    """
    def no_op(*args):
        """ do nothing
        """
        pass
    
    def __init__(self, data,
                 each_func = no_op,
                 first_func = no_op,
                 last_func = no_op):
        """Accept a sequence of data, and functions to run before the
        first member, on each member, and after the last member.

        Arguments:
        - `self`: the instantiated object

        - `each_func`: function executed on each item of the data.  is
          passed a single argument, the current item in the data.

        - `first_func`: function executed once, when the iterator is
          instantiated.  is passed a single argument, the first item
          in the data.

        - `last_func`: function executed once, when the iterator
          finishes.  is passed a single argument, the last item in the
          data.
    
        """
        self.data = data
        self.length = len(data)
        self.index = 0

        self.first_func = first_func
        self.each_func = each_func
        self.last_func = last_func
        
    def __iter__(self):
        """Implement the iterator interface
        """
        return self

    def next(self):
        """Go to the next element in the data
        """
        if self.index == 0:
            try:
                self.first_func(self.data[0])
            except:
                raise

        if self.index == self.length:
            # run last_func on the last item
            try:
                self.last_func(self.data[self.index - 1])
            except:
                raise
            raise StopIteration

        # grab the current element
        current = self.data[self.index]

        # call the each function on the current item
        try:
            self.each_func(current)
        except:
            raise

        # increment the counter
        self.index = self.index + 1
        # return the current item
        return current
