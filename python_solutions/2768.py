class Solution:
    def is_valid_coordinates(self, coordinates, m, n):
        for coordinate in coordinates:
            if coordinate[0] < 0 or coordinate[0] >= m:
                return False
            if coordinate[1] < 0 or coordinate[1] >= n:
                return False
        return True

    def get_blocks_around_coordinate(self, x, y, m, n):
        res = {}  # key will be location of [x,y] in the block (which will be the value of the key)
        # check for bottom right corner
        if self.is_valid_coordinates([[x - 1, y - 1], [x - 1, y], [x, y - 1], [x, y]], m, n):
            res["bottom_right"] = [[x - 1, y - 1], [x - 1, y], [x, y - 1], [x, y]]
        # check for top right corner
        if self.is_valid_coordinates([[x, y - 1], [x, y], [x + 1, y - 1], [x + 1, y]], m, n):
            res["top_right"] = [[x, y - 1], [x, y], [x + 1, y - 1], [x + 1, y]]
        # check for bottom left corner
        if self.is_valid_coordinates([[x - 1, y], [x - 1, y + 1], [x, y], [x, y + 1]], m, n):
            res["bottom_left"] = [[x - 1, y], [x - 1, y + 1], [x, y], [x, y + 1]]
        # check for top left corner
        if self.is_valid_coordinates([[x, y], [x, y + 1], [x + 1, y], [x + 1, y + 1]], m, n):
            res["top_left"] = [[x, y], [x, y + 1], [x + 1, y], [x + 1, y + 1]]
        return res

    def get_black_cell_count(self, blocks, coordinates_hashmap):
        black_cell_count = 0
        for block in blocks:
            if tuple(block) in coordinates_hashmap:
                black_cell_count += 1
        return black_cell_count

    def is_already_calculated(self, coordinate_location, block, x, y, coordinates_hashmap):
        if coordinate_location == "top_left":
            # in this block the coordinate is present at the top_left
            # , as we are doing the calculation in sorted order (so this is first time we are counting this block)
            #           B =
            #           = =
            # { here B : [x,y] , = is the location of coordinates which we have not visited yet) }
            # in the above picture it clear that this block is appeared first time (due to scanning the coordinates in sorted order)
            pass
        if coordinate_location == "top_right":
            # in this block the coordinate is present at the top_right
            # , as we are doing the calculation in sorted order than it might be the case that the top_left cell was black and this block is already counted
            #           # B
            #           = =
            # { here B : [x,y] ,# : already visited coordinates , =  : is the location of coordinates which we have not visited yet) }
            # check that '#' is cell with black color
            if tuple([x, y - 1]) in coordinates_hashmap:
                # we have already counted this block while doing the calculation for [x,y-1]
                return True
        if coordinate_location == "bottom_left":
            # in this block the coordinate is present at bottom left
            # , as we are doing the calculation in sorted order than it might be the case that the top_left or top_right cell was black and this block is already counted
            #           # #
            #           B =
            # { here B : [x,y] ,# : already visited coordinates , =  : is the location of coordinates which we have not visited yet) }

            # check that [x-1,y] is cell with black color
            if tuple([x - 1, y]) in coordinates_hashmap:
                return True
            # check that [x-1,y+1] is cell with black color
            if tuple([x - 1, y + 1]) in coordinates_hashmap:
                return True
        if coordinate_location == "bottom_right":
            # in this block the coordinate is present at bottom right
            # , as we are doing the calculation in sorted order than it might be the case that the top_left or top_right or bottom_left cell was black and this block is already counted
            #           # #
            #           # B
            # { here B : [x,y] ,# : already visited coordinates) }

            # check that [x-1,y-1] is cell with black color
            if tuple([x - 1, y - 1]) in coordinates_hashmap:
                return True
            # check that [x-1,y] is cell with black color
            if tuple([x - 1, y]) in coordinates_hashmap:
                return True
            # check that [x,y-1] is cell with black color
            if tuple([x, y - 1]) in coordinates_hashmap:
                return True
        return False

    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        # overview of solution
        # we know that there are only (m-1) * (n-1) blocks
        # if we are able to find the arr[1] , arr[2] , arr[3] , arr[4]
        # then arr[0] = (m-1)*(n-1) - arr[1] - arr[2] - arr[3] - arr[4]
        # now to find arr[1],arr[2],arr[3],arr[4] we only need to consdier coordinates array
        # for given coordinate we will consider the blocks around this coordinate and find update the values of arr[1],arr[2],arr[3],arr[4] accordingly
        # pictorial view of [x,y] being at center
        #           = = =
        #           = * =
        #           = = =
        # here we have four blocks to consider as follows :
        # 1. [x,y] at the bottom right corner of the block
        #               = =
        #               = *
        # 2. [x,y] at the top right corner of the block
        #               = *
        #               = =
        # 3. [x,y] at the bottom left corner of the block
        #               = =
        #               * =
        # 4. [x,y] at the top left corner of the block
        #               * =
        #               = =
        # now to update the answer we only need to check the color of cell with equal sign in our presentation for [x,y]
        # to find quickly the color of coordinates around it, we can take help of hashmap

        coordinates.sort(key=lambda x: (x[0], x[1]))
        coordinates_hashmap = {}
        arr = [0 for i in range(5)]
        for coordinate in coordinates:
            coordinate_tuple = tuple(coordinate)
            coordinates_hashmap[coordinate_tuple] = True
        for coordinate in coordinates:
            x, y = coordinate
            blocks = self.get_blocks_around_coordinate(x, y, m, n)
            for key, block in blocks.items():
                black_cell_count = self.get_black_cell_count(block, coordinates_hashmap)
                # there might be the case that we have already counted this block
                if not self.is_already_calculated(key, block, x, y, coordinates_hashmap):
                    arr[black_cell_count] += 1
        arr[0] = (m - 1) * (n - 1) - arr[1] - arr[2] - arr[3] - arr[4]
        return arr
