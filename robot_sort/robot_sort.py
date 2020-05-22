class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    # *** THE PLAN ***
    # Implement using bubble sort. The light on the
    # robot will keep track of whether any swaps were
    # made in an iteration. If a swap is made at any
    # point in an iteration, the light will be turned on.
    # If no swap is made, the light will remain off, and
    # the list is done being sorted.
    
    # I think sort() is O(n^3) because of the way I
    # have to go back to the beginning of the list
    # once I've hit the end. But it's possible it's O(n^2)
    def sort(self):
        """
        Sort the robot's list.
        """
        # the light being on represents whether any swaps 
        # were performed on any given iteration. If no
        # swaps were performed, the light will remain off.
        self.set_light_on() # <- set the light on initially to enter the while loop
        while self.light_is_on():
            self.set_light_off() # <- turn it back off
            # while we are able to move right,
            while self.can_move_right(): # <- O(n) because the fn() inside is what moves the position forward
                # swap the item at list[position+1]
                # if list[position] is larger
                self.swap_right_item_if_smaller() 
            # if we can't move right any further,
            if not self.can_move_right():
                # move back to the start of the list,
                self.move_to_start() # <- O(n)
    
    # move's the list position to the start
    def move_to_start(self):
        while self.can_move_left(): # O(n)
            self.move_left()
            
    def swap_right_item_if_smaller(self):
        # if the item to the right of the
        # current position is smaller, swap
        # the item at the current position 
        # with the item at the next position
        
        # load the current position into item
        # and go to the next position
        self.swap_item()
        self.move_right()
        
        # compare the items. If the currently
        # selected item is larger, swap with the
        # item whose position we are at
        if self.compare_item() == 1:
            # we are making a swap, so turn the
            # light on
            self.set_light_on()
            # the items need to be swapped
            self.swap_item()
            

        # now we need to move back, and swap again
        # item so that the robot's current item
        # is None again
        self.move_left()
        self.swap_item()
        self.move_right()
        # the robot's item is now None again
        

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    #l = [5, 4, 3, 2, 9, 1, 11, 4, 12, 15, 184, 19]
    
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)